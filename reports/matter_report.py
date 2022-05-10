# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, api


class ShLawMatterReport(models.AbstractModel):
    _name = "report.sh_law_erp.sh_law_matter_report"
    _description = "Law Matter Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        return data
