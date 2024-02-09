# A) String Operations:
#     - Reverse a string, replace string with other string, merge two strings
#     - Find character is in string or not without using loops
#     - Split string into multiple words &characters

original_string = "charmy"
reversed_string = original_string[::-1]
replaced_string = original_string.replace("c", "C")

string1 = "Charmy"
string2 = "Rudani"
merged_string = string1 + " " + string2

print("Original String:", original_string)
print("Reversed String:", reversed_string)
print("After Replacement:", replaced_string)
print("Merged String:", merged_string)

is_present = "b" in original_string
print(is_present)

print("Split string into Words:", original_string.split())
print("Split string into Characters:", list(original_string))




# B) Dictionaries Operations:
#   - Apply “Update, Delete, clear, popitem, pop, get, keys and values” operation in dictionary.

dictionary = {
    "firstName": "Charmy", 
    "lastName": "Rudani",
    "age":18,
    "state":"Gujarat",
    "country": "India"
    }

dictionary.update({"age": 19})
del dictionary["state"]
print(dictionary)

print("Removed item using popitem:", dictionary.popitem())
print("Removed age using pop:", dictionary.pop("age"))

keys_list = dictionary.keys()
values_list = dictionary.values()

print("get operation:", dictionary.get("firstName", "Name not found"))
print("Keys in the dictionary:", list(keys_list))
print("Values in the dictionary:", list(values_list))

dictionary.clear()
print("clear Dictionary:",dictionary)




#   - Create 3 dictionaries and merge them into 1 dictionary

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

merged_dict = {**dict1, **dict2, **dict3}
print("Merged Dictionary:", merged_dict)
