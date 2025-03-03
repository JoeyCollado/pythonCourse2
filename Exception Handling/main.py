try: #where exception might occur
    result = 10 / 0
except ZeroDivisionError as e: #if exception occurs
    print("Error: Cannot be divided by zero.")
else: #if no exception occurs
    print("Division Successful")
finally: #always executed
    print("Execution Complete")