# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawErpTrial(models.Model):
    _name = "sh.law.erp.trial"
    _inherit = ["portal.mixin", "mail.thread",
                "mail.activity.mixin", "utm.mixin"]
    _description = "Law Erp Trial"
    _order = "id desc"

    name = fields.Char(string="Trial Name", required=True,
                       tracking=True)
    partner_id = fields.Many2one(
        "res.partner", string="Client", tracking=True)
    trial_date = fields.Datetime("Trial Date", tracking=True)
    close_date = fields.Datetime("Close Date")
    judge_id = fields.Many2one("sh.law.erp.judge", string="Judge")
    matter = fields.Many2one(
        "sh.law.matter", string="Matter", tracking=True, required=True)
    court_name_id = fields.Many2one(
        "sh.law.erp.courts", string="Court Name", tracking=True)
    invoice_id = fields.Many2one(
        "account.move", string="Invoice", tracking=True)
    description = fields.Text(string="", tracking=True)
    state = fields.Selection(
        selection=[
            ("draft", "Open"),
            ("close", "Close"),
        ], string="Status", default="draft", readonly=True
    )
    invoice_count = fields.Integer(
        "Invoice Count", compute="_compute_action_view_invoices")

    #Current Close Date
    def trial_close(self):
        self.write({"state": "close",
                    "close_date": fields.Datetime.now()})

    def trial_open(self):
        self.write({"state": "draft"})

    def _compute_action_view_invoices(self):
        invoices = self.env["account.move"]

        if self:
            for rec in self:
                invoices = invoices.search([
                    ("trial_ids", "in", [rec.id])
                ])
                if invoices:
                    rec.invoice_count = len(invoices.ids)
                else:
                    rec.invoice_count = 0
    def action_view_invoices(self):
        invoices = self.env["account.move"]
        if self:
            for rec in self:
                invoices = invoices.search([
                    ("trial_ids", "in", [rec.id])
                ])
        return{
            "name": "Invoices",
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "view_mode": "tree,form",
            "domain": [("id", "in", invoices.ids)],
            "context": {"default_move_type": "out_invoice"},
            "target": "current",
        }
