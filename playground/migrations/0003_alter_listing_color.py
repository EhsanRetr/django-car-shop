# Generated by Django 4.2.7 on 2023-12-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playground", "0002_listing_brand_listing_color_listing_discription_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="color",
            field=models.CharField(max_length=24),
        ),
    ]