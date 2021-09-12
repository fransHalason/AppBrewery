# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hello Angela")
#   print("How do you do Angela?")
#   print("Isn't the weather nice today?")
# greet()

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")
# greet_with_name("Angela")

# Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")


greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")

# Functions with keyword arguments
greet_with(location="London", name="Angela")
