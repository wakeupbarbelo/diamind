# Generated by Django 2.2.16 on 2020-10-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_entryparentthroughmodel_next_auto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entryparentthroughmodel',
            old_name='next_auto',
            new_name='slide_auto',
        ),
        migrations.AddField(
            model_name='entryparentthroughmodel',
            name='slide_title',
            field=models.BooleanField(default=False),
        ),
    ]
