# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models


class ShLawErpEvidence(models.Model):
    _name = "sh.law.erp.evidence"
    _inherit = ["portal.mixin", "mail.thread",
                "mail.activity.mixin", "utm.mixin"]
    _description = "Law Erp Evidence"
    _order = "id desc"

    name = fields.Char("Name", required=True, tracking=True)
    favor = fields.Many2one(
        "sh.law.erp.favor", string="In Favor", tracking=True)
    client = fields.Many2one(
        "res.partner", string="Client", tracking=True)
    matter_id = fields.Many2one(
        "sh.law.matter", string="Matter",
        tracking=True, required=True)
    attach_file = fields.Many2many(
        "ir.attachment", "class_ir_attachments_rel",
        "class_id", "attachment_id", "Attachments")
    description = fields.Text(string="Description",
                              tracking=True)
