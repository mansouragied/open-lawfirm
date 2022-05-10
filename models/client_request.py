# -*- coding: utf-8 -*-

from odoo import fields, models


class ShLawClientRequest(models.Model):
    _name = "sh.law.client.request"
    _inherit = ["portal.mixin", "mail.thread",
                "mail.activity.mixin", "utm.mixin"]
    _description = "Law Client Request"
    _order = "id desc"

    name = fields.Char(string="Client Name", required=True)
    street = fields.Char("Street")
    street2 = fields.Char("Street2")
    city = fields.Char("City", tracking=True)
    state_id = fields.Many2one(
        "res.country.state", string="State",
        tracking=True)
    zip = fields.Char("Zip", change_default=True,
                      tracking=True)
    country_id = fields.Many2one(
        "res.country", string="Country",
        tracking=True)
    related_partner_id = fields.Many2one(
        "res.partner", string="Related Profile",
        ondelete="cascade", readonly=True)
    phone = fields.Char(string="Phone Number", required=True,
                        tracking=True)
    mobile = fields.Char(string="Mobile Number", required=True,
                         tracking=True)
    email = fields.Char(string="Email")
    identity = fields.Char(string="Identity Number")
    reject_reason = fields.Text("Reject Reason")
    matter_id = fields.Many2one(
        "sh.law.matter.type", string="Type of Matter",
        tracking=True)
    discription_matter = fields.Text(
        string="Description of Matter",
        tracking=True)
    state = fields.Selection(
        selection=[
            ("draft", "Request for Approval"),
            ("approve", "Approved"),
            ("reject", "Reject"),
        ], string="Status",
        default="draft", readonly=True
    )

    # Create Partner
    def action_approve(self):
        vals = {
            "name": self.name,
            "street": self.street,
            "street2": self.street2,
            "city": self.city,
            "state_id": self.state_id.id,
            "zip": self.zip,
            "country_id": self.country_id.id,
            "phone": self.phone,
            "mobile": self.mobile,
            "email": self.email,
            "website": self.website,
        }
        partner_id = self.env["res.partner"].create(vals)
        self.write({"state": "approve", "related_partner_id": partner_id.id})
