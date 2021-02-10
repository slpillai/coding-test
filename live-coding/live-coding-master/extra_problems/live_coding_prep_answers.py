'''
Staircase
'''
def Staircase(n):
    for i in range(1,n+1):
        print_str = ""
        for j in range((n - i)):
            print_str += " "
        for k in range(i):
            print_str += "#"
    
        print(print_str)
    return(print_str)


'''
camelCase
'''

def camelCase(s):
    current_word = ''
    phrase = []
    for letter in s:
        if letter.islower():
            current_word += letter
        else:
            phrase.append(current_word)
            current_word = letter
    phrase.append(current_word)
    print(len(phrase))
    return(len(phrase))

'''
Grading Students
'''
def grading_students(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:
            print(grade)
            new_grades.append(grade)
        elif (grade % 5) > 2:
            grade = grade + (5 - (grade % 5))
            print(grade)
            new_grades.append(grade)
        else:
            print(grade)
            new_grades.append(grade)
    return new_grades

'''
Mars Exploration
'''

def mars_explore(s):
    string_mistakes = 0
    where_are_we = 1
    for i in range(len(s)):
        if where_are_we == 1 or where_are_we == 3:
            if s[i] != "S":
                string_mistakes += 1
        elif where_are_we == 2:
            if s[i] != "O":
                string_mistakes += 1
        if where_are_we == 3:
            where_are_we = 1
        else:
            where_are_we += 1
    print(string_mistakes)
    return(string_mistakes)


'''
Breaking Records
'''

def breaking_records(s):
    high = s[0]
    low = s[0]
    high_count = 0
    low_count = 0
    s.pop(0)
    for record in s:
        if record > high:
            high = record
            high_count += 1
        if record < low:
            low = record
            low_count += 1
    print(high_count, low_count)