import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from api.models import Meal, Dish

def run():
    #df = pd.read_csv("Meals.csv")
    df = pd.read_csv('C:/Users/kyrikalp/Desktop/S2Hcodes/S2H_integration_v01/backend/scripts/Meals.csv')

    for index, row in df.iterrows():
        #print(index, row)
        meal_id = row['Id']
        try:
            meal = Meal.objects.get(id=meal_id)
        except ObjectDoesNotExist:
            meal = Meal(id=meal_id)

        meal.id = row['Id']
        meal.name_gr = row['Name (in Greek)']
        meal.name_en = row['Name (in English)']
        meal.type = row['Type']
        meal.country = row["Country"]
        meal.autumn = row["For Autumn"]
        meal.winter = row["For Winter"]
        meal.spring = row["For Spring"]
        meal.summer = row["For Summer"]
        if pd.isna(row["Dish ID #1"]) is False:
            dish_1 = Dish.objects.get(id = row["Dish ID #1"])
            meal.dish_1 = Dish.objects.get(id = dish_1.id)
        if pd.isna(row["Dish ID #2"]) is False:
            dish_2 = Dish.objects.get(id = row["Dish ID #2"])
            meal.dish_2 = Dish.objects.get(id = dish_2.id)
        if pd.isna(row["Dish ID #3"]) is False:
            dish_3 = Dish.objects.get(id = row["Dish ID #3"])
            meal.dish_3 = Dish.objects.get(id = dish_3.id)
        if pd.isna(row["Dish ID #4"]) is False:
            dish_4 = Dish.objects.get(id = row["Dish ID #4"])
            meal.dish_4 = Dish.objects.get(id = dish_4.id)
        if pd.isna(row["Dish ID #5"]) is False:
            dish_5 = Dish.objects.get(id = row["Dish ID #5"])
            meal.dish_5 = Dish.objects.get(id = dish_5.id)

        #meal.dish_6 = Dish.objects.get(id = row["Dish ID #6"])
        #meal.dish_7 = Dish.objects.get(id = row["Dish ID #7"])
        #meal.dish_8 = Dish.objects.get(id = row["Dish ID #8"])
        #meal.dish_9 = Dish.objects.get(id = row["Dish ID #9"])
        #meal.dish_10 = Dish.objects.get(id = row["Dish ID #10"])
        meal.save()