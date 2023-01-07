{
    'name': 'E-Commerce Theme',
    'description': 'E-Commerce website theme',
    'author': "Chinmay Roy",
    'website': "https://www.chinmayroy.com",
    'category': 'Theme',
    'sequence': 10,
    'version': '15.0.1',
    'depends': ['sale_product_configurator', 'website_sale_comparison', 'website_sale_wishlist',
                'website_sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',

        # All Snippets
        'views/snippets/snippets.xml',
        'views/snippets/explore_product_category.xml',
        'views/snippets/explore_new_products_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'e_commerce_theme/static/src/scss/styles.scss',
            'e_commerce_theme/static/src/scss/product_category.scss',
            'e_commerce_theme/static/src/js/explore_product_category.js',
            'e_commerce_theme/static/src/js/explore_new_products_view.js',
            'e_commerce_theme/static/src/js/jquery.js',
        ],
        'web._assets_primary_variables': [
            "e_commerce_theme/static/src/scss/primary_variables.scss",
        ]
    },
    'images': [
    ],
    'snippet_lists': {
    },
    'auto_install': False,
    'application': False,
    'price': 0,
    'currency': 'USD',
    'license': 'LGPL-3',
    'contributors': [
        'Chinmay Roy <https://github.com/chinmayroy>',
    ],
}
