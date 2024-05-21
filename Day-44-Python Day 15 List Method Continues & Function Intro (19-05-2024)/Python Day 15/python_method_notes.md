## **Python Methods/Functions**
- [**Built-in Functions**](#built-in-functions)
    - [**Mathematical Functions**](#mathematical-functions)
    - [**Type Conversion**](#type-conversion)
    - [**Iteration and Sequence Operations**](#iteration-and-sequence-operations)

## **Built-in Functions**
### **Mathematical Functions**
- [abs()](https://www.w3schools.com/python/ref_func_abs.asp): **Returns the absolute value of a number.** 
    ```python
    # Example using a positive number
    positive_number = 10
    positive_result = abs(positive_number)
    print(f"The absolute value of {positive_number} is {positive_result}")

    # Example using a negative number
    negative_number = -5
    negative_result = abs(negative_number)
    print(f"The absolute value of {negative_number} is {negative_result}")

    # Example using zero
    zero = 0
    zero_result = abs(zero)
    print(f"The absolute value of {zero} is {zero_result}")
    ```
    Output:
    ```
    The absolute value of 10 is 10
    The absolute value of -5 is 5
    The absolute value of 0 is 0
    ```
    _`abs()` converts negative numbers to positive ones, while positive numbers and zero remain unchanged._

    [⬆️ Go to top](#python-methodsfunctions)
- [divmod()](https://www.w3schools.com/python/ref_func_divmod.asp): **Returns a tuple containing the quotient and remainder when dividing two numbers.**
    ```python
    # Example using two positive integers
    numerator = 10
    denominator = 3
    result = divmod(numerator, denominator)
    print(f"The quotient and remainder of {numerator} divided by {denominator} are {result}")

    # Example using a negative numerator
    numerator = -10
    denominator = 3
    result = divmod(numerator, denominator)
    print(f"The quotient and remainder of {numerator} divided by {denominator} are {result}")

    # Example using a negative denominator
    numerator = 10
    denominator = -3
    result = divmod(numerator, denominator)
    print(f"The quotient and remainder of {numerator} divided by {denominator} are {result}")

    # Example using floating-point numbers
    numerator = 10.5
    denominator = 3
    result = divmod(numerator, denominator)
    print(f"The quotient and remainder of {numerator} divided by {denominator} are {result}")
    ```
    Output:
    ```
    The quotient and remainder of 10 divided by 3 are (3, 1)
    The quotient and remainder of -10 divided by 3 are (-4, 2)
    The quotient and remainder of 10 divided by -3 are (-4, -2)
    The quotient and remainder of 10.5 divided by 3 are (3.0, 1.5)
    ```
    _The `divmod()` function works with both integers and floating-point numbers, returning the quotient and remainder as a tuple._

    [⬆️ Go to top](#python-methodsfunctions)
- [float()](https://www.w3schools.com/python/ref_func_float.asp): **Converts a value to a floating-point number.**
    ```python
    # Example using an integer
    integer_value = 10
    float_result = float(integer_value)
    print(f"The floating-point representation of {integer_value} is {float_result}")

    # Example using a string representing a number
    string_value = "12.34"
    float_result = float(string_value)
    print(f"The floating-point representation of '{string_value}' is {float_result}")

    # Example using a string representing an integer
    string_value_int = "56"
    float_result = float(string_value_int)
    print(f"The floating-point representation of '{string_value_int}' is {float_result}")

    # Example using a string with leading and trailing spaces
    string_value_spaces = "  78.90  "
    float_result = float(string_value_spaces)
    print(f"The floating-point representation of '{string_value_spaces}' is {float_result}")

    # Example using a boolean value
    boolean_value = True
    float_result = float(boolean_value)
    print(f"The floating-point representation of {boolean_value} is {float_result}")

    # Example using a boolean value (False)
    boolean_value_false = False
    float_result = float(boolean_value_false)
    print(f"The floating-point representation of {boolean_value_false} is {float_result}")
    ```
    Output:
    ```
    The floating-point representation of 10 is 10.0
    The floating-point representation of '12.34' is 12.34
    The floating-point representation of '56' is 56.0
    The floating-point representation of '  78.90  ' is 78.9
    The floating-point representation of True is 1.0
    The floating-point representation of False is 0.0
    ```
    _`float()` converts the input into a floating-point number. Integers remain unchanged, string representations of numbers are converted to their equivalent floating-point values, leading and trailing spaces in strings are trimmed, and boolean values are converted to 1.0 for True and 0.0 for False._

    [⬆️ Go to top](#python-methodsfunctions)
- [int()](https://www.w3schools.com/python/ref_func_int.asp): **Converts a value to an integer.** 
    ```python
    # Example using a floating-point number
    float_value = 12.34
    int_result = int(float_value)
    print(f"The integer representation of {float_value} is {int_result}")

    # Example using a string representing an integer
    string_value = "56"
    int_result = int(string_value)
    print(f"The integer representation of '{string_value}' is {int_result}")

    # Example using a string representing a floating-point number (this will cause an error)
    string_value_float = "78.90"
    int_result = int(string_value_float)
    print(f"The integer representation of '{string_value_float}' is {int_result}")

    # Example using a boolean value
    boolean_value = True
    int_result = int(boolean_value)
    print(f"The integer representation of {boolean_value} is {int_result}")

    # Example using a boolean value (False)
    boolean_value_false = False
    int_result = int(boolean_value_false)
    print(f"The integer representation of {boolean_value_false} is {int_result}")

    # Example using a number in a different base (e.g., binary, hexadecimal)
    binary_string = "1010"
    int_result = int(binary_string, 2)
    print(f"The integer representation of binary '{binary_string}' is {int_result}")

    hex_string = "1A"
    int_result = int(hex_string, 16)
    print(f"The integer representation of hexadecimal '{hex_string}' is {int_result}")
    ```
    Output:
    ```
    The integer representation of 12.34 is 12
    The integer representation of '56' is 56
    The integer representation of True is 1
    The integer representation of False is 0
    The integer representation of binary '1010' is 10
    The integer representation of hexadecimal '1A' is 26
    ```
    _`int()` converts the input into an integer. Floating-point numbers are truncated, string representations of integers are converted directly, boolean values are converted to 1 for True and 0 for False. It can also handle conversion from binary and hexadecimal strings if specified._

    [⬆️ Go to top](#python-methodsfunctions)
- [max()](https://www.w3schools.com/python/ref_func_max.asp): **Returns the largest item in an iterable or the largest of two or more arguments.**
    ```python
    # Example using a list of numbers
    numbers = [10, 20, 30, 40, 50]
    max_number = max(numbers)
    print(f"The largest number in the list is {max_number}")

    # Example using multiple arguments
    max_value = max(5, 10, 15, 20)
    print(f"The largest value among the arguments is {max_value}")

    # Example using a list of strings
    strings = ["apple", "banana", "cherry", "date"]
    max_string = max(strings)
    print(f"The largest string in the list is '{max_string}'")

    # Example using a tuple of numbers
    tuple_numbers = (3, 6, 2, 8, 1)
    max_tuple_number = max(tuple_numbers)
    print(f"The largest number in the tuple is {max_tuple_number}")

    # Example using the key argument
    names = ["Alice", "Bob", "Charlie", "David"]
    longest_name = max(names, key=len)
    print(f"The longest name in the list is '{longest_name}'")

    # Example using a dictionary to find the key with the highest value
    grades = {"Alice": 85, "Bob": 92, "Charlie": 87}
    max_grade_student = max(grades, key=grades.get)
    print(f"The student with the highest grade is {max_grade_student}")
    ```
    Output:
    ```
    The largest number in the list is 50
    The largest value among the arguments is 20
    The largest string in the list is 'date'
    The largest number in the tuple is 8
    The longest name in the list is 'Charlie'
    The student with the highest grade is Bob
    ```
    _`max()` returns the largest item in an iterable or the largest of two or more arguments. It can operate on lists, tuples, and strings, returning the maximum value. You can also specify a key function to determine how to evaluate the items._

    [⬆️ Go to top](#python-methodsfunctions)
- [min()](https://www.w3schools.com/python/ref_func_min.asp): **Returns the smallest item in an iterable or the smallest of two or more arguments.** 
    ```python
    # Example using a list of numbers
    numbers = [10, 20, 30, 40, 50]
    min_number = min(numbers)
    print(f"The smallest number in the list is {min_number}")

    # Example using multiple arguments
    min_value = min(5, 10, 15, 20)
    print(f"The smallest value among the arguments is {min_value}")

    # Example using a list of strings
    strings = ["apple", "banana", "cherry", "date"]
    min_string = min(strings)
    print(f"The smallest string in the list is '{min_string}'")

    # Example using a tuple of numbers
    tuple_numbers = (3, 6, 2, 8, 1)
    min_tuple_number = min(tuple_numbers)
    print(f"The smallest number in the tuple is {min_tuple_number}")

    # Example using the key argument
    names = ["Alice", "Bob", "Charlie", "David"]
    shortest_name = min(names, key=len)
    print(f"The shortest name in the list is '{shortest_name}'")

    # Example using a dictionary to find the key with the lowest value
    grades = {"Alice": 85, "Bob": 92, "Charlie": 87}
    min_grade_student = min(grades, key=grades.get)
    print(f"The student with the lowest grade is {min_grade_student}")
    ```
    Output:
    ```
    The smallest number in the list is 10
    The smallest value among the arguments is 5
    The smallest string in the list is 'apple'
    The smallest number in the tuple is 1
    The shortest name in the list is 'Bob'
    The student with the lowest grade is Alice
    ```
    _`min()` returns the smallest item in an iterable or the smallest of two or more arguments. It operates similarly to max(), but returns the minimum value instead._

    [⬆️ Go to top](#python-methodsfunctions)
- [pow()](https://www.w3schools.com/python/ref_func_pow.asp): **Returns the value of a number raised to a specified power.**
    ```python
    # Example using two arguments (base and exponent)
    base = 2
    exponent = 3
    result = pow(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")

    # Example using three arguments (base, exponent, and modulus)
    base = 2
    exponent = 3
    modulus = 5
    result = pow(base, exponent, modulus)
    print(f"{base} raised to the power of {exponent} modulo {modulus} is {result}")

    # Example using floating-point numbers
    base = 2.5
    exponent = 3
    result = pow(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")

    # Example using a negative exponent
    base = 2
    exponent = -3
    result = pow(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")
    ```
    Output:
    ```
    2 raised to the power of 3 is 8
    2 raised to the power of 3 modulo 5 is 3
    2.5 raised to the power of 3 is 15.625
    2 raised to the power of -3 is 0.125
    ```
    _`pow()` function is used to calculate exponentiation. It can take two arguments (base and exponent) or three arguments (base, exponent, and modulus). It returns the result of raising the base to the power of the exponent, optionally modulo the modulus._

    [⬆️ Go to top](#python-methodsfunctions)
- [round()](https://www.w3schools.com/python/ref_func_round.asp): **Rounds a number to a specified number of decimal places.** 
    ```python
    # Example using a floating-point number
    float_number = 3.14159
    rounded_number = round(float_number, 2)  # Round to 2 decimal places
    print(f"The rounded number is {rounded_number}")

    # Example using a positive integer
    positive_integer = 12345
    rounded_integer = round(positive_integer, -2)  # Round to the nearest hundred
    print(f"The rounded integer is {rounded_integer}")

    # Example using a negative integer
    negative_integer = -9876
    rounded_negative_integer = round(negative_integer, -3)  # Round to the nearest thousand
    print(f"The rounded negative integer is {rounded_negative_integer}")
    ```
    Output:
    ```
    The rounded number is 3.14
    The rounded integer is 12300
    The rounded negative integer is -10000
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [sum()](https://www.w3schools.com/python/ref_func_sum.asp): **Sums the items of an iterable.**
    ```python
    # Example using a list of numbers
    numbers = [1, 2, 3, 4, 5]
    sum_of_numbers = sum(numbers)
    print(f"The sum of numbers is {sum_of_numbers}")

    # Example using a tuple of numbers
    tuple_numbers = (10, 20, 30, 40, 50)
    sum_of_tuple = sum(tuple_numbers)
    print(f"The sum of tuple numbers is {sum_of_tuple}")

    # Example using a generator expression
    generator_sum = sum(x for x in range(6))  # Sum of numbers from 0 to 5
    print(f"The sum of numbers from 0 to 5 is {generator_sum}")
    ```
    Output:
    ```
    The sum of numbers is 15
    The sum of tuple numbers is 150
    The sum of numbers from 0 to 5 is 15
    ```
    [⬆️ Go to top](#python-methodsfunctions)
### **Type Conversion** 
- [bin()](https://www.w3schools.com/python/ref_func_bin.asp): **Converts an integer to a binary string.**
    ```python
    # Example using an integer
    integer_value = 10
    binary_string = bin(integer_value)
    print(f"The binary representation of {integer_value} is {binary_string}")
    ```
    Output:
    ```
    The binary representation of 10 is 0b1010
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [bool()](https://www.w3schools.com/python/ref_func_bool.asp): **Converts a value to a Boolean.** 
    ```python
    # Integer value
    value_1 = 42
    # Convert the integer value to a Boolean
    bool_value_1 = bool(value_1)
    # Print the original value and its Boolean representation
    print(f"The Boolean representation of {value_1} is {bool_value_1}")

    # Integer value (zero)
    value_2 = 0
    bool_value_2 = bool(value_2)
    print(f"The Boolean representation of {value_2} is {bool_value_2}")

    # String value
    value_3 = "Hello"
    bool_value_3 = bool(value_3)
    print(f"The Boolean representation of '{value_3}' is {bool_value_3}")

    # Empty string
    value_4 = ""
    bool_value_4 = bool(value_4)
    print(f"The Boolean representation of '{value_4}' is {bool_value_4}")

    # List value
    value_5 = [1, 2, 3]
    bool_value_5 = bool(value_5)
    print(f"The Boolean representation of {value_5} is {bool_value_5}")

    # Empty list
    value_6 = []
    bool_value_6 = bool(value_6)
    print(f"The Boolean representation of {value_6} is {bool_value_6}")

    # Dictionary value
    value_7 = {"a": 1, "b": 2}
    bool_value_7 = bool(value_7)
    print(f"The Boolean representation of {value_7} is {bool_value_7}")

    # Empty dictionary
    value_8 = {}
    bool_value_8 = bool(value_8)
    print(f"The Boolean representation of {value_8} is {bool_value_8}")

    ```
    Output:
    ```
    The Boolean representation of 42 is True
    The Boolean representation of 0 is False
    The Boolean representation of 'Hello' is True
    The Boolean representation of '' is False
    The Boolean representation of [1, 2, 3] is True
    The Boolean representation of [] is False
    The Boolean representation of {'a': 1, 'b': 2} is True
    The Boolean representation of {} is False
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [bytearray()](https://www.w3schools.com/python/ref_func_bytearray.asp): **Returns a bytearray object.**
    ```python
    # Example using a string
    string = "Hello, world!"
    byte_array_from_string = bytearray(string, 'utf-8')
    print(byte_array_from_string)

    # Example using an iterable of integers
    integers = [65, 66, 67, 68, 69]
    byte_array_from_integers = bytearray(integers)
    print(byte_array_from_integers)

    # Example using a bytes object
    bytes_object = b"Python"
    byte_array_from_bytes = bytearray(bytes_object)
    print(byte_array_from_bytes)

    # Example using a bytearray object
    existing_byte_array = bytearray(b"Existing")
    byte_array_from_existing = bytearray(existing_byte_array)
    print(byte_array_from_existing)

    # Example using a range object
    range_obj = range(10)
    byte_array_from_range = bytearray(range_obj)
    print(byte_array_from_range)
    ```
    Output:
    ```
    bytearray(b'Hello, world!')
    bytearray(b'ABCDE')
    bytearray(b'Python')
    bytearray(b'Existing')
    bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [bytes()](https://www.w3schools.com/python/ref_func_bytes.asp): **Returns a bytes object.**
    ```python
    # Example using a string with encoding
    string_value = "Hello, World!"
    bytes_object = bytes(string_value, encoding='utf-8')
    print(f"The bytes representation of '{string_value}' is {bytes_object}")

    # Example using a list of integers (each representing a byte)
    byte_list = [72, 101, 108, 108, 111]
    bytes_object = bytes(byte_list)
    print(f"The bytes representation of {byte_list} is {bytes_object}")

    # Example using a bytes literal
    bytes_literal = b"Hello, World!"
    print(f"The bytes literal is {bytes_literal}")

    # Example creating an empty bytes object
    empty_bytes = bytes()
    print(f"The empty bytes object is {empty_bytes}")

    # Example creating a bytes object of a specified size with zero initialization
    size = 5
    zero_bytes = bytes(size)
    print(f"The bytes object of size {size} with zero initialization is {zero_bytes}")

    # Example using an iterable
    iterable = (65, 66, 67)
    bytes_from_iterable = bytes(iterable)
    print(f"The bytes object created from iterable {iterable} is {bytes_from_iterable}")
    ```
    Output:
    ```
    The bytes representation of 'Hello, World!' is b'Hello, World!'
    The bytes representation of [72, 101, 108, 108, 111] is b'Hello'
    The bytes literal is b'Hello, World!'
    The empty bytes object is b''
    The bytes object of size 5 with zero initialization is b'\x00\x00\x00\x00\x00'
    The bytes object created from iterable (65, 66, 67) is b'ABC'
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [chr()](https://www.w3schools.com/python/ref_func_chr.asp): **Returns the string representing a character whose Unicode code point is the integer.**
    ```python
    # Example using a Unicode code point for a common character
    code_point = 65
    character = chr(code_point)
    print(f"The character for Unicode code point {code_point} is '{character}'")

    # Example using a Unicode code point for a special character
    code_point = 9731
    character = chr(code_point)
    print(f"The character for Unicode code point {code_point} is '{character}'")

    # Example using a Unicode code point for an emoji
    code_point = 128515
    character = chr(code_point)
    print(f"The character for Unicode code point {code_point} is '{character}'")

    # Example using a Unicode code point for a non-printable character
    code_point = 10
    character = chr(code_point)
    print(f"The character for Unicode code point {code_point} is a newline: {repr(character)}")
    ```
    Output:
    ```
    The character for Unicode code point 65 is 'A'
    The character for Unicode code point 9731 is '☃'
    The character for Unicode code point 128515 is '😁'
    The character for Unicode code point 10 is a newline: '\n'
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [complex()](https://www.w3schools.com/python/ref_func_complex.asp): **Creates a complex number.**
    ```python
    # Example using two arguments (real and imaginary parts)
    real_part = 3
    imaginary_part = 5
    complex_number = complex(real_part, imaginary_part)
    print(f"The complex number with real part {real_part} and imaginary part {imaginary_part} is {complex_number}")

    # Example using a single argument (real part only)
    real_part_only = 4
    complex_number = complex(real_part_only)
    print(f"The complex number with real part {real_part_only} and no imaginary part is {complex_number}")

    # Example using string representation of a complex number
    complex_string = "2+3j"
    complex_number = complex(complex_string)
    print(f"The complex number created from the string '{complex_string}' is {complex_number}")

    # Example using default arguments (0 + 0j)
    default_complex = complex()
    print(f"The default complex number with no arguments is {default_complex}")
    ```
    Output:
    ```
    The complex number with real part 3 and imaginary part 5 is (3+5j)
    The complex number with real part 4 and no imaginary part is (4+0j)
    The complex number created from the string '2+3j' is (2+3j)
    The default complex number with no arguments is 0j
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [dict()](https://www.w3schools.com/python/ref_func_dict.asp): **Creates a dictionary.** 
    ```python
    # Creating an empty dictionary
    empty_dict = dict()
    print(f"Empty dictionary: {empty_dict}")

    # Creating a dictionary using key-value pairs
    key_value_pairs_dict = dict(name="Alice", age=30, city="New York")
    print(f"Dictionary from key-value pairs: {key_value_pairs_dict}")

    # Creating a dictionary from a list of tuples
    list_of_tuples = [("name", "Bob"), ("age", 25), ("city", "Los Angeles")]
    tuple_dict = dict(list_of_tuples)
    print(f"Dictionary from list of tuples: {tuple_dict}")

    # Creating a dictionary from a list of lists
    list_of_lists = [["name", "Carol"], ["age", 22], ["city", "Chicago"]]
    list_dict = dict(list_of_lists)
    print(f"Dictionary from list of lists: {list_dict}")

    # Creating a dictionary using keyword arguments
    kwargs_dict = dict(first=1, second=2, third=3)
    print(f"Dictionary from keyword arguments: {kwargs_dict}")

    # Creating a dictionary from another dictionary
    existing_dict = {"a": 1, "b": 2, "c": 3}
    copy_dict = dict(existing_dict)
    print(f"Dictionary copied from another dictionary: {copy_dict}")
    ```
    Output:
    ```
    Empty dictionary: {}
    Dictionary from key-value pairs: {'name': 'Alice', 'age': 30, 'city': 'New York'}
    Dictionary from list of tuples: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
    Dictionary from list of lists: {'name': 'Carol', 'age': 22, 'city': 'Chicago'}
    Dictionary from keyword arguments: {'first': 1, 'second': 2, 'third': 3}
    Dictionary copied from another dictionary: {'a': 1, 'b': 2, 'c': 3}
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [frozenset()](https://www.w3schools.com/python/ref_func_frozenset.asp): **Returns a frozenset object.** 
    ```python
    # Creating an empty frozenset
    empty_frozenset = frozenset()
    print(f"Empty frozenset: {empty_frozenset}")

    # Creating a frozenset from a list
    list_data = [1, 2, 3, 2, 1]
    frozenset_from_list = frozenset(list_data)
    print(f"Frozenset from list: {frozenset_from_list}")

    # Creating a frozenset from a string
    string_data = "hello"
    frozenset_from_string = frozenset(string_data)
    print(f"Frozenset from string: {frozenset_from_string}")

    # Creating a frozenset from a set
    set_data = {4, 5, 6}
    frozenset_from_set = frozenset(set_data)
    print(f"Frozenset from set: {frozenset_from_set}")

    # Using a frozenset as a key in a dictionary
    frozenset_key = frozenset([1, 2, 3])
    dictionary = {frozenset_key: "value"}
    print(f"Dictionary with frozenset key: {dictionary}")

    # Frozenset operations (union, intersection, difference)
    frozenset_a = frozenset([1, 2, 3, 4])
    frozenset_b = frozenset([3, 4, 5, 6])

    union_result = frozenset_a | frozenset_b  # Union
    intersection_result = frozenset_a & frozenset_b  # Intersection
    difference_result = frozenset_a - frozenset_b  # Difference

    print(f"Union of {frozenset_a} and {frozenset_b}: {union_result}")
    print(f"Intersection of {frozenset_a} and {frozenset_b}: {intersection_result}")
    print(f"Difference of {frozenset_a} and {frozenset_b}: {difference_result}")
    ```
    Output:
    ```
    Empty frozenset: frozenset()
    Frozenset from list: frozenset({1, 2, 3})
    Frozenset from string: frozenset({'e', 'o', 'l', 'h'})
    Frozenset from set: frozenset({4, 5, 6})
    Dictionary with frozenset key: {frozenset({1, 2, 3}): 'value'}
    Union of frozenset({1, 2, 3, 4}) and frozenset({3, 4, 5, 6}): frozenset({1, 2, 3, 4, 5, 6})
    Intersection of frozenset({1, 2, 3, 4}) and frozenset({3, 4, 5, 6}): frozenset({3, 4})
    Difference of frozenset({1, 2, 3, 4}) and frozenset({3, 4, 5, 6}): frozenset({1, 2})
    ```
    _The `frozenset()` function is useful for creating immutable sets that ensure the uniqueness of elements and can be used in contexts where mutability is not desired._

    [⬆️ Go to top](#python-methodsfunctions)
    _The `frozenset()` function is useful for creating immutable sets that ensure the uniqueness of elements and can be used in contexts where mutability is not desired._
- [hex()](https://www.w3schools.com/python/ref_func_hex.asp): **Converts an integer to a hexadecimal string.**
    ```python
    # Example 1: Converting an integer to a hexadecimal string
    decimal_number = 255
    hexadecimal_string = hex(decimal_number)
    print(f"Hexadecimal representation of {decimal_number}: {hexadecimal_string}")
    # Output: Hexadecimal representation of 255: 0xff

    # Example 2: Converting a negative integer to a hexadecimal string
    negative_number = -42
    hex_negative = hex(negative_number)
    print(f"Hexadecimal representation of {negative_number}: {hex_negative}")
    # Output: Hexadecimal representation of -42: -0x2a

    # Example 3: Converting a floating-point number to a hexadecimal string
    float_number = 3.14
    hex_float = hex(int(float_number))
    print(f"Hexadecimal representation of {float_number}: {hex_float}")
    # Output: Hexadecimal representation of 3.14: 0x3

    # Example 4: Using hex() with different base
    number_base_8 = 0o17  # Octal representation
    hex_octal = hex(number_base_8)
    print(f"Hexadecimal representation of octal number {number_base_8}: {hex_octal}")
    # Output: Hexadecimal representation of octal number 15: 0xf

    # Example 5: Using hex() with complex numbers
    complex_number = 3 + 4j
    # hex(complex_number) will raise a TypeError since complex numbers cannot be converted to hexadecimal

    # Example 6: Using hex() with a custom class
    class CustomClass:
        def __init__(self, value):
            self.value = value

    custom_instance = CustomClass(42)
    # hex(custom_instance) will raise a TypeError since custom classes do not have a default conversion to hexadecimal
    ```
    Output:
    ```
    Hexadecimal representation of 255: 0xff
    Hexadecimal representation of -42: -0x2a
    Hexadecimal representation of 3.14: 0x3
    Hexadecimal representation of octal number 15: 0xf
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [list()](https://www.w3schools.com/python/ref_func_list.asp): **Creates a list.** 
    ```python
    # Creating a list from an iterable
    iterable_data = [1, 2, 3, 4, 5]
    list_from_iterable = list(iterable_data)
    print(f"List from iterable: {list_from_iterable}")

    # Creating an empty list
    empty_list = list()
    print(f"Empty list: {empty_list}")

    # Creating a list from a string
    string_data = "hello"
    list_from_string = list(string_data)
    print(f"List from string: {list_from_string}")

    # Creating a list from a tuple
    tuple_data = (6, 7, 8)
    list_from_tuple = list(tuple_data)
    print(f"List from tuple: {list_from_tuple}")

    # Creating a list from a range
    range_data = range(3)
    list_from_range = list(range_data)
    print(f"List from range: {list_from_range}")

    # Creating a list with repeated elements
    repeated_element = 0
    list_with_repeated_element = [repeated_element] * 4
    print(f"List with repeated element: {list_with_repeated_element}")
    ```
    Output:
    ```
    List from iterable: [1, 2, 3, 4, 5]
    Empty list: []
    List from string: ['h', 'e', 'l', 'l', 'o']
    List from tuple: [6, 7, 8]
    List from range: [0, 1, 2]
    List with repeated element: [0, 0, 0, 0]
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [memoryview()](https://www.w3schools.com/python/ref_func_memoryview.asp): **Returns a memory view object.**
    ```python
    # Creating a memory view from a bytes object
    bytes_data = b'Hello'
    memory_view_from_bytes = memoryview(bytes_data)
    print(f"Memory view from bytes: {memory_view_from_bytes}")

    # Creating a memory view from a bytearray object
    bytearray_data = bytearray(b'World')
    memory_view_from_bytearray = memoryview(bytearray_data)
    print(f"Memory view from bytearray: {memory_view_from_bytearray}")

    # Accessing elements using memory view
    print(f"First element from memory view: {memory_view_from_bytes[0]}")
    print(f"Last element from memory view: {memory_view_from_bytearray[-1]}")

    # Modifying elements using memory view
    memory_view_from_bytes[0] = 65  # ASCII code for 'A'
    print(f"Modified memory view from bytes: {memory_view_from_bytes.tobytes()}")
    ```
    Output:
    ```
    Memory view from bytes: <memory at 0x7f2e498f09c0>
    Memory view from bytearray: <memory at 0x7f2e498f0a00>
    First element from memory view: 72
    Last element from memory view: 100
    Modified memory view from bytes: b'Aello'
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [object()](https://www.w3schools.com/python/ref_func_object.asp): **Creates a new featureless object.** 
    ```python
    # Example 1: Creating a new object
    new_object = object()
    print(f"New object: {new_object}")

    # Example 2: Checking the type of the new object
    print(f"Type of new object: {type(new_object)}")

    # Example 3: Using isinstance to check if an object is an instance of the base object type
    print(f"Is new object an instance of base object type?: {isinstance(new_object, object)}")  # Returns True

    # Example 4: Creating another object and comparing their identities
    another_object = object()
    print(f"Are new object and another object distinct instances?: {new_object is another_object}")  # Returns False

    # Example 5: Using dir() to inspect the attributes and methods of the object
    print(f"Attributes and methods of new object: {dir(new_object)}")
    ```
    Output:
    ```
    New object: <object object at 0x7f6de2a8ca30>
    Type of new object: <class 'object'>
    Is new object an instance of base object type?: True
    Are new object and another object distinct instances?: False
    Attributes and methods of new object: ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [oct()](https://www.w3schools.com/python/ref_func_oct.asp): **Converts an integer to an octal string.** 
    ```python
    # Example 1: Converting an integer to an octal string
    num = 42
    octal_string = oct(num)
    print(f"Integer {num} in octal: {octal_string}")

    # Example 2: Converting another integer to an octal string
    another_num = 123
    another_octal_string = oct(another_num)
    print(f"Integer {another_num} in octal: {another_octal_string}")

    # Example 3: Converting a negative integer to an octal string
    negative_num = -10
    negative_octal_string = oct(negative_num)
    print(f"Negative integer {negative_num} in octal: {negative_octal_string}")
    ```
    Output:
    ```
    Integer 42 in octal: 0o52
    Integer 123 in octal: 0o173
    Negative integer -10 in octal: -0o12
    ```
    [⬆️ Go to top](#python-methodsfunctions)
- [ord()](https://www.w3schools.com/python/ref_func_ord.asp): **Returns the Unicode code point for a given character.** 
    ```python
    # Example 1: Getting the Unicode code point for the character 'A'
    unicode_A = ord('A')
    print(f"Unicode code point for 'A': {unicode_A}")

    # Example 2: Getting the Unicode code point for the character '€'
    unicode_euro = ord('€')
    print(f"Unicode code point for '€': {unicode_euro}")

    # Example 3: Getting the Unicode code point for the character '😊'
    unicode_smiley = ord('😊')
    print(f"Unicode code point for '😊': {unicode_smiley}")
    ```
    Output:
    ```
    Unicode code point for 'A': 65
    Unicode code point for '€': 8364
    Unicode code point for '😊': 128522
    ```
    _The `ord()` function returns an integer representing the Unicode code point of the character passed to it. In these examples, it returns the Unicode code points for the characters 'A', '€', and '😊'. Let me know if you need further explanation!_

    [⬆️ Go to top](#python-methodsfunctions)
- [set()](https://www.w3schools.com/python/ref_func_set.asp): **Creates a set.**
    ```python
    # Creating an empty set
    empty_set = set()
    print(f"Empty set: {empty_set}")

    # Creating a set from a list
    list_data = [1, 2, 3, 2, 1]
    set_from_list = set(list_data)
    print(f"Set from list: {set_from_list}")

    # Creating a set from a string
    string_data = "hello"
    set_from_string = set(string_data)
    print(f"Set from string: {set_from_string}")

    # Creating a set using curly braces
    set_with_braces = {1, 2, 3, 4}
    print(f"Set with curly braces: {set_with_braces}")

    # Adding elements to a set
    my_set = {1, 2, 3}
    my_set.add(4)
    print(f"Set after adding an element: {my_set}")

    # Removing elements from a set
    my_set.remove(3)
    print(f"Set after removing an element: {my_set}")

    # Discarding an element that may or may not be in the set
    my_set.discard(5)  # No error if 5 is not in the set
    print(f"Set after discarding an element: {my_set}")

    # Set operations (union, intersection, difference)
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}

    union_result = set_a | set_b  # Union
    intersection_result = set_a & set_b  # Intersection
    difference_result = set_a - set_b  # Difference

    print(f"Union of {set_a} and {set_b}: {union_result}")
    print(f"Intersection of {set_a} and {set_b}: {intersection_result}")
    print(f"Difference of {set_a} and {set_b}: {difference_result}")
    ```
    Output:
    ```
    Empty set: set()
    Set from list: {1, 2, 3}
    Set from string: {'h', 'o', 'e', 'l'}
    Set with curly braces: {1, 2, 3, 4}
    Set after adding an element: {1, 2, 3, 4}
    Set after removing an element: {1, 2, 4}
    Set after discarding an element: {1, 2, 4}
    Union of {1, 2, 3} and {3, 4, 5}: {1, 2, 3, 4, 5}
    Intersection of {1, 2, 3} and {3, 4, 5}: {3}
    Difference of {1, 2, 3} and {3, 4, 5}: {1, 2}
    ```
    _The `set()` function is versatile and allows you to create sets in various ways, which is useful for operations involving collections of unique elements._

    [⬆️ Go to top](#python-methodsfunctions)
- [slice()](https://www.w3schools.com/python/ref_func_slice.asp): **Creates a slice object.** 
    ```python
    # Creating a list
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Creating a slice object
    my_slice = slice(2, 7)

    # Using the slice object to get a subset of the list
    sliced_list = my_list[my_slice]
    print(f"Sliced list using slice(2, 7): {sliced_list}")

    # Creating a slice object with a step
    step_slice = slice(1, 8, 2)

    # Using the slice object to get a subset of the list
    sliced_list_with_step = my_list[step_slice]
    print(f"Sliced list using slice(1, 8, 2): {sliced_list_with_step}")

    # Creating a string
    my_string = "Hello, World!"

    # Creating a slice object
    string_slice = slice(7, 12)

    # Using the slice object to get a subset of the string
    sliced_string = my_string[string_slice]
    print(f"Sliced string using slice(7, 12): '{sliced_string}'")

    # Creating a slice object with negative indices
    negative_slice = slice(-5, -1)

    # Using the slice object to get a subset of the list
    sliced_list_negative = my_list[negative_slice]
    print(f"Sliced list using slice(-5, -1): {sliced_list_negative}")

    # Accessing the attributes of a slice object
    s = slice(2, 8, 2)
    print(f"Slice start: {s.start}")
    print(f"Slice stop: {s.stop}")
    print(f"Slice step: {s.step}")
    ```
    Output:
    ```
    Sliced list using slice(2, 7): [2, 3, 4, 5, 6]
    Sliced list using slice(1, 8, 2): [1, 3, 5, 7]
    Sliced string using slice(7, 12): 'World'
    Sliced list using slice(-5, -1): [5, 6, 7, 8]
    Slice start: 2
    Slice stop: 8
    Slice step: 2
    ```
    _The `slice()` function is useful for specifying a range of indices to extract subsets of sequences, providing a flexible way to work with parts of lists, tuples, strings, and other sequence types._

    [⬆️ Go to top](#python-methodsfunctions)
- [str()](https://www.w3schools.com/python/ref_func_str.asp): **Converts a value to a string.**
    ```python
    # Converting an integer to a string
    integer_value = 123
    string_value = str(integer_value)
    print(f"The string representation of {integer_value} is '{string_value}'")

    # Converting a float to a string
    float_value = 3.14159
    string_value = str(float_value)
    print(f"The string representation of {float_value} is '{string_value}'")

    # Converting a boolean to a string
    boolean_value = True
    string_value = str(boolean_value)
    print(f"The string representation of {boolean_value} is '{string_value}'")

    # Converting a list to a string
    list_value = [1, 2, 3, 4]
    string_value = str(list_value)
    print(f"The string representation of {list_value} is '{string_value}'")

    # Converting a dictionary to a string
    dict_value = {"name": "Alice", "age": 30}
    string_value = str(dict_value)
    print(f"The string representation of {dict_value} is '{string_value}'")

    # Using str() for concatenation
    name = "Bob"
    age = 25
    message = "Hello, my name is " + name + " and I am " + str(age) + " years old."
    print(message)
    ``` 
    Output:
    ```
    The string representation of 123 is '123'
    The string representation of 3.14159 is '3.14159'
    The string representation of True is 'True'
    The string representation of [1, 2, 3, 4] is '[1, 2, 3, 4]'
    The string representation of {'name': 'Alice', 'age': 30} is '{'name': 'Alice', 'age': 30}'
    The string representation of (3+4j) is '(3+4j)'
    Hello, my name is Bob and I am 25 years old.
    ```
    _The `str()` function is versatile and essential for converting different types of values to their string representations, which is especially useful in contexts where string manipulation or display is required._

    [⬆️ Go to top](#python-methodsfunctions)
- [tuple()](https://www.w3schools.com/python/ref_func_tuple.asp): **Creates a tuple.**
    ```python
    # Creating an empty tuple
    empty_tuple = tuple()
    print(f"Empty tuple: {empty_tuple}")

    # Creating a tuple from a list
    list_data = [1, 2, 3, 4]
    tuple_from_list = tuple(list_data)
    print(f"Tuple from list: {tuple_from_list}")

    # Creating a tuple from a string
    string_data = "hello"
    tuple_from_string = tuple(string_data)
    print(f"Tuple from string: {tuple_from_string}")

    # Creating a tuple with different data types
    mixed_tuple = (1, "hello", 3.14, True)
    print(f"Tuple with mixed data types: {mixed_tuple}")

    # Creating nested tuples
    nested_tuple = ((1, 2), (3, 4), (5, 6))
    print(f"Nested tuple: {nested_tuple}")

    # Creating a tuple directly using parentheses
    direct_tuple = (1, 2, 3, 4)
    print(f"Directly created tuple: {direct_tuple}")

    # Tuple unpacking
    a, b, c = (10, 20, 30)
    print(f"Unpacked values: a={a}, b={b}, c={c}")

    # Creating a single element tuple
    single_element_tuple = (42,)
    print(f"Single element tuple: {single_element_tuple}")
    ```
    Output:
    ```
    Empty tuple: ()
    Tuple from list: (1, 2, 3, 4)
    Tuple from string: ('h', 'e', 'l', 'l', 'o')
    Tuple with mixed data types: (1, 'hello', 3.14, True)
    Nested tuple: ((1, 2), (3, 4), (5, 6))
    Directly created tuple: (1, 2, 3, 4)
    Unpacked values: a=10, b=20, c=30
    Single element tuple: (42,)
    ```
    _The `tuple()` function is useful for creating immutable sequences, ensuring that the contained elements cannot be modified, which can be useful for maintaining data integrity in your programs._

    [⬆️ Go to top](#python-methodsfunctions)
### Iteration and Sequence Operations 
- [aiter()](https://docs.python.org/3/library/functions.html#aiter): **Returns an asynchronous iterator for an object.** 
    ```python
    # Example 1: Basic Usage of aiter()
    class AsyncIterable:
        def __init__(self, start, end):
            self.current = start
            self.end = end

        def __aiter__(self):
            return self

        async def __anext__(self):
            if self.current >= self.end:
                raise StopAsyncIteration
            self.current += 1
            return self.current - 1

    # Using aiter() to get an asynchronous iterator
    async def main():
        async_iterable = AsyncIterable(0, 5)
        async_iterator = aiter(async_iterable)
        async for value in async_iterator:
            print(value)

    # Running the asynchronous main function
    import asyncio
    asyncio.run(main())

    # Example 2: Using aiter() with an Asynchronous Generator
    async def async_generator():
        for i in range(5):
            yield i
            await asyncio.sleep(1)  # Simulate an async I/O-bound operation

    async def main():
        async_iterator = aiter(async_generator())
        async for value in async_iterator:
            print(value)

    # Running the asynchronous main function
    import asyncio
    asyncio.run(main())

    # Example 3: Using aiter() with Built-in Asynchronous Iterators
    import aiofiles

    async def read_file_async(file_path):
        async with aiofiles.open(file_path, mode='r') as f:
            async_iterator = aiter(f)
            async for line in async_iterator:
                print(line.strip())

    # Running the asynchronous read_file_async function
    import asyncio
    asyncio.run(read_file_async('example.txt'))
    ```
    Basic Usage:
    - We define an AsyncIterable class with __aiter__ and __anext__ methods to make it an asynchronous iterable.
    - The __aiter__ method returns self, making the class its own iterator.
    - The __anext__ method is defined with async and it yields values until the end condition is met, at which point it raises StopAsyncIteration.
    - In the main coroutine, aiter(async_iterable) is used to get the asynchronous iterator and async for is used to iterate over it.

    Asynchronous Generator:
    - An asynchronous generator function async_generator is defined using async def and yield.
    - The await asyncio.sleep(1) simulates an asynchronous I/O operation.
    - aiter(async_generator()) returns an asynchronous iterator, and async for iterates over it.

    Built-in Asynchronous Iterators:
    - Using aiofiles to read a file asynchronously, aiter(f) is used to obtain an asynchronous iterator from the file object.
    The async for loop iterates over each line in the file.
    
    Notes:
    - The aiter() function requires an object that implements the __aiter__ method, returning an asynchronous iterator.
    - Asynchronous iterators must implement the __anext__ method, which is a coroutine and should be awaited.
    - These examples use asyncio.run() to run the asynchronous main function, which is the recommended way to run asynchronous code in Python.
    _The `aiter()` function is essential for working with asynchronous iteration, especially when dealing with I/O-bound tasks that can benefit from concurrency._

    [⬆️ Go to top](#python-methodsfunctions)
- [anext()](https://docs.python.org/3/library/functions.html#anext): **Retrieves the next item from an asynchronous iterator.** 
    ```python
    # Example 1: Using anext() with a Custom Asynchronous Iterator
    class AsyncIterable:
        def __init__(self, start, end):
            self.current = start
            self.end = end

        def __aiter__(self):
            return self

        async def __anext__(self):
            if self.current >= self.end:
                raise StopAsyncIteration
            self.current += 1
            return self.current - 1

    # Using anext() to get the next item from the asynchronous iterator
    async def main():
        async_iterable = AsyncIterable(0, 5)
        async_iterator = aiter(async_iterable)
        
        try:
            while True:
                value = await anext(async_iterator)
                print(value)
        except StopAsyncIteration:
            print("Iteration complete.")

    # Running the asynchronous main function
    import asyncio
    asyncio.run(main())

    # Example 2: Using anext() with an Asynchronous Generator
    async def async_generator():
        for i in range(5):
            yield i
            await asyncio.sleep(1)  # Simulate an async I/O-bound operation

    async def main():
        async_iterator = aiter(async_generator())
        
        try:
            while True:
                value = await anext(async_iterator)
                print(value)
        except StopAsyncIteration:
            print("Iteration complete.")

    # Running the asynchronous main function
    import asyncio
    asyncio.run(main())
    ```
    Custom Asynchronous Iterator:
    - An AsyncIterable class is defined with __aiter__ and __anext__ methods to make it an asynchronous iterable.
    - The __aiter__ method returns self, making the class its own iterator.
    - The __anext__ method is defined with async and it yields values until the end condition is met, at which point it raises StopAsyncIteration.
    - In the main coroutine, aiter(async_iterable) is used to get the asynchronous iterator, and anext(async_iterator) is awaited to retrieve the next item. This continues in a loop until StopAsyncIteration is raised.

    Asynchronous Generator:
    - An asynchronous generator function async_generator is defined using async def and yield.
    - The await asyncio.sleep(1) simulates an asynchronous I/O operation.
    - In the main coroutine, aiter(async_generator()) is used to get the asynchronous iterator, and anext(async_iterator) is awaited to retrieve the next item. This continues in a loop until StopAsyncIteration is raised.

    Notes:
    - The anext() function is used to retrieve the next item from an asynchronous iterator. It must be awaited because it is an asynchronous operation.
    - If the iterator is exhausted, anext() raises a StopAsyncIteration exception, which should be handled to end the iteration gracefully.
    - Using anext() directly allows for fine-grained control over asynchronous iteration, which can be useful in scenarios where you need to process elements individually and handle exceptions or perform specific actions between iterations.
    _The anext() function is essential for working with asynchronous iterators, providing a way to manually retrieve the next item in an asynchronous loop._

    [⬆️ Go to top](#python-methodsfunctions)
- [enumerate()](https://www.w3schools.com/python/ref_func_enumerate.asp): **Returns an enumerate object with a counter.**
    ```python
    # Example 1: Basic Usage of enumerate() with a List
    # Creating a list
    fruits = ['apple', 'banana', 'cherry']

    # Using enumerate() to get an enumerate object
    enumerate_fruits = enumerate(fruits)

    # Converting to a list of tuples for display
    enumerate_list = list(enumerate_fruits)
    print(f"Enumerate object as list of tuples: {enumerate_list}")

    # Iterating over the enumerate object
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Fruit: {fruit}")

    # Example 2: Using enumerate() with a Starting Index
    # Creating a list
    colors = ['red', 'green', 'blue']

    # Using enumerate() with a starting index of 1
    enumerate_colors = enumerate(colors, start=1)

    # Converting to a list of tuples for display
    enumerate_list = list(enumerate_colors)
    print(f"Enumerate object with start=1 as list of tuples: {enumerate_list}")

    # Iterating over the enumerate object with a starting index
    for index, color in enumerate(colors, start=1):
        print(f"Index: {index}, Color: {color}")

    # Example 3: Using enumerate() with a String
    # Creating a string
    text = "hello"

    # Using enumerate() with a string
    enumerate_text = enumerate(text)

    # Converting to a list of tuples for display
    enumerate_list = list(enumerate_text)
    print(f"Enumerate object from string as list of tuples: {enumerate_list}")

    # Iterating over the enumerate object
    for index, char in enumerate(text):
        print(f"Index: {index}, Character: {char}")

    # Example 4: Using enumerate() with a Dictionary
    # Creating a dictionary
    student_grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}

    # Using enumerate() with a dictionary
    enumerate_grades = enumerate(student_grades.items())

    # Converting to a list of tuples for display
    enumerate_list = list(enumerate_grades)
    print(f"Enumerate object from dictionary items as list of tuples: {enumerate_list}")

    # Iterating over the enumerate object
    for index, (student, grade) in enumerate(student_grades.items()):
        print(f"Index: {index}, Student: {student}, Grade: {grade}")
    ```
    Output:
    ```
    Enumerate object as list of tuples: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
    Index: 0, Fruit: apple
    Index: 1, Fruit: banana
    Index: 2, Fruit: cherry

    Enumerate object with start=1 as list of tuples: [(1, 'red'), (2, 'green'), (3, 'blue')]
    Index: 1, Color: red
    Index: 2, Color: green
    Index: 3, Color: blue

    Enumerate object from string as list of tuples: [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
    Index: 0, Character: h
    Index: 1, Character: e
    Index: 2, Character: l
    Index: 3, Character: l
    Index: 4, Character: o

    Enumerate object from dictionary items as list of tuples: [(0, ('Alice', 'A')), (1, ('Bob', 'B')), (2, ('Charlie', 'C'))]
    Index: 0, Student: Alice, Grade: A
    Index: 1, Student: Bob, Grade: B
    Index: 2, Student: Charlie, Grade: C
    ```
    _The enumerate() function is a powerful tool for iterating over an iterable with a counter, making it easier to track the position of elements within the iterable._

    [⬆️ Go to top](#python-methodsfunctions)
- filter(): Constructs an iterator from elements of an iterable for which a function returns true. 
- iter(): Returns an iterator for an object. 
- len(): Returns the length of an object. 
- map(): Applies a function to all items in an iterable. 
- next(): Retrieves the next item from an iterator. 
- range(): Generates a sequence of numbers. 
- reversed(): Returns a reverse iterator. 
- zip(): Aggregates elements from two or more iterables.
### Attribute and Object Handling 
- callable(): Checks if an object is callable. 
- delattr(): Deletes an attribute from an object. 
- dir(): Returns a list of valid attributes for an object. 
- getattr(): Returns the value of a named attribute of an object. 
- hasattr(): Checks if an object has a specified attribute. 
- setattr(): Sets an attribute on an object to a specified value. 
- isinstance(): Checks if an object is an instance of a specified class or tuple of classes. 
- issubclass(): Checks if a class is a subclass of another class or tuple of classes. 
- property(): Returns a property attribute. 
- staticmethod(): Returns a static method for a function. 
- super(): Returns a temporary object of the superclass that allows access to its methods. 
- type(): Returns the type of an object or creates a new type.
### Input/Output Operations 
- input(): Reads a line from input. 
- print(): Prints objects to the text stream or another specified stream. 
- open(): Opens a file and returns a file object.
### String Operations 
- ascii(): Returns a string representation of an object with non-ASCII characters escaped. 
- format(): Formats a string using a format string. 
- repr(): Returns a string representation of an object that can be used to recreate the object.
### Evaluation and Execution 
- compile(): Compiles source code into a code object that can be executed by exec() or eval(). 
- eval(): Evaluates a given expression in the context of global and local variables. 
- exec(): Executes dynamically created Python code.
### Utility Functions 
- all(): Returns True if all elements of an iterable are true. 
- any(): Returns True if any element of an iterable is true. 
- breakpoint(): Drops into the debugger at the call site. 
- globals(): Returns a dictionary representing the current global symbol table. 
- hash(): Returns the hash value of an object. 
- help(): Invokes the built-in help system. 
- id(): Returns the unique identifier for an object. 
- locals(): Updates and returns a dictionary representing the current local symbol table. 
- vars(): Returns the __dict__ attribute of an object, if it has one.