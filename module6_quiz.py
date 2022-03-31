dict_masher = {
    "name": "Amos",
    "age": 100
}

print(dict_masher)

a = {1, 2, 3}
a.remove(3)
print(a)

c = {"name": "Skandar Keynes", "age": "24", "sex": "male"}
d = c.setdefault("name")
print(d)

# The copy method creates shallow copies of dictionaries

a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3, 7, 8, 9, 10}
print(a-b)
