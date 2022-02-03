# string = input("Sentence: ")
# sub_string = input("Word to look for in sentence: ")
# list = string.lower().split(" ")
# count = 0
# for word in list:
#     if word == sub_string:
#         count += 1
# print("There are {} occurences of '{}' in the sentence".format(count, sub_string))

string = input("Sentence: ")
string = string.replace(" ", "").lower()
sub_string = input("Word to look for in sentence: ")
count = 0
for i, char in enumerate(string):
    if string[i: i + len(sub_string)] == sub_string:
        count += 1
print("There are {} occurences of '{}' in the sentence".format(count, sub_string))

print("There are 3 occurrences of 'because' in the sentence" ==
      "There are 3 occurrences of 'because' in the sentence")
