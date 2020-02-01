# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact_data = Contact(firstname="kkkk", lastname="test", address="uuuuuu")
    new_contact_data.id = contact.id
    index = None
    for cont in range(len(old_contacts)):
        id = app.contact.find_user_id_by_index(cont)
        if id == new_contact_data.id:
            index = cont
    app.contact.edit_contact_by_index(index, new_contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.firstname = new_contact_data.firstname
    contact.lastname = new_contact_data.lastname
    contact.address = new_contact_data.address
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_edit_first_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.edit_first_contact(Contact(lastname="aaaaaa"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

#def test_edit_first_contact_address(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(address="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.edit_first_contact(Contact(address="ccccc"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)