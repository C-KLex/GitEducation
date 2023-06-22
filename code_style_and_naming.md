# Coding style guideline

## General guideline
### Whitespace
#### 1. Avoid extraneous whitespace in the following situations
    Immediately inside parentheses or braces:
    Immediately before a comma, semicolon, or colon:
    Immediately before the open parenthesis that starts the argument list of a function call:
    One space around an assignment (or other) operator to align it with another:

#### 2. Others
    Separating any reserved word starting a conditional or switch statement (such as if, guard, while, or switch) from the expression that follows it if that expression starts with an open parenthesis '('.
    Use a space before any closing curly brace '}' that follows code on the same line, before any open curly brace '{', and after any open curly brace '{' that is followed by code on the same line.
    Space on both sides of any binary or ternary operator, including the “operator-like” symbols described below, with exceptions (dot and range expressions)

### Vertical whitespace
#### 1. A single blank line appears in the following locations:
    Between consecutive members of a type: properties, initializers, methods, enum cases, and nested types, except that:
    A blank line is optional between two consecutive stored properties or two enum cases whose declarations fit entirely on a single line. Such blank lines can be used to create logical groupings of these declarations.
    A blank line is optional between two extremely closely related properties that do not otherwise meet the criterion above; for example, a private stored property and a related public computed property.
    Only as needed between statements to organize code into logical subsections.
    Optionally before the first member or after the last member of a type (neither is encouraged nor discouraged).
    Anywhere explicitly required by other sections of this document.

#### 2. Multiple blank lines are permitted, but never required (nor encouraged). If you do use multiple consecutive blank lines, do so consistently throughout your code base.

### Parentheses
    Parentheses are not used around the top-most expression that follows an if, guard, while, or switch keyword.

### Braces
    There is no line break before the opening brace '{'.

    There is a line break after the opening brace '{', except
        in closures, where the signature of the closure is placed on the same line as the curly brace, if it fits, and a line break follows the in keyword.
        where it may be omitted as described in one statement per line.

```guard let value = value else { return 0 }```

        empty blocks may be written as {}.

    There is a line break before the closing brace '}', except where it may be omitted as described in one statement per line, or it completes an empty block.

    There is a line break after the closing brace '}', if and only if that brace terminates a statement or the body of a declaration. For example, an else block is written } else { with both braces on the same line.

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

### Others


# Naming convention
    It is important that naming should only include alphabetic & numerical characters!! In addition, naming should be as short and meaningful as possible. Make sure to keep it short and in an easily understandable format. The following are the naming conventions.

    Files: PascalCase
    Files that belongs to other files: ParentFile_ChildrenFile
    Class: PascalCase
    Function: camelCase
    Variables: camelCase
    Dates: YYYYMMDD
    Versions: xxx001, xxx002
