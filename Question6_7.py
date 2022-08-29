# - Write a program that reads words from a provided text file and returns each 
# unique word, the number of times they appear, the line numbers they appear at 
# and whether its a consonant or vowel.
uniq_word = []
uniq_no = []
import string
consonants = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"
with open("C:/Users/zeu/Documents/Exam_First/exam.txt") as txt:
    text = txt.read()
from string import punctuation
text = text.lower()
for char in punctuation:
    text = text.replace(char, '')
words = text.split()
# print(words)

for i in words:
    if i not in uniq_word:
        uniq_word.append(i)
for k in range(len(uniq_word)):
        l = words.count(uniq_word[k])
        uniq_no.append(l)
        print(uniq_word[k], ":",  l)
print(uniq_word)
print(len(uniq_word))
print(uniq_no)
print(len(uniq_no))

start_vow_con = []
for char in uniq_word:
    if char[0] in vowel:
        x= "vowel"
        start_vow_con.append(x)
        
    else:
        y = "consonant"
        start_vow_con.append(y)
print(start_vow_con)

import pandas as pd
d = {"unique_word" : uniq_word, "no_of_times_it_appears": uniq_no, "starts_with": start_vow_con}

dataFrame = pd.DataFrame(d)
print("DataFrame\n",dataFrame)
print("\n")

dataFrame.to_csv("C:/Users/zeu/Documents/Exam_First/exam.csv")



def text_find(key, filename):
    with open(filename) as file: 
        lines = file.readlines()  
    for line_number, line in enumerate(lines, 1): 
        if key in line:
            print(f'{key} is on line {line_number}') 

for item in uniq_word:
    text_find(item, "C:/Users/zeu/Documents/Exam_First/exam.csv")