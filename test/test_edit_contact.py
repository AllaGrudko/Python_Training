# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="kkkk"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(lastname="aaaaaa"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_first_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(address="ccccc"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)