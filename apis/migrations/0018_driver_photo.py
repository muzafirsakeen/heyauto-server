# Generated by Django 4.1.2 on 2023-02-20 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0017_remove_driver_detail_d_photo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="driver_photo",
            fields=[
                ("photo_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "d_photo",
                    models.ImageField(
                        blank=True,
                        default="images/None/No0img.jpg",
                        max_length=255,
                        null=True,
                        upload_to="driversphoto",
                    ),
                ),
                (
                    "driver_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apis.driver_detail",
                    ),
                ),
            ],
        ),
    ]
