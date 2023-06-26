# **Documentation Guideline**

## 1️⃣ **Code comment(.py)**

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

----

## 2️⃣ **Document(.md)**

- ### **Function description**

  1. Briefly describe what the function does.
  2. List the parameters it accepts, including their names, types, and any constraints or requirements.
  3. Specify the return type of the function.
  - *template*:

    `calculate_average(numbers: List[float]) -> float`

    Calculates the average of a list of numbers.

    - **Parameters:**
      - `numbers` (List[float]): A list of floating-point numbers.

    - **Returns:**
      - `float`: The average value of the numbers.
    ----

- ### **Module description**
  
  1. Provide an overview of the module's purpose and functionality.
  2. Explain what the module is used for and how it can be helpful to users.
  3. Highlight the key features, functions, or classes provided by the module.

  - *template:*
  
      The `utils` module provides utility functions and classes for common tasks.

      **Functions:**
      - `validate_email(email: str) -> bool`: Validates if an email address is valid.
      - `generate_random_number() -> int`: Generates a random integer.

      **Classes:**
      - `FileHandler`: A class for handling file operations such as reading, writing, and file manipulation.

        ----

- ### **Package description**

    1. Describe the purpose and scope of the package. 
    2. Explain what the package offers, its main features, and how it can be beneficial to users. 
    3. Highlight the key modules or scripts included in the package.

    - *template:*
  
      The `data_processing` package provides a set of modules and scripts for data processing and analysis.

        **Modules:**
      - `preprocessing`: Contains functions for data preprocessing tasks such as cleaning, normalization, and feature engineering.
      - `analysis`: Implements various statistical and analytical methods for data analysis and visualization.
      - `modeling`: Includes classes and functions for building and evaluating predictive models.
  