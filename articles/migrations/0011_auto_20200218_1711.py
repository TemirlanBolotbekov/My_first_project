# Generated by Django 2.2.8 on 2020-02-18 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20200212_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='dislikes',
            new_name='dislike',
        ),
    ]
