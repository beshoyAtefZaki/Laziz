# Copyright (c) 2024, beshoy atef and contributors
# For license information, please see license.txt

import frappe

from frappe import throw , _ 
from frappe.model.document import Document

class ItemPrice(Document):
	def validate(self) :
		self.validate_uom()


	def validate_uom(self) :
		if self.uom not in frappe.get_doc("Item" , self.item).uom_list() :
			throw(_("Not allowed"))
