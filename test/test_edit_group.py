# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="aaa4aaa"))

def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="b66bbbbbb"))

def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer=";okiokpkopko"))
