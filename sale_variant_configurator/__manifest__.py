# Copyright 2014-2016 Oihane Crucelaegui - AvanzOSC
# Copyright 2015-2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2017 David Vidal <david.vidal@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Sale - Product variants",
    "summary": "Product variants in sale management",
    "version": "11.0.1.2.0",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "product_variant_configurator",
    ],
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Tecnativa,"
              "Odoo Community Association (OCA)",
    "category": "Sales Management",
    "website": "https://github.com/OCA/product-variant",
    "data": [
        "views/sale_view.xml",
    ],
    "installable": True,
    "post_init_hook": "assign_product_template",
}
