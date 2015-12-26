from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Coupon",
					"description": _("All Coupon"),
				},
			]
		},
		{
			"label": _("Tools"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Adjust Point Value",
					"description": _("Adjust Point Value"),
				},
				{
					"type": "doctype",
					"name": "Cash Coupon Tool",
					"description": _("Create coupons in bulk"),
				},
			]
		},
	]
