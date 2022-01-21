{
    'name': 'Construction - Purchase Management',
    'version': '14.0.1.0.11',
    'author': 'Pragmatic TechSoft Pvt Ltd.',
    'website': "www.pragtech.co.in",
    'category': 'Construction',
    'description': """
Construction (V15)
Odoo version - V15
    """,
    'depends': ['base', 'pragtech_ppc', 'purchase', 'purchase_stock'],
    'data': [
        'wizard/stage_transaction_wizard.xml',
        'security/pragtech_purchase_security.xml',
        'security/ir.model.access.csv',
        'wizard/purchase_requisition_wizard.xml',
        'views/account_invoice_view.xml',
        'views/purchase_requisition.xml',
        'views/partner_view.xml',
        'views/purchase_view.xml',
        'views/vendor_quotation.xml',
        'views/quotation_comparison_view.xml',
        'views/purchase_transaction.xml',
        'views/purchase_advance_view.xml',
        'views/purchase_debit_recovery_view.xml',
        'views/stock_view.xml',
        'views/sequence_view.xml',
        'views/purchase_consumption.xml',
        'views/shipment_scheduler.xml',
        'report/purchase_order_summary.xml',
        'report/purchase_order_bill_summary.xml',
        'report/short_supply.xml',
        'report/unbilled_grn.xml',
        'report/report.xml',
        'wizard/procurement_view.xml',
        'wizard/purchase_order_summary.xml',
        'wizard/purchase_bill_summary.xml',
        'wizard/short_supply.xml',
        'wizard/unbilled_grn.xml',
        'wizard/consumtion_report_view.xml',
        'wizard/purchase_material_consumption.xml'
    ],
    'images': ['images/construction-purchase.png'],

    'license': 'OPL-1',
    'price': 199,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
}
