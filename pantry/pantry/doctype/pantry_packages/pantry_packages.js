// Copyright (c) 2021, Vimalraj R and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pantry Subscription', {
    refresh: function(frm) {
        frm.add_custom_button('Create a Custom Package', () => {
            frappe.new_doc('Pantry Packages', {
                pantry_subscription : frm.doc.name
            })
        })
    }
});
