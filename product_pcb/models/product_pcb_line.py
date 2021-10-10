# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductPcbLine(models.Model):
    _name = "product.pcb.line"
    _rec_name = "product_id"
    _description = "Product PCB Line"
    _order = "product_id"
    

    pcb_id = fields.Many2one("product.pcb", string="Pre-split PCB")
    product_id = fields.Many2one("product.product", string="Product", required=True)
    ratio = fields.Float()
