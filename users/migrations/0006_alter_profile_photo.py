# Generated by Django 4.2.7 on 2023-12-26 17:21

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_profile_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=models.ImageField(
                null=True, upload_to=users.utils.user_directory_path
            ),
        ),
    ]
