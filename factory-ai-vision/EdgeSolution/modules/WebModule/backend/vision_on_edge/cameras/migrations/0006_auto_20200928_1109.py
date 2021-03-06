# Generated by Django 3.0.8 on 2020-09-28 11:09

from django.db import migrations, models
import vision_on_edge.cameras.constants


class Migration(migrations.Migration):

    dependencies = [
        ("cameras", "0005_auto_20200922_0641"),
    ]

    operations = [
        migrations.AlterField(
            model_name="camera",
            name="danger_zones",
            field=models.CharField(
                blank=True,
                default=vision_on_edge.cameras.constants.gen_default_zones,
                max_length=1000,
            ),
        ),
        migrations.AlterField(
            model_name="camera",
            name="lines",
            field=models.CharField(
                blank=True,
                default=vision_on_edge.cameras.constants.gen_default_lines,
                max_length=1000,
            ),
        ),
    ]
