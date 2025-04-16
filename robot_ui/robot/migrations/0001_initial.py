# Generated by Django 5.2 on 2025-04-16 01:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Position",
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
                ("angle0", models.IntegerField()),
                ("angle1", models.IntegerField()),
                ("angle2", models.IntegerField()),
                ("angle3", models.IntegerField()),
                ("angle4", models.IntegerField()),
                ("angle5", models.IntegerField()),
            ],
        ),
    ]
