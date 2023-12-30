# 1. Create an empty dictionary called dog
empty_dictionary = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name':'Daisy',
    'color':'White',
    'breed':'German Shepherd',
    'legs':'four',
    'age':3
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Charmy',
    'last_name':'Rudani',
    'gender':'Female',
    'age':18,
    'maritial_status':'unmarried',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'India',
    'city':'Junagadh',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills')) 

# 6. Modify the skills values by adding one or two skills
student['skills'].append('Express')
student['skills'].append('Java')
print(student.get('skills')) 

# 7. Get the dictionary keys as a list
print(student.keys())

# 8. Get the dictionary values as a list
print(student.values())

# 9. Change the dictionary to a list of tuples using _items()_ method
list = list(student.items())
print(list)

# 10. Delete one of the items in the dictionary
student.pop('maritial_status')
print(student)

# 11. Delete one of the dictionaries
del dog