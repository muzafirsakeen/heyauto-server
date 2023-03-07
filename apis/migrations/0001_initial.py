# Generated by Django 4.1.2 on 2022-10-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="user_details",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("fname", models.CharField(max_length=50)),
                ("lname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("age", models.CharField(max_length=5)),
                ("gender", models.CharField(max_length=10)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
