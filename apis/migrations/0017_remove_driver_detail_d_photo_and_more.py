# Generated by Django 4.1.2 on 2023-02-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0016_rename_fname_users_name_remove_users_lname"),
    ]

    operations = [
        migrations.RemoveField(model_name="driver_detail", name="d_photo",),
        migrations.AlterField(
            model_name="driver_detail",
            name="d_password",
            field=models.CharField(max_length=200),
        ),
    ]