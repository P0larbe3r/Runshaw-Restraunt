# Generated by Django 4.2.16 on 2025-02-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestrauntApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.CharField(choices=[('Main', 'MAIN'), ('Starter', 'STARTER'), ('Dessert', 'DESSERT'), ('Drink', 'DRINK')], default='MAIN', max_length=7),
        ),
    ]
