# Generated by Django 3.2.5 on 2021-08-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cnab_handler", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="recipient_cpf",
            field=models.BigIntegerField(help_text="CPF do beneficiário"),
        ),
    ]
