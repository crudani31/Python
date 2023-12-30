### Exercises: Level 1

# 1. Create an empty tuple
emptyTuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Khush','Mitansh')
sisters = ('Shivani','Swara')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers+sisters
print(siblings)

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_member
father = 'Ashvinbhai'
mother = 'Rinaben'
family_members = siblings + (father, mother)
print(family_members)

####### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]  
father, mother = family_members[-2:]  
print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)

# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple','Guava','Strawberry')
vegetables = ('Tomato','Carrot','Chilli')
animals = ('Dog','Cow','Panda')
food_stuff_tp = fruits+vegetables+animals
print(food_stuff_tp)

# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = food_stuff_tp

# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = int(len(food_stuff_tp)/2)
print (food_stuff_lt[middle:])


# 1. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[-4:-1])

# 1. Delete the food_staff_tp tuple completely
del food_stuff_lt

# 1. Check if an item exists in  tuple:
# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) 
print('Iceland' in nordic_countries)
