# Achu Philemon Tabufor, phitabs24@gmail.com
# Assignment 4 - Term 1, 2023

phonebook = { "achu philemon tabufor" : {"home phone number" : " ",
"mobile phone number" : "237 670 290 583", 
"Work phone number" : " ",
"personal Email address" : "phitabs24@gmail.com",
"work Email address" : "subscribeachu@gmail.com",
"home address" : " ",
"work address" : " "}, 

"david" : {"home phone number" : " ",
"mobile phone number" : "237 670 290 583", 
"Work phone number" : " ",
"personal Email address" : "phitabs24@gmail.com",
"work Email address" : "subscribeachu@gmail.com",
"home address" : " ",
"work address" : " "},

"zofia" : {"home phone number" : " ",
"mobile phone number" : "237 670 290 583", 
"mork phone number" : " ",
"personal Email address" : "phitabs24@gmail.com",
"pork Email address" : "subscribeachu@gmail.com",
"home address" : " ",
"work address" : " "},

"djokep" : {"home phone number" : " ",
"mobile phone number" : "237 670 290 583", 
"Work phone number" : " ",
"personal Email address" : "phitabs24@gmail.com",
"work Email address" : "subscribeachu@gmail.com",
"home address" : " ",
"work address" : " "}, 
}

search_key = input("Enter a name to search for: ").lower()

if search_key in phonebook:
	print("Contact information found for " + str(phonebook[search_key]) + "!")
	if "home phone number" in phonebook[search_key]:
		print(str(search_key) + " can be reached via their home phone number at " + str(phonebook[search_key]["home phone number"]))
	if "mobile phone number" in phonebook[search_key]:
		print(str(search_key) + " can be reached via their mobile phone number at " + str(phonebook[search_key]["mobile phone number"]))
	if "work phone number" in phonebook[search_key]:
		print(str(search_key) + " can be reached via their work phone number at " + str(phonebook[search_key]["work phone number"]))
	if "personal email address" in phonebook[search_key]:
		print(str(search_key) + " can be reached via their personal email address at " + str(phonebook[search_key]["personal email address"]))
	if "work email address" in phonebook[search_key]:
		print(str(search_key) + " can be reached via their work email address at " + str(phonebook[search_key]["work email address"]))
	if "home address" in phonebook[search_key]:
		print(str(search_key) + " can be reached via their home address at " + str(phonebook[search_key]["home address"]))
	if "work address" in phonebook[search_key]:
		print(str(search_key) + " can be reached via their work address at " + str(phonebook[search_key]["work address"]))
else:
	print("No contact information found for " + str(search_key) + "! Be sure to ask them for their contact details next time you see them.")
