# Generated by Django 2.2.16 on 2020-09-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200927_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='aka',
            field=models.CharField(blank=True, max_length=256, verbose_name='a.k.a'),
        ),
    ]