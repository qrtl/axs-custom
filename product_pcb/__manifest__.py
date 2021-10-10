# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product PCB",
    "version": "14.0.1.0.0",
    "author": "Quartile Limited",
    "category": "Product",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": ["purchase_stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_pcb_views.xml",
        "views/purchase_order_views.xml",
        "views/stock_production_lot_views.xml",
        "views/stock_quant_views.xml",
    ],
}
