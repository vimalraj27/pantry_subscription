// Copyright (c) 2021, Vimalraj R and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pantry Customer', {
    refresh: function(frm) {
        frm.add_custom_button('Go To Subscriptions', () => {
            frappe.new_doc('Pantry Subscription', {
                pantry_customer : frm.doc.name
            })
        })
    }
});
