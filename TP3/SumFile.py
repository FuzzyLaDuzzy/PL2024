def process_input():
    input_string = sys.stdin.read()
    total_sum = 0
    adding = False

    for char in input_string:
        if char == 'o':
            adding = True
        elif char == '=' and adding:
            print(total_sum)
        elif char == 'f':
            adding = False
        elif adding and char.isdigit():
            total_sum += int(char)

process_input()
