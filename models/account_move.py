# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    matter_id = fields.Many2one(
        "sh.law.matter", string="Matter",
        tracking=True, ondelete="cascade")
    trial_ids = fields.Many2many(
        "sh.law.erp.trial", string="Trials",
        tracking=True)
    lawyer = fields.Many2one(
        "hr.employee", string="Lawyer",
        tracking=True, ondelete="cascade")
    payment_by = fields.Selection(
        selection=[
            ("trial", "Per Trial"),
            ("case", "Per Case"),
            ("hour", "Per Hour"),
        ], string="Payment By", readonly=True
    )
    hours = fields.Float("Hours")
    to_price_unit = fields.Monetary(string="Amount Per Case/Hour/Trial")

    @api.onchange("matter_id")
    def _onchange_sh_matter_auto_complete(self):

        # MAKE INVOICE LINE HERE
        # ==================================
        invoice_lines = []
        account_id = 1
        # income account
        categ_id = self.env["product.category"].sudo().search([], limit=1)
        if categ_id and categ_id.property_account_income_categ_id:
            account_id = categ_id.property_account_income_categ_id.id

        if self.payment_by == "trial" and self.trial_ids:
            for trial in self.trial_ids:
                move_line_dic = {
                    "name": trial.name,
                    "quantity": 1,
                    "price_unit": self.to_price_unit,
                    "move_id": self.id,
                    "account_id": account_id,
                }

                invoice_lines.append(move_line_dic)

        elif self.payment_by == "case":
            move_line_dic = {
                "name": "Case",
                "quantity": 1,
                "price_unit": self.to_price_unit,
                "move_id": self.id,
                "account_id": account_id
            }
            invoice_lines.append(move_line_dic)

        elif self.payment_by == "hour":
            move_line_dic = {
                "name": "Hour",
                "quantity": self.hours,
                "price_unit": self.to_price_unit,
                "move_id": self.id,
                "account_id": account_id
            }
            invoice_lines.append(move_line_dic)

        if invoice_lines:
            new_lines = self.env["account.move.line"]
            for line in invoice_lines:

                new_line = new_lines.new(line)
                new_line._onchange_price_subtotal()
                new_lines += new_line
            new_lines._onchange_mark_recompute_taxes()

        self._compute_tax_totals_json()
        self._onchange_invoice_line_ids()
        self._compute_amount()
        self._recompute_dynamic_lines(recompute_tax_base_amount=True)
