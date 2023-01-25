programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# print(programming_dictionary)

# adding a new item to the dictionary
programming_dictionary["loop"] = "The action of doing something over and over again"

# checking that new item is in the dictionary
print(programming_dictionary)

# wiping the the dictionary values
# programming_dictionary = {}

# checking that dictionary is now cleaned out.
# print(programming_dictionary)

# loop through a dictionary this prints the keys only

# for i in programming_dictionary:
# print(i)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
