# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
# 2. Ask the user for the city that they grew up in.
# question_city = "What's name of the city you grew up in? "
# city = input(question_city)
# print(input(city))
street = input("What's name of the city you grew up in?\n")
# 3. Ask the user for the name of a pet.
# question_pet = "What's your pet's name? "
# pet = input(question_pet)
# print(input(pet))
pet = input("What's your pet's name?\n")
# 4. Combine the name of their city and pet and show them their band name.
# print("Your band name could be", city + ' ' + pet)
print("Your band name could be " + street + " " + pet)
# 5. Make sure the input cursor shows on a new line, see the example at:
# https://band-name-generator-end.appbrewery.repl.run/
