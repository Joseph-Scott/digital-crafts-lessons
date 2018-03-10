first_string = "Good"
second_string = "Cheese"
third_string = "Man"
fourth_string = "Spoon"

long_vowels = ['oo', 'ee', 'aa', 'ii', 'uu']

result = ''
for index in range(len(first_string)):   # [0,1,2,3,4,5]
    twoletters = first_string[index:index+2]
    if twoletters in long_vowels:
        result += first_string[index] * 4
    else:
        result += first_string[index]
    
print result


first_string = first_string.replace['ee', 'eeeee']