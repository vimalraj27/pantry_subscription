// Copyright (c) 2021, Vimalraj R and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pantry Items', {

    food_accomodation_taken_amount : function(frm)
	{
        frm.set_value("total_amount", frm.doc.total_rent + frm.doc.food_accomodation_taken_amount);
    },
    total_rent : function(frm)
	{
        frm.set_value("total_amount", frm.doc.total_rent + frm.doc.food_accomodation_taken_amount);
    }

});
