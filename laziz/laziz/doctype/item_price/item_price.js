// Copyright (c) 2024, beshoy atef and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Price', {
	refresh: function(frm) {
		// frm.events.setup_item_qyery(frm)
		console.log("refresh")
	},

	setup_item_qyery:function(frm) {
		frm.set_query('item', () => {
			return {
				filters: {
					has_size:  1 
				}
			}
		})
	},
	setup_uom_query(frm) {
		console.log("Setup query ")
		frm.set_query('uom', () => {
			return {
				query: 'laziz.laziz.doctype.item.item.get_item_uom_list',
				filters: {
					"item": frm.doc.item
				}
			}
		})
	},
	item:function(frm) {
		frm.doc.uom =""
		frm.refresh_field("uom")
		frm.events.setup_uom_query(frm)
	},
	uom:function(cur_frm){
		console.log(cur_frm.doc.uom)
		if (! cur_frm.doc.item) {
			cur_frm.doc.uom =""
			cur_frm.refresh_field("uom")
			throw("Can not proccess")

		}
		if (cur_frm.doc.uom ){
		frappe.call({

			"method" :"laziz.laziz.doctype.item.item.validate_uom_self" ,
			"args" :{
				"item" : cur_frm.doc.item ,
				"uom" : cur_frm.doc.uom 
			}, callback: function(r ){
					if (r.message ==false ){
						cur_frm.doc.uom =""
						cur_frm.refresh_field("uom")
						frappe.throw("Error")
					}
					console.log(r.message)
			}
		})
	} 
}
});
