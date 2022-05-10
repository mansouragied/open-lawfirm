# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawErpVictim(models.Model):
    _name = "sh.law.erp.victim"
    _description = "Law Erp Victim"
    _order = "id desc"

    name = fields.Char(string="Name", required=True)
    contact = fields.Char(string="Contact Number")
