# Generated by Django 4.0.3 on 2022-03-14 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_mgmt', '0012_rename_assigner_issue_manager'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['dateUpdated', 'dateAdded']},
        ),
    ]
