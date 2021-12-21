# Copyright (c) 2021, Vimalraj R and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class PantryPackages(WebsiteGenerator):
	def before_save(self):
		total_fcprice=0
		for row in self.items_fetch:
			total_fcprice+=row.fcprice
		self.package_price=total_fcprice