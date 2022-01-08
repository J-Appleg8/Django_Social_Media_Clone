from django.contrib import admin
from .models import Group, GroupMember


class GroupMemberInLine(admin.TabularInline):
    models = GroupMember


admin.site.register(Group)
