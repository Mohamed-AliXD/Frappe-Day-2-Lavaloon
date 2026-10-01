# Copyright (c) 2026, mohamedali456@gmail.com and contributors
# For license information, please see license.txt

# import frappe

import random
import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def before_insert(self):
        self.seat = f"{random.randint(1, 99)}{random.choice('ABCDE')}"

    def validate(self):
        self.remove_duplicate_add_ons()
        self.calculate_total()

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("You can only submit a ticket when its status is Boarded.")

    def remove_duplicate_add_ons(self):
        seen, unique = set(), []
        for row in self.add_ons:
            if row.item not in seen:
                seen.add(row.item)
                unique.append(row)
        self.set("add_ons", unique)
        for i, row in enumerate(self.add_ons, start=1):
            row.idx = i

    def calculate_total(self):
        self.total_amount = (self.flight_price or 0) + sum(
            (row.amount or 0) for row in self.add_ons
        )
