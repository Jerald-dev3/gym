# Copyright (c) 2025, Jeraldin PJ and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Member(Document):
	def before_save(self):
		frappe.throw("Working")
		print("hello world")
		if self.first_name and self.last_name:
			self.full_name = self.first_name +" "+ self.last_name
		else:
			self.full_name = self.first_name
		if len(self.aadhaar_number) != 12:
			frappe.throw("Entered Aadhaar number is incorrect.")
		self.joining_date = frappe.utils.today()

