# Generated by Django 3.2.8 on 2021-10-24 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimSum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField()),
                ('description', models.TextField()),
                ('normal_price', models.TextField()),
            ],
        ),
    ]