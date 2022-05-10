# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawMatterType(models.Model):
    _name = "sh.law.matter.type"
    _description = "Law Matter Type"
    _order = "id desc"

    name = fields.Char(string="Matter", required=True)
    matter_code = fields.Char(string="Matter Code", required=True)
