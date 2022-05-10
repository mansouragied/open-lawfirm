# -*- coding: utf-8 -*-

from odoo import fields, models


class ShLawErpJudge(models.Model):
    _name = "sh.law.erp.judge"
    _description = "Law Firm Judge"
    _order = "id desc"

    name = fields.Char(string="Name", required=True)
    contact = fields.Char(string="Contact Number")
