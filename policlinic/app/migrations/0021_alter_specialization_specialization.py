# Generated by Django 5.1.3 on 2024-11-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0020_remove_user_confirmed_policy_confirmed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="specialization",
            name="specialization",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Специализация"
            ),
        ),
    ]
