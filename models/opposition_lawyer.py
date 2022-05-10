# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawErpOppositionLawyer(models.Model):
    _name = "sh.law.erp.opposition.lawyer"
    _description = "Law Erp Opposition Lawyer"
    _rec_name = "employee_id"
    _order = "id desc"

    employee_id = fields.Many2one("hr.employee", string="Name", required=True)
    contact = fields.Char(string="Contact")
