# Generated by Django 5.2 on 2025-04-17 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("robot", "0004_alter_robot_angle0_alter_robot_angle1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="angle0",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="angle1",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="angle2",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="angle3",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="angle4",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="angle5",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                ]
            ),
        ),
    ]
