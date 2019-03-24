# int 范围


value = 1000
print(type(value))
while True:
    try:
        value *= value
        print(value)
    except Exception as e:
        print(e)
