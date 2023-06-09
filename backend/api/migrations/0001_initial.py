# Generated by Django 4.1.7 on 2023-03-08 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Side', 'Side'), ('Bread', 'Bread'), ('Fruit', 'Fruit'), ('Unique', 'Unique'), ('Semi', 'Semi'), ('Dessert', 'Dessert'), ('Breakfast', 'Breakfast'), ('Morning snack', 'Morning Snack'), ('Afternoon snack', 'Afternoon Snack')], max_length=20)),
                ('marocco', models.BooleanField(null=True)),
                ('spain', models.BooleanField(null=True)),
                ('turkey', models.BooleanField(null=True)),
                ('porsion', models.FloatField()),
                ('kcal', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('white_meat', models.BooleanField()),
                ('red_meat', models.BooleanField()),
                ('pork', models.BooleanField()),
                ('fish', models.BooleanField()),
                ('dairy', models.BooleanField()),
                ('eggs', models.BooleanField()),
                ('fruit', models.BooleanField(null=True)),
                ('raw_vegetables', models.BooleanField(null=True)),
                ('cooced_vegetables', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('yob', models.DateField()),
                ('age', models.IntegerField(null=True)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('pal', models.CharField(choices=[('Sedentary', 'Sedentary'), ('Low active', 'Low Active'), ('Active', 'Active'), ('Very active', 'Very Active')], max_length=50)),
                ('bmi', models.FloatField()),
                ('bmr', models.FloatField()),
                ('energy_intake', models.FloatField()),
                ('halal', models.BooleanField()),
                ('diary', models.BooleanField()),
                ('eggs', models.BooleanField()),
                ('fish', models.BooleanField()),
                ('cousine', models.CharField(choices=[('Morocco', 'Morocco'), ('Turkey', 'Turkey'), ('Spain', 'Spain')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Morning_snack', 'Morning Snack'), ('Lunch', 'Lunch'), ('Afternoon_snack', 'Afternoon Snack'), ('Dinner', 'Dinner')], max_length=20)),
                ('morocco', models.BooleanField(null=True)),
                ('spain', models.BooleanField(null=True)),
                ('turkey', models.BooleanField(null=True)),
                ('dish_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish1_menu_set', to='api.dish')),
                ('dish_10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish10_menu_set', to='api.dish')),
                ('dish_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish2_menu_set', to='api.dish')),
                ('dish_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish3_menu_set', to='api.dish')),
                ('dish_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish4_menu_set', to='api.dish')),
                ('dish_5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish5_menu_set', to='api.dish')),
                ('dish_6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish6_menu_set', to='api.dish')),
                ('dish_7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish7_menu_set', to='api.dish')),
                ('dish_8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish8_menu_set', to='api.dish')),
                ('dish_9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dish9_menu_set', to='api.dish')),
            ],
        ),
    ]
