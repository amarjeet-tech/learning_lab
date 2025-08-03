print("-------Working with Lists---------")
fruits = ["Apple", "Banana", "Milk", "Tea"]
print(f"Original list of fruits: {fruits}")



# @ what : Adding a new item to the end of the list.
fruits.append("Orange")
print(f"After appending Orange: {fruits}")


#@what: Accessing an item by its index... python indexs start from 0..
#@why: to get a specific item, we use its position. fruits[0] is the first item.

first_fruit = fruits[0]
print(f"The frist fruit is: {first_fruit}")


#@what: Looping through each item in the list
#@why: this is how we perform an action on every single item in our collection.
print("Looping through all fruits:")
for fruit in fruits:
    print(f"-{fruit}")
print("\n "+ "="*20 + "\n") #just a separator

#----------------Dictionaries-------------------
print("-------Working with Dictionaries---------")

#@what: Creating a dictionary to store key-value pairs.
employee = {
    "name": "Alice",
    "age": 30,
    "department": "Development",
    "skills": ["Python", "JavaScript", "SQL"],
    "is_active": True,
    "projects": {
        "current": "Project Booking System",
        "previous": ["Project Scraper", "Project OTag"]
    }
}

print(f"Original employee dictionary: {employee}")

#@what: Accessing a value by its key.

print(f"Employee's name and department is: {employee['name'], employee['department']}")

# adding a new key value pair to the dictionary
employee["salary"] = 60000
print(f"After adding salary: {employee}")

#@what: Looping through each key-value pair in the dictionary
print("Looping through employee details:")
for key, value in employee.items():
    print(f"{key}: {value}")