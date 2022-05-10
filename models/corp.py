# -*- coding: utf-8 -*-

from odoo import fields, models


class ShLawErpCorp(models.Model):
    _name = "sh.law.erp.corp"
    _description = "Law Firm Corporate"
    _order = "id desc"

    name = fields.Char(string="Corporate", required=True)
    contact = fields.Char(string="Contact", required=True)