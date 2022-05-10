# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawErpFavor(models.Model):
    _name = "sh.law.erp.favor"
    _description = "Law Erp Favor"
    _order = "id desc"

    name = fields.Char("Name", required=True)
