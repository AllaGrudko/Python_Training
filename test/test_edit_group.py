# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="aaa4ahgfhd999rsdrtsrdtaa", header="hello")
    app.group.edit_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.name = new_group_data.name
    group.header = new_group_data.header
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header="b66bbbbbb"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

#def test_edit_first_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(footer="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(footer=";okiokpkopko"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
