# bookshelf/signals.py
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Book

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'bookshelf':
        # Create groups
        admins, _ = Group.objects.get_or_create(name='Admins')
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')

        # Assign permissions
        perms = Permission.objects.filter(codename__in=['can_view', 'can_create', 'can_edit', 'can_delete'])
        admins.permissions.set(perms)

        editor_perms = Permission.objects.filter(codename__in=['can_create', 'can_edit'])
        editors.permissions.set(editor_perms)

        viewer_perms = Permission.objects.filter(codename='can_view')
        viewers.permissions.set(viewer_perms)
