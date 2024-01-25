#Function named 'count' takes a single parameter. The paremeter is a string.
#The string contains a single word devided into syllables by hyphens.

#Function counts the number of syllables and returns it.
    #E.g, count("ho-tel") returns 2

def count(string): 
    # [''.join( i if i != '-' else  for i in list(string))]
    # ([i for i in list(string) ].count('-')) if ([i for i in list(string)].count('-')) >= 1 else 0
    return  len(string.split('-'))
print(count("ho-tel")) # 2
print(count("cat")) # 1
print(count("met-a-phor")) # 3
print(count("ter-min-a-tor")) # 4