# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="kkkk", lastname="aaaaaa", address="ccccc", home_phone="ccccccc",
                                mobile_phone="ddddddd", work_phone="gggggg", fax="1111", email="sssss", email2="hhhhh",
                                email3="tttttt", homepage=",,"))
    app.session.logout()
