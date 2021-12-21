# Copyright (c) 2021, Vimalraj R and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PantryItems(Document):
	def before_save(self):
		self.item_total_price=(self.item_price*(self.item_tax/100))+self.item_price