
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, nowdate, now_datetime
from frappe import msgprint, _
from frappe.utils import flt, getdate, nowdate
from datetime import date

class CashCouponTool(Document):
	def create_coupons(self):
		for i in range(self.number_of_coupons):
			doc_coupon = frappe.new_doc("Coupon")
			doc_coupon.naming_series = self.naming_series
			doc_coupon.customer = self.customer
			doc_coupon.coupon_code = self.coupon_code
			doc_coupon.coupon_value = self.coupon_value
			doc_coupon.date_of_issue = self.date_of_issue
			doc_coupon.date_of_expiry = self.date_of_expiry
			doc_coupon.coupon_description = self.coupon_description
			doc_coupon.save()
			coupon_link = "<a href='desk#Form/Coupon/"+doc_coupon.name+"'>"+doc_coupon.name+" </a>"
			frappe.msgprint(coupon_link+" created")