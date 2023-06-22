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
### Switch statements
### Enum cases
### Trailing commas
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