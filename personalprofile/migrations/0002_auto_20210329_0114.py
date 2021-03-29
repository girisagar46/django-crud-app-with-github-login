# Generated by Django 3.1.7 on 2021-03-29 01:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("personalprofile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalprofile",
            name="phone_no",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None, unique=True
            ),
        ),
    ]
