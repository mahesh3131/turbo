# Generated by Django 2.2.4 on 2021-05-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0016_deliv_form_achived_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliv_form',
            name='achived_by',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
