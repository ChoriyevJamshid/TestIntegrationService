# Generated by Django 4.2.7 on 2024-05-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("phone", models.CharField(blank=True, max_length=20)),
                ("image_url", models.URLField(blank=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
