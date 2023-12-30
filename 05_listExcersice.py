######### Exercises: Level 1

#  1. Declare an empty list
emptyList = []
print("Empty list :",emptyList)

# 2. Declare a list with more than 5 items
list = ['A', 1, True, 233.23, "Hello", "xyz"]
print(list)

# 3. Find the length of your list
print("Length of list :",len(list))

# 4. Get the first item, the middle item and the last item of the list
print("First element :",list[0])

middle=int(len(list)/2)
print("Middle element :",list[middle])

print("Last element :",list[-1])


# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Charmy",19,5.0,"unmarried","Junagadh"]
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using _print()_
print(it_companies)

# 8. Print the number of companies in the list
print("Number of companies :",len(it_companies))

# 9. Print the first, middle and last company
print("First company :",it_companies[0])
print("Middle company :",it_companies[int(len(list)/2)])
print("Last company :",it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[2] = "Boat"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("TCS")
print(it_companies)


# 12. Insert an IT company in the middle of the companies list
middle = int(len(it_companies)/2)
it_companies.insert(middle,"Infosys")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())

# 14. Join the it_companies with a string '#;&nbsp;'
joinit = '#;&nbsp; '.join(it_companies)
print(joinit)

# 15. Check if a certain company exists in the it_companies list.
print("Google" in it_companies) 

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
middle=int(len(it_companies)/2)
print(it_companies[middle])
print("---------")

# 21. Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22. Remove the middle IT company or companies from the list
middle=int(len(it_companies)/2)
it_companies.pop(middle)
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)



########## Exercises: Level 2


# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age
ages.sort()
print(ages)
minAge = min(ages)
maxAge = max(ages)
print("Min age :",minAge)
print("Max age :",maxAge)

# - Add the min age and the max age again to the list
ages.append(minAge)
ages.append(maxAge)
print(ages)

# - Find the median age (one middle item or two middle items divided by two)
mid = int(len(ages)/2)
print(ages[mid]/2)

# - Find the average age (sum of all items divided by their number )
avg = sum(ages)/len(ages)
print(avg)

# - Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(range)

# - Compare the value of (min - average) and (max - average), use _abs()_ method
min_avg=minAge-avg
max_avg=maxAge-avg
print(abs(min_avg))
print(abs(max_avg))

# Find the middle country(ies) in the [countries list]
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country=int(len(countries)/2)
print(countries[middle_country])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_part=(countries[:middle_country])
second_part=(countries[middle_country:])
print(first_part)
print(second_part)

#'China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries
scandic_countries=second_part
print(scandic_countries)