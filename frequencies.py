"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if type(item) != str:
            item = str(item)
        if item in frequencies.keys():
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    return frequencies

input = ['0', 4,4,'4','d','d','e',0,'a','d','4']
output = frequencies(input)
print(output)
