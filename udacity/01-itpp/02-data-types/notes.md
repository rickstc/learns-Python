# Introduction
- print() can be used to display information

# Arithmetic Operators
- "+" Addition
- "-" Subtraction
- "*" Multiplication
- "/" Division
- "%" Mod (remainder after dividing)
- "**" Exponentiation (not the ^)
- "//" Divides and rounds down to the nearest integer

Python follows usual order of mathematical operations
More information on the bitwise operators can be found here:
https://wiki.python.org/moin/BitwiseOperators

# Variables and Assignment Operators
`=` is an operator that assigns the value on the right to the variable on the left
Variable names are used to access the values

# Integers and Floats
Numeric Data Types:
- `int` - for integer values
- `float` - for decimal or floating point values

Type can be checked using `type(var)`

Division always returns a float, even if the result is an integer.

Python floats use approximation.

## Best Practices
[PEP8](https://www.python.org/dev/peps/pep-0008/) should be consulted for style. Lines of code should be limited to 80 characters.

# Booleans, Comparison Operators, and Logical Operators
- `bool` represents the variables `True` or `False`

Comparison operators produce `boolean` results. EX: `42 > 43` produces `False`

# Strings
Strings are immutable, ordered sequences of characters, and are how Python works with text.

Strings are defined using quotes; either single or double.

Quotation marks can be included in strings:
- By using the other type of quoteation than you're trying to include
    - Ex: `bike_string = "The boy took Tim's bike."`
- By escaping the quotation:
    - Ex: `bike_string = "\"Hey!\" he shouted as the boy took Tim's bike."`


## String Operations:
- `+` concatenates strings
    - Ex: `print("Hello " + "World")`
- `*` repeats strings
- `len` calculates string length
    - Ex: `print(len("Udacity"))` yields 7

# Type and Type Converstions
One type can be cast to another type like this:  
`grams = "35.0" # String`  
`grams = float(grams) # Float`

# String Methods
Methods are related to functions, but are associated with different types of objects.  
Methods belong to an object, like `islower()` belongs to the `String` class.  
Example: `print("sebastian thrun").islower()`

# Another String Method - Split
The string `split` method returns a `list` containing words from the input string.
It takes two arguments:
- sep - the character used to split up the string
- maxsplit - the maximum number of splits

# "There's a Bug in my Code"
Basically, use print statements and stack overflow...

# Conclusion

# Summary