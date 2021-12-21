# Copyright (c) 2021, Vimalraj R and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe.website.website_generator import WebsiteGenerator

class PantrySubscription(WebsiteGenerator):
    # check before submitting this document
    def before_save(self):
        exists = frappe.db.exists(
            "Pantry Subscription",
            {
                "pantry_customer": self.pantry_customer,
                # check for submitted documents
                "docstatus": 1,
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active Subscription for this Customer")

        subscription_period = frappe.db.get_single_value("Pantry Settings", "subscription_period")
        self.to_date = frappe.utils.add_days(self.from_date, (subscription_period or 30) * self.subscription_months)
        self.price=self.package_cost*self.subscription_months
    