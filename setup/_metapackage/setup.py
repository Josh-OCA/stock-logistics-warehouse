import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-stock-logistics-warehouse",
    description="Meta package for oca-stock-logistics-warehouse Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-stock_free_quantity',
        'odoo14-addon-stock_inventory_include_exhausted',
        'odoo14-addon-stock_move_location',
        'odoo14-addon-stock_packaging_calculator',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)