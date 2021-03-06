# Generated by Django 2.2.16 on 2020-09-27 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tagged_from', to='core.Entry'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='name_parent',
            field=models.ForeignKey(blank=True, help_text="Use this parent's name as prefix when displayed out of context.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_using_name', to='core.Entry', verbose_name='Parent name prefix'),
        ),
    ]
