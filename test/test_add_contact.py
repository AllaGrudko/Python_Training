# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="sdfsf", lastname="werwre", address="fdgdg", home_phone="343",
                               mobile_phone="453", work_phone="345", fax="345", email="xcxcx", email2="xcvv",
                               email3="xcvv", homepage="dsfdsf"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", email2="", email3="", homepage=""))
    app.session.logout()

