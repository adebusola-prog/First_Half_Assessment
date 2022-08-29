# - Write a program that takes a text and returns each unique word and the number of times each unique word occurs in that text.
def unique_word(text):
    unique = []
    for i in text:
        if i not in unique:
            unique.append(i)
    print(unique)
    for k in range(len(unique)):
        print(unique[k], ":",  text.count(unique[k]))

text = ["come", "go", "rice", "go", "go"]       
unique_word(text)


















