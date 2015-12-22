from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, nowdate, now_datetime
from frappe import msgprint, _
from frappe.utils import flt, getdate, nowdate
from datetime import date

class AdjustPointValue(Document):
	def get_details(self):
		dl = frappe.db.sql("""select name,transaction_date,grand_total_point_value,claim_status,customer from `tabSales Order` where customer=%s and docstatus=1 and claim_status NOT IN ('Claimed','Expired'); """,(self.customer),as_dict=1, debug=1)

		self.set('adjust_point_value_detail', [])

		for d in dl:
			nl = self.append('adjust_point_value_detail', {})
			nl.sales_order = d.name
			nl.sales_order_date = d.transaction_date
			nl.grand_total_point_value = d.grand_total_point_value
			nl.claim_status = d.claim_status
			nl.customer = d.customer

	def update_point_value(self):
		sales_order_list = []
		for d in self.get('adjust_point_value_detail'):
			if d.claim_status=='Claimed' or d.claim_status=='Expired':
				frappe.db.sql("""update `tabSales Order` set claim_status = %s,modified = %s where name=%s and docstatus=1""", (d.claim_status, now_datetime(), d.sales_order))
				sales_order_list.append(d.sales_order)
				customer_doc=frappe.get_doc("Customer", d.customer)
				customer_doc.total_point_collected = customer_doc.total_point_collected-d.grand_total_point_value
				customer_doc.save()


		if sales_order_list:
			msgprint("Claim Status updated in: {0}".format(", ".join(sales_order_list)))