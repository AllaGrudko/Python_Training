# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="sdfsf", lastname="werwre", address="fdgdg", home_phone="343",
                               mobile_phone="453", work_phone="345", fax="345", email="xcxcx", email2="xcvv",
                               email3="xcvv", homepage="dsfdsf"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", email2="", email3="", homepage=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

