numbers = [1,2,0,4,5]

for num in numbers:
    if num == 0:
        print("Skipping zero")
        continue

    try:
        result = 10 / num
    except ZeroDivisionError:
        print("Error: Cannot divided by zero.")
    else:
        print(f"10 divided by {num} is {result}")
    finally:
        print("iteration complete")

    if 0 in numbers:
        print("zero is in the list")
    else:
        print("zero is not in the list")