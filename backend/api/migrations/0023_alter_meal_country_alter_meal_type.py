# Generated by Django 4.1.7 on 2023-04-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_dish_autumn_dish_carbohydrates_dish_cereals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
