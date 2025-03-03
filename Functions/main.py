#functions = are block of reusable code that performs a specific task

#basic syntax
#def functionName(paramaters):
#    """docstring"""
#    #function body  
#    return value

#def Keyword: This keyword is used to start the function definition.
# Function Name: A descriptive name following Python naming conventions (lowercase
#letters, underscores).
# Parameters: Optional. Enclosed in parentheses, these are placeholders for values
#(arguments) that the function will use.
# Docstring: Optional. A string literal that describes the function's purpose and behavior.
# Function Body: The indented block of code that performs the function’s operations.
# Return Statement: Optional. Specifies the value to be returned to the caller. If omitted, the
#function returns None by default.

#to call a function
#function_name(Arguments)

#
#Parameters: Variables listed in the function definition.
#Arguments: Values passed to the function when it is called.

#ex
def add(a,b):

    result = a + b
    return result


sum_result = add(5,3)
print(sum_result)


