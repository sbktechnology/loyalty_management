
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
			# doc_coupon.customer = self.customer
			doc_coupon.coupon_code = self.coupon_code
			doc_coupon.is_bulk = self.is_bulk
			doc_coupon.coupon_value = self.coupon_value
			doc_coupon.date_of_issue = self.date_of_issue
			doc_coupon.company = self.company
			doc_coupon.cost_center = self.cost_center
			doc_coupon.date_of_expiry = self.date_of_expiry
			doc_coupon.coupon_description = self.coupon_description
			doc_coupon.submit()
			coupon_link = "<a href='desk#Form/Coupon/"+doc_coupon.name+"'>"+doc_coupon.name+" </a>"
			frappe.msgprint(coupon_link+" created")
		self.create_jv()

	def create_jv(self):
		total_credit = self.number_of_coupons*self.coupon_value
		# cost_center = frappe.db.get_value("Company", ref_doc.company, "cost_center")
		if self.date_of_issue and self.company:
			company_abbr = frappe.db.get_value("Company", self.company, "abbr")
			doc_jv_creation=frappe.new_doc("Journal Entry")
			# doc_jv_creation.standards = r.get("standard")
			doc_jv_creation.posting_date=self.date_of_issue
			doc_jv_creation.append("accounts", {
			"account": "Cash Coupon Owe - "+company_abbr,
			"cost_center": self.cost_center,
			"credit_in_account_currency": total_credit,
			})
			doc_jv_creation.append("accounts", {
			"account": "Cash Coupon - "+company_abbr,
			"cost_center": self.cost_center,
			"debit_in_account_currency": total_credit,
			})
			doc_jv_creation.save()
			doc_jv_creation.user_remark=self.coupon_code+" - Bulk"
			doc_jv_creation.submit()
			frappe.msgprint(doc_jv_creation.name+" is Submited")