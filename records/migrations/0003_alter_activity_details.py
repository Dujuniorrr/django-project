# Generated by Django 4.1.7 on 2023-02-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0002_alter_activity_details_alter_activity_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="details",
            field=models.CharField(
                blank=True, default="", max_length=100, verbose_name="Detalhes"
            ),
            preserve_default=False,
        ),
    ]
