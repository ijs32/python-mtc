# string = input("Word to convert: ")
# count = int(input("How many letters at the end of the string should be converted? "))
string = "string"
count = len(string) - 2

caps = string[:count] + string[count:].upper()
print(caps)
