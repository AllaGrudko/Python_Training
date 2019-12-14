# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="aaa4aaa"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.edit_first_group(Group(header="b66bbbbbb"))

def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test"))
    app.group.edit_first_group(Group(footer=";okiokpkopko"))
