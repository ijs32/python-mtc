
location = dict(
    state="SC",
    city="Cola"
)
print(type(location))


def word_counter(word):
    word = word.replace(" ", "")
    counter = dict()
    for i in range(len(word)):
        if word[i] in counter:
            counter[word[i]] += 1
        else:
            counter[word[i]] = 1
    return counter


print(word_counter("this is a test"))

dict1 = dict(
    hello="greeting"
)

dict2 = dict(
    goodbye="bye",
    hello="greeting"
)


def dictionary_combiner(dict1, dict2):
    for key, value in dict1.items():
        if key in dict2:
            continue
        else:
            dict2[key] = value
    return dict2


print(dictionary_combiner(dict1, dict2))
