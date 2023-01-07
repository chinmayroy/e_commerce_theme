/** @odoo-module **/

import options from 'web_editor.snippets.options';

options.registry.ExploreNewProductsView = options.Class.extend({
    start() {
        let new_productRow = this.$target.find('#explore_new_products')

        if (new_productRow) {
            this._rpc({
                route: '/explore_new_products_template/',
                params: {}
            }).then(data => {
                let html = ``
                data.forEach(new_product => {
                    html += `<div class="col-md-3 mb-5">
                        <div class="align-items-left new_product_view">
                        <a href="/shop/${((new_product.name ? new_product.name : '').replace(/ /gm,'-')).toLowerCase()}-${new_product.id ? new_product.id : ''}" class="bg-primary">
                            <div class="img-container mr-3 new_product_img">
                                <img class="product-img-container" src="data:image/png;base64,${new_product.image_1920}" alt="New Product Image"/>
                            </div>
                            <div class="new_product_title">
                                <h5>${new_product.name ? new_product.name : ''}</h5>
                            </div>
                            </a>
                            <div class="new_product_price">
                                <h6>Price ${new_product.list_price ? new_product.list_price : ''} USD</h6>
                            </div>
                        </div>
                    </div>`
                })
                new_productRow.html(html)
            })
        }
    },
})
