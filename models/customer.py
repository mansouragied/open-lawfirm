# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    matter_count = fields.Integer("Matter", compute="_compute_compute_matter_count")
    client_count = fields.Integer(
        "Client Request", compute="_compute_compute_client_count")
    evidence_count = fields.Integer(
        "Evidence", compute="_compute_compute_evidence_count")
    trial_count = fields.Integer("Trial", compute="_compute_compute_trial_count")

    def _compute_compute_matter_count(self):
        if self:
            for rec in self:
                matters = self.env["sh.law.matter"].search(
                    [("client_id", "=", rec.id)])
                if matters:
                    rec.matter_count = len(matters.ids)
                else:
                    rec.matter_count = 0

    def matter_btn(self):
        return{
            "name": "Matter",
            "type": "ir.actions.act_window",
            "res_model": "sh.law.matter",
            "view_mode": "tree,form",
            "domain": [("client_id", "=", self.id)],
            "target": "current",
        }

    def _compute_compute_client_count(self):
        if self:
            for rec in self:
                clients = self.env["sh.law.client.request"].search(
                    [("related_partner_id", "=", rec.id)])
                if clients:
                    rec.client_count = len(clients.ids)
                else:
                    rec.client_count = 0

    def client_btn(self):
        return{
            "name": "Client Request",
            "type": "ir.actions.act_window",
            "res_model": "sh.law.client.request",
            "view_mode": "tree,form",
            "domain": [("related_partner_id", "=", self.id)],
            "target": "current",
        }

    def _compute_compute_evidence_count(self):
        if self:
            for rec in self:
                evidences = self.env["sh.law.erp.evidence"].search(
                    [("client", "=", rec.id)])
                if evidences:
                    rec.evidence_count = len(evidences.ids)
                else:
                    rec.evidence_count = 0

    def evidence_btn(self):
        return{
            "name": "Evidence",
            "type": "ir.actions.act_window",
            "res_model": "sh.law.erp.evidence",
            "view_mode": "tree,form",
            "domain": [("client", "=", self.id)],
            "target": "current",
        }

    def _compute_compute_trial_count(self):
        if self:
            for rec in self:
                trials = self.env["sh.law.erp.trial"].search(
                    [("partner_id", "=", rec.id)])
                if trials:
                    rec.trial_count = len(trials.ids)
                else:
                    rec.trial_count = 0

    def trial_btn(self):
        return{
            "name": "Trial",
            "type": "ir.actions.act_window",
            "res_model": "sh.law.erp.trial",
            "view_mode": "tree,form",
            "domain": [("partner_id", "=", self.id)],
            "target": "current",
        }
