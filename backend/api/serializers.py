from rest_framework import serializers
from api.models import Dish, Meal, UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dish
        fields='__all__'

class MealSerializer(serializers.ModelSerializer):
    dish_1 = DishSerializer()
    dish_2 = DishSerializer()
    dish_3 = DishSerializer()
    dish_4 = DishSerializer()
    dish_5 = DishSerializer()
    dish_6 = DishSerializer()
    dish_7 = DishSerializer()
    dish_8 = DishSerializer()
    dish_9 = DishSerializer()
    dish_10 = DishSerializer()
    class Meta:
        model = Meal
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'

class RegisterUserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ('user', 'gender', 'height', 'weight', 'yob', 'pal', 'halal', 'diary', 'eggs', 'fish')

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('gender', 'height', 'weight', 'yob', 'pal', 'halal', 'diary', 'eggs', 'fish')

