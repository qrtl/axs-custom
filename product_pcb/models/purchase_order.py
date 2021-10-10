# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    pcb_id = fields.Many2one("product.pcb", string="Pre-split PCB")
    pcb_qty = fields.Float("PCB Quantity")

    def action_add_pcb_components(self):
        line_obj = self.env["purchase.order.line"]
        if self.pcb_id:
            line_obj.create(
                {
                    "name": self.pcb_id.name,
                    "pcb_id": self.pcb_id.id,
                    "product_qty": 0.0,
                    "display_type": "line_section",
                    "order_id": self.id,
                }
            )
            for line in self.pcb_id.pcb_line_ids:
                line_obj.create(
                    {
                        "pcb_id": self.pcb_id.id,
                        "product_id": line.product_id.id,
                        "product_qty": self.pcb_qty,
                        "order_id": self.id,
                    }
                )
