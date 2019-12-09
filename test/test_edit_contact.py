# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="kkkk"))
    app.session.logout()

def test_edit_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(lastname="aaaaaa"))
    app.session.logout()

def test_edit_first_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(address="ccccc"))
    app.session.logout()
