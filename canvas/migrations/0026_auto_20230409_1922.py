# Generated by Django 3.0.14 on 2023-04-10 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("canvas", "0025_eventset"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eventset",
            old_name="tokens_worth",
            new_name="tokens",
        ),
    ]
