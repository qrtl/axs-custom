# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductPcb(models.Model):
    _name = "product.pcb"
    _description = "Product PCB"

    name = fields.Char(required=True)
    pcb_line_ids = fields.One2many("product.pcb.line", "pcb_id", string="PCB Lines")
    active = fields.Boolean(default=True)
