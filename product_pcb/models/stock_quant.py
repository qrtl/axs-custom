# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    pcb_id = fields.Many2one(related="lot_id.pcb_id", string="Pre-split PCB", store=True)
    pcb_qty = fields.Float(compute="_compute_pcb_qty", string="PCB Quantity", store=True)

    @api.depends("pcb_id", "quantity")
    def _compute_pcb_qty(self):
        for quant in self:
            if not quant.pcb_id:
                continue
            pcb_line = self.env["product.pcb.line"].search(
                [
                    ("pcb_id", "=", quant.pcb_id.id),
                    ("product_id", "=", quant.product_id.id),
                ]
            )[:1]
            if pcb_line:
                quant.pcb_qty = quant.quantity * pcb_line.ratio / 100
