
def get_number(prompt):
    value = input(prompt)
    while not value.isdigit():
        print(f"Not a number: {value}")
        value = input(prompt)
    
    return int(value)


n = get_number("Irj be egy egesz szamot: ")

print(n, type(n))
