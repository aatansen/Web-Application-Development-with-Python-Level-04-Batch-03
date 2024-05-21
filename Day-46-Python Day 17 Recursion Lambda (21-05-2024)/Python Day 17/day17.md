## Day 17 Topics
- Python Day 17
    - Recursion
    - Recursion problem
    - Lambda Intro

### Recursion
- Recursion - A function that can call itself
    ```python
    # recursion
    def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

    print("\n\nRecursion Example Results")
    tri_recursion(1)
    ```
- Recursion problem: sum of given number
    ```python
    # recursion problem: sum of given number
    def sum(num):
    if num>0:
        summation = num+sum(num-1)
    else:
        summation=0
    return summation
    print(sum(10))
    ```
- Lambda Intro
    ```python
    x = lambda a: a + 10
    print(x(5))

    x = lambda a,b: a + b
    print(x(5,10))
    ```
    - A small anonymous function
    - Can take any number of arguments, but can only have one expression