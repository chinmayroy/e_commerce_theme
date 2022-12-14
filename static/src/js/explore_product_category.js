/** @odoo-module **/

import options from 'web_editor.snippets.options';

options.registry.ExploreCategoryOptions = options.Class.extend({
    start() {
        let categoryRow = this.$target.find('#explore_new_product_category')

        if (categoryRow) {
            this._rpc({
                route: '/explore_product_category/',
                params: {}
            }).then(data => {
                let html = ``
                data.forEach(category => {
                    html += `<div class="col-lg-2 mb-5">
                        <div class="align-items-left">
                        <a href="/shop/category/${(category.name ? category.name : '').toLowerCase()}-${category.id ? category.id : ''}" class="bg-primary">
                            <div class="img-container mr-3 rounded category_view">
                                <img class="category-image" src="data:image/png;base64,${category.image_1920}" alt="Category Image"/>
                            </div>
                            <div class="category-title">
                                <h5>${category.name ? category.name : ''}</h5>
                            </div>
                            </a>
                        </div>
                    </div>`
                })
                categoryRow.html(html)
            })
        }
    },
})
