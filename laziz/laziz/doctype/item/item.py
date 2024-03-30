# Copyright (c) 2024, beshoy atef and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe.model.naming import getseries

class Item(Document):
	# def autoname(self):
	# 	# select a project name based on customer

	# 	#frappe.throw("Auto name method ")
	# 	#prefix = f'P-{self.item_name}-'
	# 	#frappe.throw(prefix)
	# 	self.name =  f'P-{self.item_name}- 1' #getseries(prefix, 3)
	def validate(self) :
		pass
		#frappe.throw("Validate Method")