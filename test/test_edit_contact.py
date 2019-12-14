# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname="kkkk"))

def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    app.contact.edit_first_contact(Contact(lastname="aaaaaa"))

def test_edit_first_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="test"))
    app.contact.edit_first_contact(Contact(address="ccccc"))
