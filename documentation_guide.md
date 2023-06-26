# **Documentation Guideline**

## **Code comment(.py)**

When to use different types of comments in Python:

1. Triple-quoted string comments (""" """):
   - Use them for class, function, and script explanations.
   - Provides detailed descriptions of classes, methods, functions, and their arguments.

2. Single-line comments (#):
   - Keep single-line comments concise and to the point.
   - Use them to explain specific lines of code, clarify complex logic, or provide additional context.
   - have one line space above #
   - place above the code it refer to

### *Template for the python script:*

```python
"""
Module/Package/Script name and brief description.

Author: [Your Name]
Date: [Script Create Date]
"""

class MyClass:
    """
    Class description goes here.

    Attributes:
        attr1 (type): Description of attr1.
        attr2 (type): Description of attr2.

    Methods:
        method1(args): Description of method1.
    
    class_method()
        Description of the class method.
    """

    def __init__(self, arg1, arg2):
        """
        Constructor description goes here.

        Args:
            arg1 (type): Description of arg1.
            arg2 (type): Description of arg2.
        """
        self.attr1 = arg1
        self.attr2 = arg2

    def method1(self, arg):
        """
        Method description goes here.

        Args:
            arg (type): Description of arg.

        Returns:
            type: Description of the return value.
        """
        # Method implementation
        pass

    @classmethod
    def class_method(cls):
        """
        Perform a specific task.

        """
        pass

def funcion2(num1, num2):
    """
    function description goes here.

    Parameters:
        num1 (int): A number to be checked.
        num2 (int): A number to be checked.  
    """

    # Calculate the sum of two numbers
    x = num1 + num2
  
    # Check if the sum is even
    if x % 2 == 0:
        return True
    else:
        return False

```