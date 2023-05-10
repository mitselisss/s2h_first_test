from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class UserProfile(models.Model):

    class genderChoice(models.TextChoices):
        male = 'male'
        female = 'female'

    class palChoice(models.TextChoices):
        Sedentary = 'Sedentary'
        Low_active = 'Low active'
        Active = 'Active'
        Very_active = 'Very active'

    class cousineChoice(models.TextChoices):
        Morocco = 'Morocco'
        Turkey = 'Turkey'
        Spain = 'Spain'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=genderChoice.choices, default='male')
    yob = models.IntegerField(default=1994)
    age = models.IntegerField(null=True)
    height = models.FloatField()
    weight = models.FloatField()
    pal = models.CharField(max_length=50, choices=palChoice.choices)
    bmi = models.FloatField()
    bmr = models.FloatField()
    energy_intake = models.FloatField()
    halal = models.BooleanField()
    diary = models.BooleanField()
    eggs = models.BooleanField()
    fish = models.BooleanField()
    cousine = models.CharField(max_length=10, choices=cousineChoice.choices)

    def __str__(self):
        return str(self.user.username)
    
    def age_calculator(self):
        age = date.today().year-self.yob
        return age

    def bmi_calculator(self):
        bmi = self.weight/(self.height*self.height)
        return round(bmi, 2)

    def bmr_calculator(self):
        if self.gender == 'male':
            bmr = 88.362 + (13.397*self.weight) + (4.799*self.height*100) - (5.677*self.age)
        else:
            bmr = 447.593 + (9.247*self.weight) + (3.098*self.height*100) - (4.330*self.age)
        return round(bmr, 2)
 
    def energy_intake_calculator(self):
        #calculate PAL
        if self.pal == 'Sedentary':
            pal = 1.195
        elif self.pal == 'Low active':
            pal = 1.495
        elif self.pal == 'Active':
            pal = 1.745
        elif self.pal == 'Very active':   
            pal = 2.2
        #calculate Energy Intake
        if 18.5<=self.bmi<=24.99:
            energy_intake = self.bmr*pal
        elif self.bmi<18.5:
            energy_intake = self.bmr*pal + 500
        elif self.bmi>24.99:
            energy_intake = self.bmr*pal - 500
            
        return round(energy_intake, 2)
    
    
    def save(self, *args, **kwargs):
        
        self.age = self.age_calculator()
        self.bmi = self.bmi_calculator()
        self.bmr = self.bmr_calculator()
        self.energy_intake = self.energy_intake_calculator()
        
        super().save(*args, **kwargs)  

    
class Dish(models.Model):
    
    class typeChoice(models.TextChoices):
        First = 'First'
        Second = 'Second'
        Side = 'Side'
        Bread = 'Bread'
        Fruit = 'Fruit'
        Unique = 'Unique'
        Semi = 'Semi'
        Dessert = 'Dessert'
        Breakfast = 'Breakfast'
        Morning_snack = 'Morning snack'
        Afternoon_snack = 'Afternoon snack'

    id = models.IntegerField(primary_key=True)
    name_gr = models.CharField(max_length=500, null=True)
    name_en = models.CharField(max_length=500, null=True)
    ingredients_child_gr = models.CharField(max_length=500, null=True)
    ingredients_child_en = models.CharField(max_length=500, null=True)
    ingredients_adult_gr = models.CharField(max_length=500, null=True)
    ingredients_adult_en = models.CharField(max_length=500, null=True)
    recipe_gr = models.CharField(max_length=500, null=True)
    recipe_en = models.CharField(max_length=500, null=True)
    tip_gr = models.CharField(max_length=500, null=True)
    tip_en = models.CharField(max_length=500, null=True)
    kcal = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    protein = models.FloatField(null=True)
    carbohydrates = models.FloatField(null=True)
    type = models.CharField(max_length=20, choices=typeChoice.choices, null=True)
    autumn = models.BooleanField(null=True)
    winter = models.BooleanField(null=True)
    spring = models.BooleanField(null=True)
    summer = models.BooleanField(null=True)
    white_meat = models.BooleanField(null=True)
    red_meat = models.BooleanField(null=True)
    pork = models.BooleanField(null=True)
    fish = models.BooleanField(null=True)
    pulses = models.BooleanField(null=True)
    diary = models.BooleanField(null=True)
    eggs = models.BooleanField(null=True)
    pasta = models.BooleanField(null=True)
    rice = models.BooleanField(null=True)
    tubers = models.BooleanField(null=True)
    soups = models.BooleanField(null=True)
    cereals = models.BooleanField(null=True)
    fruit = models.BooleanField(null=True)
    nuts = models.BooleanField(null=True)
    raw_vegetables = models.BooleanField(null=True)
    cooked_vegetables = models.BooleanField(null=True)


    def __str__(self):
        return self.name_en


class Meal(models.Model):

    #class typeChoice(models.TextChoices):
    #    Breakfast = 'Breakfast'
    #    Morning_snack = 'Morning_snack'
    #    Lunch = 'Lunch'
    #    Afternoon_snack = 'Afternoon_snack'
    #    Dinner = 'Dinner'
    
    #class typeChoice2(models.TextChoices):
    #    Greece = 'Greece'
    #    Spain = 'Spain'
    #    Morocco = 'Moroco'
    #    Turkey = 'Turkey'

    id = models.IntegerField(primary_key=True)
    name_gr = models.CharField(max_length=500, null=True)
    name_en = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    autumn = models.BooleanField(null=True)
    winter = models.BooleanField(null=True)
    spring = models.BooleanField(null=True)
    summer = models.BooleanField(null=True)
    dish_1 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish1_menu_set', null=True)
    dish_2 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish2_menu_set', blank=True, null=True)
    dish_3 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish3_menu_set', blank=True, null=True)
    dish_4 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish4_menu_set', blank=True, null=True)
    dish_5 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish5_menu_set', blank=True, null=True)
    dish_6 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish6_menu_set', blank=True, null=True)
    dish_7 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish7_menu_set', blank=True, null=True)
    dish_8 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish8_menu_set', blank=True, null=True)
    dish_9 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish9_menu_set', blank=True, null=True)
    dish_10 = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish10_menu_set', blank=True, null=True)

    def __str__(self):
        return self.name_en

    #@property
    #def porsion(self):
    #    list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
    #            self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
    #    porsion = 0
    #    for l in list:
    #        if l is not None:
    #            porsion = porsion + l.porsion
    #    return porsion
        
    
    @property
    def kcal(self):
        list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
                self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
        kcal = 0
        for l in list:
            if l is not None:
                kcal = kcal + l.kcal
        return kcal
   
    @property
    def protein(self):
        list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
                self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
        protein = 0
        for l in list:
            if l is not None:
                protein = protein + l.protein
        return protein
        
    @property
    def fat(self):
        list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
                self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
        fat = 0
        for l in list:
            if l is not None:
                fat = fat + l.fat
        return fat
    
    @property
    def carbohydrates(self):
        list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
                self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
        carbohydrates = 0
        for l in list:
            if l is not None:
                carbohydrates = carbohydrates + l.carbohydrates
        return carbohydrates
    
    @property
    def fruit(self):
        list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
                self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
        fruit = 0
        for l in list:
            if l is not None:
                if l.fruit == True:
                    fruit = fruit + 1
        return fruit
    
    @property
    def raw_vegetables(self):
        list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
                self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
        raw_vegetables = 0
        for l in list:
            if l is not None:
                if l.raw_vegetables == True:
                    raw_vegetables = raw_vegetables + 1
        return raw_vegetables
    
    @property
    def cooked_vegetables(self):
        list = [self.dish_1, self.dish_2, self.dish_3, self.dish_4, self.dish_5, 
                self.dish_6, self.dish_7, self.dish_8, self.dish_9, self.dish_10]
        cooked_vegetables = 0
        for l in list:
            if l is not None:
                if l.cooked_vegetables == True:
                    cooked_vegetables = cooked_vegetables + 1
        return cooked_vegetables


#class Days(models.Model):
#    Mondey = models.ManyToManyField(Meal, related_name='Mondey_NP_set')
#    Tuesday = models.ManyToManyField(Meal, related_name='Tuesday_NP_set')
#    Wednesday = models.ManyToManyField(Meal, related_name='Wednesday_NP_set')
#    Thursday = models.ManyToManyField(Meal, related_name='Thursday_NP_set')
#    Friday = models.ManyToManyField(Meal, related_name='Friday_NP_set')
#    Saturday = models.ManyToManyField(Meal, related_name='Saturday_NP_set')
#    Sunday = models.ManyToManyField(Meal, related_name='Sunday_NP_set')
    
# class Calendar(models.Model):

#    class weekChoice(models.TextChoices):
#        Previous = 'Previous'
#        Current = 'Current'
#        Next = 'Next'
    
#    class dayChoice(models.TextChoices):
#        Mondey = 'Mondey'
#        Tuesday = 'Tuesday'
#        Wednesday = 'Wednesday'
#        Thursday = 'Thursday'
#        Friday = 'Friday'
#        Saturday = 'Saturday'
#        Sunday = 'Sunday'

#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    week = models.CharField(max_length=20, choices=weekChoice.choices)
#    day = models.CharField(max_length=20, choices=dayChoice.choices)
#    meal_1 = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal1_Cal_set')
#    meal_2 = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal2_Cal_set')
#    meal_3 = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal3_Cal_set')
#    meal_4 = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal4_Cal_set')
#    meal_5 = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal5_Cal_set')

