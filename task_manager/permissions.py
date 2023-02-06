from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get(app_label='task_manager', model='Task')
permission = Permission.objects.create(
    codename='can_masscreate_tag',
    name='Can mass create Tag',
    content_type=content_type
)