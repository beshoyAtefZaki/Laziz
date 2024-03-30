# Copyright (c) 2024, beshoy atef and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe.model.naming import getseries

class Item(Document):

	def validate(self) :
		pass
	def get_item_size(self) :
		sizes = [i.size for i in self.item_size]
		return sizes 


	def uom_list(self):
		uom_li = [i.uom for i in self.item_uom]
		return uom_li 



@frappe.whitelist()
def validate_uom_self(item , uom , *args , **kwargs) :

	"""
	item : string item name 
	uom : string uom name 
	
	"""
	obj = frappe.get_doc("Item" , item) 
	if uom in obj.uom_list() :
		return True 
	else :
		 return False


@frappe.whitelist()
def get_item_uom_list(doctype, txt, searchfield, start, page_len, filters) :
	reponse = []
	if not filters :
		frappe.throw("filters Missing")
	print(filters.get("item"))
	if not filters.get("item") :
		frappe.throw("Item required ")

	item =  frappe.get_doc("Item" , filters.get("item") ) 
	data = item.uom_list()

	reponse = ((i,) for i in data)
	accepted_data = frappe.db.sql(f""" SELECT uom FROM `tabItem UOM` WHERE parent = '{filters.get("item")}' """)
	#reponse.append(data)
	print(accepted_data)
	return reponse
	# return []
	

