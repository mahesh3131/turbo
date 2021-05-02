# Generated by Django 2.2.4 on 2021-05-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turbo_app', '0005_delete_deliv_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='deliv_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=30, unique=True)),
                ('sender_email_id', models.EmailField(max_length=254, unique=True)),
                ('sender_phone_no', models.IntegerField()),
                ('sen_d_no', models.IntegerField()),
                ('sen_city', models.CharField(max_length=30, unique=True)),
                ('sen_state', models.CharField(max_length=30, unique=True)),
                ('sen_district', models.CharField(max_length=30, unique=True)),
                ('sen_pincode', models.IntegerField()),
                ('sen_land_mark', models.CharField(max_length=30, unique=True)),
                ('rec_name', models.CharField(max_length=30, unique=True)),
                ('rec_email_id', models.CharField(max_length=30, unique=True)),
                ('rec_phone_no', models.IntegerField()),
                ('rec_d_no', models.IntegerField()),
                ('rec_city', models.CharField(max_length=30, unique=True)),
                ('rec_state', models.CharField(max_length=30, unique=True)),
                ('rec_district', models.CharField(max_length=30, unique=True)),
                ('rec_pincode', models.IntegerField()),
                ('rec_land_mark', models.CharField(max_length=30, unique=True)),
                ('about_product', models.CharField(max_length=30, unique=True)),
                ('p_waight', models.CharField(max_length=30, unique=True)),
                ('pickup_time', models.CharField(max_length=30, unique=True)),
                ('auction_time', models.CharField(max_length=30, unique=True)),
                ('deliv_method', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
