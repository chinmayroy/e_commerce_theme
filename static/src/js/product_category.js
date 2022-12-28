// /** @odoo-module **/
//
// import publicWidget from 'web.public.widget';
//
// publicWidget.registry.cycategorys = publicWidget.Widget.extend({
//     selector: '.product_category',
//     start() {
//         let categoryRow = this.el.querySelector('#explore_new_product_category')
//
//         if (categoryRow){
//             this._rpc({
//                 route: '/explore_product_category/',
//                 params:{}
//             }).then(data=>{
//                 let html = ``
//                 data.forEach(category=>{
//                     category.category_name = undefined;
//                     html += `<div class="col-lg-3 mb-5">
//                         <div class="d-flex align-items-center">
//                             <div class="img-container mr-3 rounded">
//                                 <img class="category-image rounded" src="data:image/png;base64,${category.image}" alt="Category Image"/>
//                             </div>
//                             <div>
//                                 <h5 class="mb-0">${ category.category_name ? category.category_name : ''}</h5>
//                                 <div>${category.description ? category.description : ''}</div>
//                             </div>
//                         </div>
//                     </div>`
//                 })
//                 categoryRow.innerHTML = html
//             })
//         }
//     },
// });
//
// export default publicWidget.registry.cycategorys;
