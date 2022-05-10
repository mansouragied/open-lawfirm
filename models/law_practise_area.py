# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawPractiseArea(models.Model):
    _name = "sh.law.practise.area"
    _description = "Law Practise Area"
    _order = "id desc"

    name = fields.Char(string="Law Selection", required=True)
