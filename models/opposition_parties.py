# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawErpOppositionParties(models.Model):
    _name = "sh.law.erp.opposition.parties"
    _description = "Law Erp Opposition Parties"
    _rec_name = "party_id"
    _order = "id desc"

    party_id = fields.Many2one("res.partner", string="Name", required=True)
    contact = fields.Char(string="Contact")
