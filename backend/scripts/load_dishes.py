import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from api.models import Dish

def run():
    #df = pd.read_csv("Meals.csv")
    df = pd.read_csv('C:/Users/kyrikalp/Desktop/S2Hcodes/S2H_integration_v01/backend/scripts/Dishes.csv')

    for index, row in df.iterrows():
        #print(index, row)
        dish_id = row['Id']

        try:
            dish = Dish.objects.get(id=dish_id)
        except ObjectDoesNotExist:
            dish = Dish(id=dish_id)
            
            dish.id = row['Id']
            dish.name_gr = row['Name (in Greek)']
            dish.name_en = row['Name (in English)']
            dish.ingredients_child_gr = row['Ingredients for child (in Greek)']
            dish.ingredients_child_en = row['Ingredients for child (in English)']
            dish.ingredients_adult_gr = row['Ingredients for adult (in Greek)']
            dish.ingredients_adult_en = row['Ingredients for adult (in English)']
            dish.recipe_gr = row['Recipe (in Greek)']
            dish.recipe_en = row['Recipe (in English)']
            dish.tip_gr = row['Tip (in Greek)']
            dish.tip_en = row['Tip (in English)']
            dish.kcal = row['Kcal']
            dish.protein = row['Protein']
            dish.fat = row['Fat']
            dish.carbohydrates = row['Carbohydrates']
            dish.type = row['Dish type']
            dish.autumn = row['For Autumn']
            dish.winter = row['For Winter']
            dish.spring= row['For Spring']
            dish.summer = row['For Summer']
            dish.white_meat = row['White meat']
            dish.red_meat = row['Red meat']
            dish.pork = row['Pork']
            dish.fish = row['Fish or seafood']
            dish.pulses = row['Pulses']
            dish.diary = row['Dairy']
            dish.eggs = row['Eggs']
            dish.pasta = row['Pasta']
            dish.rice = row['Rice']
            dish.tubers = row['Tubers']
            dish.soups = row['Soups']
            dish.cereals = row['Cereals']
            dish.fruit = row['Fruit']
            dish.nuts = row['Nuts']
            dish.raw_vegetables = row['Raw vegetables']
            dish.cooked_vegetables = row['Cooked vegetables']
            dish.save()