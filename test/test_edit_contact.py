# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="kkkk"))

def test_edit_first_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="aaaaaa"))

def test_edit_first_contact_address(app):
    app.contact.edit_first_contact(Contact(address="ccccc"))
