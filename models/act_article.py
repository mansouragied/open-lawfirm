# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models
from odoo.tools.translate import html_translate


class ShLawErpActArticle(models.Model):
    _name = "sh.law.erp.act.article"
    _description = "Law Erp Act Article"
    _order = "id desc"
    _rec_name = "act_article_name"

    act_article_name = fields.Char("Act/Article Name", required=True)
    act_article_no = fields.Char("Act/Article No.", required=True)
    act_article_description = fields.Html("Description", translate=html_translate)
    act_article_type = fields.Many2one("sh.law.matter.type", string="Type")
