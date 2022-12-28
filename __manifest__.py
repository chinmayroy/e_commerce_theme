{
    'name': 'E-Commerce Theme',
    'description': 'E-Commerce website theme',
    'author': "Chinmay Roy",
    'website': "https://www.chinmayroy.com",
    'category': 'Theme',
    'sequence': 10,
    'version': '15.0.1',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/product_category_view.xml',
        'views/menus.xml',
        'views/product_category_view.xml',

        # All Snippets
        'views/snippets/new_products.xml',
        'views/snippets/product_mega_menu.xml',
        'views/snippets/snippets.xml',
        'views/snippets/explore_product_category.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'e_commerce_theme/static/src/scss/styles.scss',
            'e_commerce_theme/static/src/scss/product_category.scss',
            # 'e_commerce_theme/static/src/js/product_category.js',
            'e_commerce_theme/static/src/js/explore_product_category.js',
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
