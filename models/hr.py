# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id

    wage_per_trial = fields.Monetary(string="Wage Per Trial")
    wage_per_case = fields.Monetary(string="Wage Per Case")
    wage_per_hour = fields.Monetary(string="Wage Per Hour")
    practise_area = fields.Many2many(
        "sh.law.practise.area", string="Practise Area")
    currency_id = fields.Many2one(
        "res.currency",
        default=_get_default_currency_id, required=True)
    is_lawyer = fields.Boolean(string="Is Lawyer")

    def matter_report_btn(self):
        self.ensure_one()
        datas = self.read(fields=None)[0]
        return self.env.ref(
            "sh_law_erp.action_report_matter"
            ).report_action([], data=datas)


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id

    wage_per_trial = fields.Monetary(string="Wage Per Trial")
    wage_per_case = fields.Monetary(string="Wage Per Case")
    wage_per_hour = fields.Monetary(string="Wage Per Hour")
    practise_area = fields.Many2many(
        "sh.law.practise.area", string="Practise Area")
    currency_id = fields.Many2one(
        "res.currency", default=_get_default_currency_id, required=True)
    is_lawyer = fields.Boolean(string="Is Lawyer")
