# Generated by Django 3.2.9 on 2022-03-01 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220301_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='discription',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='schools',
            new_name='topic',
        ),
    ]