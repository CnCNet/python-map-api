# Generated by Django 4.2.11 on 2024-08-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kirovy", "0007_jpg_png"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cncfileextension",
            name="extension_type",
            field=models.CharField(
                choices=[("map", "map"), ("assets", "assets"), ("image", "image")],
                max_length=32,
            ),
        ),
    ]