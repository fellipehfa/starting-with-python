# You can concatenate strings with three different methods.
name =  "Fellipe Henrique" # just a string variable

# The first method is the plus sign: +
print("Hello, my name is " + name + "!")
# The second method is using the format method:
print("Hello, my name is {}!".format(name))
# The third method is using the f-string:
print(f"Hello, my name is {name}!")

adj = input("Adjective: ")
first_verb = input("First verb: ")
second_verb = input("Second verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time, because I love to {first_verb}. Stay hydrated and {second_verb} like you are {famous_person}!"

print(madlib )
