from .models import *
from .serializers import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
import itertools
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
 

@api_view(['POST'])
def Login(request):
    if request.method == "POST":
        data = request.data
        username = data["username"]
        password = data["password"]

        try: 
            user = User.objects.get(username=username)
            if user and check_password(password, user.password):
                serializer = UserSerializer(instance=user, data=request.data)
                if serializer.is_valid():
                    return Response(serializer.data)
            else:
                return JsonResponse({'error': 'Wrong password for this username.'}, status=400)
        except:
            return JsonResponse({'error': 'Username does not exist. You must sign up first'}, status=400)
    

@api_view(['POST'])
def Register(request):
    
    if request.method == 'POST':
        data = request.data
        username = data["username"]
        password = data["password"]
        password2 = data["password2"]

        try:
            user = User.objects.get(username=username)
            return JsonResponse({'error': "Username already exist."}, status=400)     
        except:
            try:
                validate_password(password)
                validate_password(password2)
                if password == password2:
                    data['password'] = make_password(data['password'])
                    #data['password2'] = make_password(data['password2']) 
                    serializer = UserSerializer(data=data)
                    #userProfile = UserProfile(user=user, gender='male', yob='1994', height='1.88', weight='85', pal='Active', halal=False, diary=False, eggs=False, fish=False, cousine='Spain')
                    if serializer.is_valid():
                        serializer.save()
                        user = User.objects.get(username=username)
                        profile = UserProfile(user = user, gender='male', yob=1994, height=1.88, weight=85, pal='Active', halal=False, diary=False, eggs=False, fish=False, cousine='Spain', age=29, bmi=1, bmr=1, energy_intake=1)
                        profile.save()
                        return Response(serializer.data)
                else:
                    return JsonResponse({'error': "Passowrd1 and password2 are not the same."}, status=400)
            except:
                return JsonResponse({'error': "Invalid password"}, status=400)

    
@api_view(['GET'])
def Users(request):
    
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def UsersProfile(request):
    
    if request.method == 'GET':
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT'])
def IdUserProfile(request, pk):
    
    if request.method == 'GET':
        user = UserProfile.objects.get(user = pk)
        serializer = UserProfileSerializer(instance=user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        user = User.objects.get(id = pk)
        userProfile = UserProfile.objects.get(user = user)
        serializer = UpdateUserProfileSerializer(instance=userProfile, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        user = User.objects.get(id = pk)
        data = request.data

        serializer = RegisterUserProfileSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    

@api_view(['GET'])
def NPs(request, pk):

    user =  UserProfile.objects.get(user=pk)
    energy_intake = user.energy_intake
    meals = Meal.objects.all() 

    AWARD_VALUE_ESSENTIAL = 0.001
    AWARD_VALUE = 0.1
    PENALTY_VALUE = 100.0
    CALORIC_LIMIT_MIN = 200.0
    CALORIC_LIMIT_MAX = 500.0
    CALORIC_PENALTY_MIN = 100.0
    CALORIC_PENALTY_MAX = 1000000.0
    NAP_EXCLUSION_VALUE = 10000000.0
    fat_t1 = energy_intake*0.25
    fat_t2 = energy_intake*0.35
    

    allergy_filters = {
    'pork': user.halal,
    'dairy': user.diary,
    'eggs': user.eggs,
    'fish': user.fish,
    }

    for allergy, is_filtered in allergy_filters.items():
        if is_filtered:
            for i in range(1, 6):
                meals = meals.exclude(**{f'dish_{i}__{allergy}': True})
    

    all_list = [meals.filter(type=meal_type) for meal_type in ('Breakfast', 'Morning Snack', 'Lunch', 'Afternoon Snack', 'Dinner')]

    # combination of all possible NPs
    res = list(itertools.product(*all_list))

    sum_kcal = []
    sum_fat = []
    sum_frandveg = []
    dishes_div = []
    # sum kcal,fat and (fruit and vegetables) for each NP
    for i in range(len(res)):
        kcal = 0
        fat = 0
        fruit = 0
        r_vegetables = 0
        c_vegetables = 0
        frandveg = 0
        dishes_list = []
        # iterate through each one of the five meals for a specific NP
        for j in range(0,5):
            kcal += res[i][j].kcal
            fat += res[i][j].fat * 9
            fruit += res[i][j].fruit 
            r_vegetables += res[i][j].raw_vegetables 
            c_vegetables += res[i][j].cooked_vegetables
            if res[i][j].dish_1 is not None:
                dishes_list.append(res[i][j].dish_1)
            if res[i][j].dish_2 is not None:
                dishes_list.append(res[i][j].dish_2)
            if res[i][j].dish_3 is not None:
                dishes_list.append(res[i][j].dish_3)
            if res[i][j].dish_4 is not None:
                dishes_list.append(res[i][j].dish_4)
            if res[i][j].dish_5 is not None:
                dishes_list.append(res[i][j].dish_5)
            
        frandveg = fruit + r_vegetables + c_vegetables
        sum_kcal.append(kcal)
        sum_fat.append(fat)
        sum_frandveg.append(frandveg)
        # check if all dishes in each one of the NPs are unique
        result = len(set(dishes_list)) == len(dishes_list)
        dishes_div.append(result)

    print("#######")
    print(sum_kcal[:14])
    print(sum_fat[:14])
    print(sum_frandveg[:14])
    print(dishes_div[:14])
    print("#######")
    caloric_distance = [0] * len(res)
    fat_distance = [0] * len(res)
    frandveg_distance = [0] * len(res)
    dishes_distance = [0] * len(res)
    for i in range(len(res)):

        # how good is that NP regarding calories
        caloric_distance[i] = abs(sum_kcal[i] - energy_intake)
        if (caloric_distance[i] == 0.0):
            caloric_distance[i] = AWARD_VALUE_ESSENTIAL
        else:
            if caloric_distance[i] > CALORIC_LIMIT_MIN:
                if caloric_distance[i] > CALORIC_LIMIT_MAX:
                    caloric_distance[i] *= CALORIC_PENALTY_MAX
                else:
                    caloric_distance[i] *= CALORIC_PENALTY_MIN
        

        # how good is the NP regarding fats
        fat_distance[i]=1.0
        if sum_fat[i] >= fat_t1 and sum_fat[i] <= fat_t2:
            fat_distance[i] = AWARD_VALUE
        else:
            fat_distance[i] = PENALTY_VALUE

        # fow good is the NP regarding fruits and vegetables
        if sum_frandveg[i] < 5 or sum_frandveg[i] > 10:
            frandveg_distance[i] = PENALTY_VALUE
        else:
            frandveg_distance[i] = AWARD_VALUE

        # how good is the NP regarding dishes diversity
        if dishes_div[i] == True:
            dishes_distance[i] = AWARD_VALUE
        else:
            dishes_distance[i] = NAP_EXCLUSION_VALUE

    print("energy intake of the user: " + str(energy_intake))
    print("caloric distance")
    print(caloric_distance[:14])
    print("fat distance")
    print(fat_distance[:14])
    print("fruits and vegetables distance")
    print(frandveg_distance[:14])
    print("dishes distance")
    print(dishes_distance[:14])
    print("#######")

    appropriateness_distance = [1] * len(res)
    for i in range(len(res)):
        appropriateness_distance[i] *= caloric_distance[i]
        appropriateness_distance[i] *= fat_distance[i]
        appropriateness_distance[i] *= frandveg_distance[i]
        appropriateness_distance[i] *= dishes_distance[i]
        
    
    print("appropriateness distance")
    print(appropriateness_distance[:7])

    # Sort appropriateness_distance
    appropriateness_distance_list = sorted(appropriateness_distance)
    print("########")
    print("sorted appropriateness distance")
    print(appropriateness_distance_list[:7])

    # Create a list of tuples with sum and corresponding combination of meals
    sum_combinations = list(zip(appropriateness_distance, res))
    print(sum_combinations[:7])

    # Sort the list of tuples based on the sums
    sorted_sum_combinations = sorted(sum_combinations, key=lambda x: x[0])
    print(sorted_sum_combinations[:7])

    # Extract the sorted combinations of meals
    sorted_res = [combination for (sum, combination) in sorted_sum_combinations]
    print(sorted_res[:7])

    # Diversity step 1!!!
    meals_id = []
    meals_id.append(sorted_res[0][0].id)
    meals_id.append(sorted_res[0][1].id)
    meals_id.append(sorted_res[0][2].id)
    meals_id.append(sorted_res[0][3].id)
    meals_id.append(sorted_res[0][4].id)
    unique_meals = []
    unique_meals.append(sorted_res[0])
    for i in range(1,len(sorted_res)):
        cnt = 0
        for j in range(5):
            x = meals_id.count(sorted_res[i][j].id)
            if (sorted_res[i][j].id not in meals_id) or (x<3):
                cnt += 1
        if cnt == 5:
            meals_id.append(sorted_res[i][0].id)
            meals_id.append(sorted_res[i][1].id)
            meals_id.append(sorted_res[i][2].id)
            meals_id.append(sorted_res[i][3].id)
            meals_id.append(sorted_res[i][4].id)
            unique_meals.append(sorted_res[i])
            
    
    print("######################")
    print("######################")
    print(meals_id)
    print(meals_id.count(66))
    #print(cnt_meals)
    print(unique_meals)


    # Diversity step 2!!!
    list1 = []
    list1.append(meals_id[:5])
    final_meals = []
    final_meals.append(unique_meals[0])

    for j in range(5, len(meals_id), 5):
        #print("#########################################")
        list2 = meals_id[j:j+5]
        set2 = set(list2)
        cnt = 0
        for i in range(0, len(list1)):
            set1 = set(list1[i])
            #print(list1)
            #print(list2)
            similarity = len(set1.intersection(set2)) / len(set1.union(set2))
            #print(similarity)
            if similarity < 0.4:
                cnt += 1
        if cnt == len(list1):
            list1.append(list2)
            final_meals.append(unique_meals[int(j/5)])
    print("###########################")
    print(list1)
    print("########################")
    print("########################")
    print(final_meals)

    

    f_mse = []
    f_sum_kcal = []
    f_sum_fat = []
    f_sum_frandveg = []
    # sum kcal,fat and (fruit and vegetables) for each of the final NPs
    for i in range(len(final_meals)):
        kcal = 0
        fat = 0
        fruit = 0
        r_vegetables = 0
        c_vegetables = 0
        frandveg = 0
        # iterate through each one of the five meals for a specific NP
        for j in range(0,5):
            kcal += final_meals[i][j].kcal
            fat += final_meals[i][j].fat * 9
            fruit += final_meals[i][j].fruit 
            r_vegetables += final_meals[i][j].raw_vegetables 
            c_vegetables += final_meals[i][j].cooked_vegetables
            
        frandveg = fruit + r_vegetables + c_vegetables
        f_mse.append(abs(kcal - energy_intake))
        f_sum_kcal.append(kcal)
        f_sum_fat.append(fat)
        f_sum_frandveg.append(frandveg)

    print("########################")
    print("########################")
    print(f_sum_kcal)
    print(f_mse)
    print(f_sum_fat)
    print(f_sum_frandveg)

    f_caloric_distance = [0] * len(res)
    f_fat_distance = [0] * len(res)
    f_frandveg_distance = [0] * len(res)
    
    for i in range(len(final_meals)):

        # how good is that NP regarding calories
        f_caloric_distance[i] = abs(f_sum_kcal[i] - energy_intake)
        if (f_caloric_distance[i] == 0.0):
            f_caloric_distance[i] = AWARD_VALUE_ESSENTIAL
        else:
            if f_caloric_distance[i] > CALORIC_LIMIT_MIN:
                if f_caloric_distance[i] > CALORIC_LIMIT_MAX:
                    f_caloric_distance[i] *= CALORIC_PENALTY_MAX
                else:
                    f_caloric_distance[i] *= CALORIC_PENALTY_MIN
        

        # how good is the NP regarding fats
        f_fat_distance[i]=1.0
        if f_sum_fat[i] >= fat_t1 and f_sum_fat[i] <= fat_t2:
            f_fat_distance[i] = AWARD_VALUE
        else:
            f_fat_distance[i] = PENALTY_VALUE

        # fow good is the NP regarding fruits and vegetables
        if f_sum_frandveg[i] < 5 or f_sum_frandveg[i] > 10:
            f_frandveg_distance[i] = PENALTY_VALUE
        else:
            f_frandveg_distance[i] = AWARD_VALUE


    print("energy intake of the user: " + str(energy_intake))
    print("caloric distance")
    print(f_caloric_distance[:8])
    print("fat distance")
    print(f_fat_distance[:8])
    print("fruits and vegetables distance")
    print(f_frandveg_distance[:8])

    f_appropriateness_distance = [1] * len(final_meals)
    for i in range(len(final_meals)):
        f_appropriateness_distance[i] *= f_caloric_distance[i]
        f_appropriateness_distance[i] *= f_fat_distance[i]
        f_appropriateness_distance[i] *= f_frandveg_distance[i]


    print("appropriateness distance")
    print(f_appropriateness_distance)

    # Sort appropriateness_distance in descending order
    f_appropriateness_distance_list = sorted(f_appropriateness_distance)
    print("########")
    print("sorted appropriateness distance")
    print(f_appropriateness_distance_list)

    # Create a list of tuples with sum and corresponding combination of meals
    f_sum_combinations = list(zip(f_appropriateness_distance, final_meals))
    print(f_sum_combinations)

    # Sort the list of tuples based on the sums 
    f_sorted_sum_combinations = sorted(f_sum_combinations, key=lambda x: x[0])
    print(f_sorted_sum_combinations)

    # Extract the sorted combinations of meals
    f_sorted_res = [f_combination for (f_sum, f_combination) in f_sorted_sum_combinations]
    print(f_sorted_res)


    n = 0
    n1 = 0
    n2 = 0
    for s in sum_kcal:
        if s>=2500 and s<3000:
            n += 1
        if s>=2000 and s<2500:
            n1 += 1
        if s<2000:
            n2 += 1    
   

    res2 = res[7:14]
    # print(res2)
    # print("######")
    # print(sorted_res[:14])
    #top_7_sorted_res = sorted_res[50:57]
    # print(top_7_sorted_res[0][0].kcal)
    
    serialized_res = []
    for item in final_meals:
        serialized_item = [] 
        for meal in item:
            serializer = MealSerializer(meal)
            serialized_meal = serializer.data
            serialized_item.append(serialized_meal)
        serialized_res.append(serialized_item)

    return Response(serialized_res)

@api_view(['GET'])
def MealsApi(request):
    user =  UserProfile.objects.get(user_id=3)
    meals = Meal.objects.all()

    if user.halal == True:
        
        meals = meals.exclude(dish_1__pork = True)
        meals = meals.exclude(dish_2__pork = True)
        meals = meals.exclude(dish_3__pork = True)
        meals = meals.exclude(dish_4__pork = True)
        meals = meals.exclude(dish_5__pork = True)

    if user.diary == True:
        
        meals = meals.exclude(dish_1__dairy = True)
        meals = meals.exclude(dish_2__dairy = True)
        meals = meals.exclude(dish_3__dairy = True)
        meals = meals.exclude(dish_4__dairy = True)
        meals = meals.exclude(dish_5__dairy = True)

    if user.eggs == True:
        
        meals = meals.exclude(dish_1__eggs = True)
        meals = meals.exclude(dish_2__eggs = True)
        meals = meals.exclude(dish_3__eggs = True)
        meals = meals.exclude(dish_4__eggs = True)
        meals = meals.exclude(dish_5__eggs = True)

    if user.fish == True:
        
        meals = meals.exclude(dish_1__fish = True)
        meals = meals.exclude(dish_2__fish = True)
        meals = meals.exclude(dish_3__fish = True)
        meals = meals.exclude(dish_4__fish = True)
        meals = meals.exclude(dish_5__fish = True)

    breakfast = meals.filter(type='Breakfast')
    morning_snack = meals.filter(type='Morning_snack')
    lunch = meals.filter(type='Lunch')
    afternoon_snack = meals.filter(type='Afternoon_snack')
    dinner = meals.filter(type='Dinner')


    all_list = []
    all_list.append(breakfast)
    all_list.append(morning_snack)
    all_list.append(lunch)
    all_list.append(afternoon_snack)
    all_list.append(dinner)

    # combination of all possible NPs
    res = list(itertools.product(*all_list))

    #res = list([[i, j, k] for i in breakfast
    #             for j in morning_snack
    #             for k in lunch])
    res2 = list([])
    sorted_res = list([])
    sum_list = []
    rows, cols = (len(res), 5)
    x = list([[None for i in range(cols)] for j in range(rows)])
    json_sorted_res = []

    for i in range(len(res)):
        new_list = [] 
        for j in range(0,5): 
            if res[i][j].description not in new_list: 
                new_list.append(res[i][j].description)
        if len(new_list)==5:
            res2.append(res[i]) 

    for i in range(len(res2)):
        #sum = 0
        sum_kcal = 0
        #sum_protein = 0
        #sum_fat = 0
        #sum_carbs = 0
        for j in range(0,5):
            sum_kcal = sum_kcal + res2[i][j].kcal
            #sum_protein = sum_protein + res[i][j].protein
            #sum_fat = sum_fat + res[i][j].fat
            #sum_carbs = sum_carbs + res[i][j].carbohydrates
        #sum = sum_kcal + sum_protein + sum_fat + sum_carbs
        sum_list.append(sum_kcal)
    
    for i in range(0,len(sum_list)):
        max = 0
        for s in range(len(sum_list)):
            if sum_list[s]>max:
                max = sum_list[s]
                s_max = s
        sorted_res.append(res2[s_max])
        sum_list[s_max] = 0


    for i in range(len(res2)):
        for j in range(0,5):
            x[i][j] = meals.filter(description = sorted_res[i][j], type = sorted_res[i][j].type).values()
        
        #for j in range(0,2):
            #x[i][j] = dishes.filter(description = sorted_res[i][j]).values()
            #x[i][j] = serializers.serialize("json", dishes.filter(description = sorted_res[i][j]))
            #x[i][j] = dishes.filter(description = sorted_res[i][j]).values()
        #for j in range(2,3):
            #x[i][j] = dishes.filter(description = sorted_res[i][j]).values()
            #x[i][j] = serializers.serialize("json", menus.filter(description = sorted_res[i][j]))
            #x[i][j] = menus.filter(description = sorted_res[i][j]).values()


    return Response(x)
