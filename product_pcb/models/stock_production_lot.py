# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    pcb_id = fields.Many2one("product.pcb", string="Pre-split PCB", compute="_compute_pcb_id", store=True)

    @api.depends("name")
    def _compute_pcb_id(self):
        for lot in self:
            stock_moves = self.env["stock.move.line"].search(
                [("lot_id", "=", lot.id)]
            ).mapped("move_id")
            stock_moves = stock_moves.filtered(
                lambda move: move.picking_id.location_id.usage == "supplier"
            )
            purchase_order = stock_moves.mapped("purchase_line_id.order_id")[:1]
            if purchase_order:
                lot.pcb_id = purchase_order.pcb_id
