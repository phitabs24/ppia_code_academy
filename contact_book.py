# Achu Philemon Tabufor, phitabs24@gmail.com
# Assignment 4 - Term 1, 2023

# create phonebook containing all contact addresses
phonebook = { "achu philemon tabufor" : {"home phone number" : " ",
"mobile phone number" : "237 670 290 583", 
"Work phone number" : " ",
"personal email address" : "phitabs24@gmail.com",
"work email address" : "subscribeachu@gmail.com",
"home address" : " ",
"work address" : " "}, 

"david" : {"home phone number" : " ",
"mobile phone number" : "237 670 290 583", 
"Work phone number" : " ",
"personal email address" : "phitabs24@gmail.com",
"work email address" : "subscribeachu@gmail.com",
"home address" : " ",
"work address" : " "},

"zofia" : {"mobile phone number" : "237 670 290 583", 
"personal email address" : "phitabs24@gmail.com",
"pork email address" : "subscribeachu@gmail.com",
},

"achu djokep" : {"home phone number" : " ",
"mobile phone number" : "237 670 290 583", 
"Work phone number" : " ",
"personal email address" : "phitabs24@gmail.com",
"work email address" : "subscribeachu@gmail.com",
"home address" : " ",
"work address" : " "}, 
}

# ask the user to enter a name(substring) to search for
search_key = input("\nEnter a name to search for: ").lower()

# check if the dictionary contains any names with substring entered by the user
# If so, returns a dictionary with all the names that match the searched substring
res = dict(filter(lambda item: search_key in item[0], phonebook.items()))

#check if the search result is empty
if bool(res) == True:
	# if search result is not empty, print the available contact info of all names in search result
	for key in res:
		print("\nContact information found for " + str(key).upper() + "!\n")
		if "home phone number" in phonebook[key]:
			print(str(key).upper() + " can be reached via their home phone number at " + str(phonebook[key]["home phone number"]))
		if "mobile phone number" in phonebook[key]:
			print(str(key).upper() + " can be reached via their mobile phone number at " + str(phonebook[key]["mobile phone number"]))
		if "work phone number" in phonebook[key]:
			print(str(key).upper() + " can be reached via their work phone number at " + str(phonebook[key]["work phone number"]))
		if "personal email address" in phonebook[key]:
			print(str(key).upper() + " can be reached via their personal email address at " + str(phonebook[key]["personal email address"]))
		if "work email address" in phonebook[key]:
			print(str(key).upper() + " can be reached via their work email address at " + str(phonebook[key]["work email address"]))
		if "home address" in phonebook[key]:
			print(str(key).upper() + " can be reached via their home address at " + str(phonebook[key]["home address"]))
		if "work address" in phonebook[key]:
			print(str(key).upper() + " can be reached via their work address at " + str(phonebook[key]["work address"]) + "")
		print("\n")
else:
	# if search results is empty, print
	print("No contact information found for " + str(search_key).upper() + "! Be sure to ask them for their contact details next time you see them.")