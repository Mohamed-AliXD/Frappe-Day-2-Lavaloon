# Copyright (c) 2026, mohamedali456@gmail.com and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.db_set("status", "Completed")
