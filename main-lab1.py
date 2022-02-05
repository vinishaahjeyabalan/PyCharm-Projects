# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/"""

print("Hello World")
name = input("what is your name?")
print(name)

animals = ["tiger", "lion", "mouse", "dog", "cat"]
print(animals)
print(animals[2])
animals[2] = "deer"
print(animals)
print(len(animals))
print(animals.index("cat"))
animals.remove("dog")
print(animals)
animals.append("buffalo")
animals.insert(2, "goat")
print(animals)

flowers = {"jasmine": 5,
           "hibiscus": 8,
           "rose": ["white", "red", "pink"],
           "carnation": 10}

print(flowers["rose"][2])
print(flowers)
animalss = []
for ani in animals:
    animalss.append(ani + "*new*")

print(animalss)


