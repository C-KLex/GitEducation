# Coding style guideline

## General guideline
### Whitespace
1. No whitespace:
- inside parentheses, brackets, braces  (), [], {}
```python
# right
function1(var1, var2)
# wrong
function1( var1, var2 )
```
- before a comma, semicolon, colon  , ; :
```python
# right
function1(var1, var2)
# wrong
function1(var1,var2)
```
- before a open parenthese, bracket, brace which is a start of a function call
```python
# right
function1(var1, var2)
# wrong
function1 (var1, var2)
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

### Vertical whitespace
1. A single blank line appears when separating the logic of codes
```python
def function1():
    print("yoo")
    print("same funtion")

def function2():
    print("this is another function")
```
2. Multiple blank lines are permitted, but never required (nor encouraged). If you do use multiple consecutive blank lines, do so consistently throughout your code base

### Parentheses
1. Parentheses are not used around the top-most expression that follows an conditional statement
```python
# right
if x = 1:
# wrong
if (x = 1):
```

## Specific guideline

### Properties
    Use meaningful names for your properties that accurately describe their purpose. Follow the naming convention recommended by PEP8, which suggest using lowercase letters and underscores for property names (my_property instead of myProperty)

    In Python, properties are often implemented using the @property decorator. Place this decorator above the getter method to indicate that the method is accessed as a property rather than a regular method.

    Keep the naming consistent for the underlying private attribute associated with the property. Prefix it with an underscore (_) to indicate that it's intended to be private. This convention helps differentiate the property from the attribute itself.

    If a property is intended to be read-only, omit the setter method. This enforces immutability and signals that the property should not be modified directly.

    If a property needs to be writable, include a setter method using the @propertyname.setter decorator. This allows controlled modification of the property's value.

    In the setter method, you can add validation logic to ensure the assigned value meets certain criteria. Raise appropriate exceptions or handle errors gracefully to maintain code robustness.

    If a property is part of a public interface or class API, maintain backward compatibility by not changing its behavior or semantics without a good reason. Make sure the property follows the Principle of Least Astonishment.

### Switch statements
    Indent the body of the switch statement to improve readability. Use either a tab or four spaces or a tab for indentation. 
    
    Start each case label on a new line and indent it one level deeper than the switch statement. Additionally, align the case labels vertically for better readability.
    
    Use braces {} for all cases, even if they're not strictly necessary.
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
        
        Always include a default case to handle unexpected values. This case should clearly communicate how unexpected values are handled.

        Include a break statement at the end of each case to prevent fall-through to the next case. If fall-through is intentional, document it with a comment.     
        
### Enum cases
    Enum case names should be written in uppercase letters, following the convention of using uppercase for constants in Python.

    If an enum case name consists of multiple words, use underscores (_) to separate them.

    Consider ordering your enum cases in a logical or meaningful sequence. This can be alphabetical, numerical, or based on the importance or frequency of use. 

    Choose whether to use singular or plural naming for your enum cases based on the context and the nature of the values they represent.

    In general, avoid using abbreviations in enum case names unless they are widely recognized and well-understood within your project or domain.
    
### Trailing commas
    Include a trailing comma after the last element in a list or array. 

    Include a trailing comma after the last argument in a function call or definition.

    Do NOT include trailing commas in single-line constructs, as they add unnecessary visual clutter.



# Naming convention

    Files: PascalCase
    Files that belongs to other files: ParentFile_ChildrenFile
    Class: PascalCase
    Function: camelCase
    Variables: camelCase
    Dates: YYYYMMDD
    Versions: xxx001, xxx002
