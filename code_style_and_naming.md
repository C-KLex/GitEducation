# Coding Style Guideline

## General Guideline

### Whitespace

1. No whitespace:

    - inside parentheses, brackets, braces  (), [], {}

        ```python
        # right
        def function1(var1, var2)
        # wrong
        def function1( var1, var2 )
        ```

    - before a comma, semicolon, colon  , ; :

        ```python
        # right
        def function1(var1, var2)
        # wrong
        def function1(var1,var2)
        ```

    - before a open parenthese, bracket, brace which is a start of a function call

        ```python
        # right
        def function1(var1, var2)
        # wrong
        def function1 (var1, var2)
        ```

2. One whitespace around:

    - an assignment operater

        ```python
        # right
        var1 = 0
        # wrong
        var1=0
        var1 =0
        var1= 0
        ```

    - reserved word starting a conditional statement with parentheses

        ```python
        # right
        if (x>1 & x<2):
        # wrong
        if(x>1 & x<2):
        ```

    - braces if follows codes in the same line

### Vertical Whitespace

1. A single blank line appears when separating the logic of codes

    ```python
    def function1():
        print("yoo")
        print("same funtion")
    # 1st blank line
    def function2():
        print("this is another function")
    ```

2.Multiple blank lines are permitted, but never required (nor encouraged). e.g. blanks between class

```python
class Class1:
    def __init__(self):
        print("this is initial function")
    
    def function1():
        print("this is function1 from class1")
# 1st blank line
# 2nd blank line
class Class2:
    def __init__(self):
        print("this is initial function")
    
    def function2():
        print("this is function2 from class2")
```

### Parentheses

1. Parentheses are not used around the top-most expression that follows an conditional statement

    ```python
    # right
    if x = 1:
    # wrong
    if (x = 1):
    ```

## Specific Guideline

### Properties

1. Use meaningful names for your properties that accurately describe their purpose. Follow the naming convention recommended by PEP8, which suggest using lowercase letters and underscores for property names (my_property instead of myProperty)

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None

        @property
        def my_property(self):
            return self._my_property
    ```

2. In Python, properties are often implemented using the @property decorator. Place this decorator above the getter method to indicate that the method is accessed as a property rather than a regular method.

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None

        @property
        def my_property(self):
            return self._my_property
    ```

3.Keep the naming consistent for the underlying private attribute associated with the property. Prefix it with an underscore (_) to indicate that it's intended to be private. This convention helps differentiate the property from the attribute itself.

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None
            
        @property
        def my_property(self):
            return self._my_property
    ```

4.If you want to allow setting the value of the property, define a setter method using the @property_name.setter decorator.

```python
class MyClass:
    def __init__(self):
        self._my_property = None

        @property
        def my_property(self):
            return self._my_property

    @my_property.setter
    def my_property(self, value):
        # Property setter logic
        self._my_property = value
```

5.If a property should be read-only, define only the getter method and omit the setter method.

    ```python
    class MyClass:
        def __init__(self):
            self._my_property = None

        @property
        def my_property(self):
            return self._my_property
    ```

### Switch Statements

1. Indent the body of the switch statement to improve readability. Use either a tab or four spaces or a tab for indentation.

2. Start each case label on a new line and indent it one level deeper than the switch statement. Align the case labels vertically for better readability. Additionally, use braces {} for all cases, even if they're not strictly necessary.

    ```python
    switch variable:
        case value1:
            {
                # code for value1
                break
            }
        case value2:
            {
                # code for value2
                break
            }
        case value3:
            {
                # code for value3
                break
            }
        default:
            {
                # code for all other cases
            }
    ```

4.Always include a default case to handle unexpected values. This case should clearly communicate how unexpected values are handled.

5.Include a break statement at the end of each case to prevent fall-through to the next case. If fall-through is intentional, document it with a comment.     

# Naming convention

- Package: Snake_Case (Uppercase Initial)
- Files: Snake_Case (Uppercase Initial)
- Class: Snake_Case (Uppercase Initial)
- Function: snake_case
- Variables: snake_case
- Dates: YYYYMMDD
- Versions: xxx001, xxx002
