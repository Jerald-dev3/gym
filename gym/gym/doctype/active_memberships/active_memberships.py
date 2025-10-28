# Copyright (c) 2025, Jeraldin PJ and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import add_to_date
from frappe.model.document import Document


class ActiveMemberships(Document):
	def before_save(self):
		membership_type = frappe.get_doc("Membership Type", self.membership_type)
		self.next_payment_date = add_to_date(self.last_payment, days=membership_type.days,as_string=True)
