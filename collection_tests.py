
dict_user = {}
#Ask user for their entries to the dictionary
dict_user["name"] = input("Please enter your name: ").capitalize()
dict_user["age"] = int(input("Please enter your age: "))
dict_user["years coding"] = int(input("Please enter your amount of years coding: "))

#Ask for their first three programming languages as tuple
languages = []
for num in range(1,4):
    languages.append(input(f"Enter {num} of 3 of your first coding languages: ").capitalize())
tuple_language = tuple(languages)

#Ask for their 3 favourite coding languages as list
favorite_language = []
for num in range(1,4):
    favorite_language.append(input(f"Enter {num} of 3 of your favorite coding languages: ").capitalize())

#Create a set that is an intersection of first 3 languages, and favorite languages

language_intersection = list(set(languages) & set(favorite_language))

#Add all the collections to the dictionary
dict_user["first_languages"] = languages
dict_user["favorite_languages"] = favorite_language
dict_user["language_intersection"] = language_intersection

for pairs in dict_user.items():
    print(f"{pairs[0]} = {pairs[1]}")
