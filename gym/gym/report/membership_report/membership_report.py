# Copyright (c) 2025, Jeraldin PJ and contributors
# For license information, please see license.txt

import frappe
from frappe import utils

def execute(filters=None):
	data = []
	columns = [
    {"label": "Name", "fieldname": "name", "fieldtype": "Data", "width": 200},
    {"label": "Due Amount", "fieldname": "due_amount", "fieldtype": "Data", "width": 200},
    {"label": "Due Date", "fieldname": "due_date", "fieldtype": "Data", "width": 200},
	{"label": "Membership Type", "fieldname": "membership_type", "fieldtype": "Data", "width": 200},
	
]

	memberships = frappe.db.get_all("Active Memberships")	
	for membership in memberships:
		mem = frappe.get_doc("Active Memberships",membership)
		member = frappe.get_doc("Member",mem.member)
		membershiptype = frappe.get_doc("Membership Type", mem.membership_type)
		if str(mem.next_payment_date) == str(frappe.utils.today()):
			data.append({
				"name":member.full_name or " ",
				"due_amount":membershiptype.amount or " ",
				"due_date": mem.next_payment_date or " ",
				"membership_type":membershiptype.name or " ",

                })
	
	return columns, data
