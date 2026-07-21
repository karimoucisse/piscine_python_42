import random

def generator(text, sep = " ", option= None):

    if not isinstance(text, str):
        return print("ERROR")

    text_list = text.split(sep)

    if option == "shuffle":
        random_list = list()
        while len(text_list):
            random_word = random.choice(text_list)
            text_list.remove(random_word)
            random_list.append(random_word)
        text_list = random_list
    if option == "ordered":
        text_list.sort()

    if option == "unique":
        no_double_list = list()
        for item in text_list:
            if item not in no_double_list:
                no_double_list.append(item)
        text_list = no_double_list.copy()

    for item in text_list:
        yield item


text = "Lorem Ipsum Lorem Ipsum"
for word in generator(1, sep= " ", option="shuffle"):
    print(word)

