# Generated by Django 3.1.2 on 2020-11-01 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupMembers',
            new_name='GroupMember',
        ),
        migrations.RemoveField(
            model_name='group',
            name='member',
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='groups.GroupMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
