# **Documentation Guideline**

## 1️⃣ **Write commit**

```bash
git commit -m "label: this is a commit summary" -m "this is a commit description (optional)" 
```

Commit Message Style: all **lowercase** letters

*Label Reference*:

- feat – a new feature is introduced with the changes
- fix – a bug fix has occurred
- chore – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
- eg: chore: update xxx to latest version
- refactor – refactored code that neither fixes a bug nor adds a feature
- docs – updates to documentation such as a the README or other markdown files
- style – changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
- test – including new or correcting previous tests
- perf – performance improvements
- build – changes that affect the build system or external dependencies
- revert – reverts a previous commit

----

## 2️⃣ **Code comment(.py)**

### *Template for the python script*

```python
"""
Module/Package/Script Name
=========================

Module/Package/Script description goes here.

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
        method2(args): Description of method2.
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
        Method description goes here.

        """
        pass

def my_function(arg1, arg2):
    """
    Function description goes here.

    Args:
        arg1 (type): Description of arg1.
        arg2 (type): Description of arg2.

    Returns:
        type: Description of the return value.
    """
    # Function implementation
    pass

```

----
## 3️⃣ **Document(.md)**

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
  
----  
