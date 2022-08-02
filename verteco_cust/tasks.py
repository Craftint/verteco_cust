import frappe

@frappe.whitelist()
def get_qty(item_code):
     return frappe.db.get_value("Bin", {"item_code": item_code}, ["reserved_qty", "actual_qty"])

