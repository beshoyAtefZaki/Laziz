# Copyright (c) 2024, beshoy atef and contributors
# For license information, please see license.txt

import frappe

from frappe import throw , _ 
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class ItemPrice(Document):
	def validate(self) :
		self.validate_uom()


	def validate_uom(self) :
		if self.uom not in frappe.get_doc("Item" , self.item).uom_list() :
			throw(_("Not allowed"))


	def get_page_info(self):
			"""
			Return page information for ItemPrice.
			Modify this method to include additional fields as needed.
			"""
			return {
				"item": self.item,
				"uom": self.uom,
				"from_date": self.from_date,
				"to_date": self.to_date,
				"has_size": self.has_size,
				"size": self.size,
				"price": self.price,
				"status": self.status,
				"route": self.route,
				# Add other relevant fields
			}