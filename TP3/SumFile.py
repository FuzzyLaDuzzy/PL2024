import sys
import re

def process_input():
    input_string = sys.stdin.read()
    total_sum = 0
    adding = False

    for match in re.finditer(r'on|off|=|\d', input_string):
        token = match.group()
        if token == 'on':
            adding = True
        elif token == 'off':
            adding = False
        elif token == '=':
            print("Sum is:", total_sum)
        elif adding and token.isdigit():
            total_sum += int(token)

process_input()
