# Generated by Django 4.2.7 on 2023-12-26 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_location_state_location_zip_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.location",
            ),
        ),
    ]
