# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="aaa4aaa")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
