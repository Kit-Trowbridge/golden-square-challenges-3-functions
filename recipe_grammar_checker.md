# Grammar Checker Function Design Recipe

## 1. Describe the Problem

_As a user_
_So that I can improve my grammar_
_I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

# Do I want to check if every sentence does this? 
# Maybe come back to
# How to break a sentence up if it doesn't contain the punctuation
def check_grammar(text):
    """ Checks if a given text starts with a capital letter
        and ends with a "!" or "."

    Parameters: 
        text: a string

    Returns: 
        True or False boolean
       
    Side effects:
        None
    """
    pass 

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a blank text
It returns False
"""
check_grammar("") # => False

"""
Given a single sentence text starting with a capital letter and ending with a period
It returns True
"""
check_grammar("Hello, world!") # => True

"""
Given a single sentence text starting with a capital letter and without a sentence-ending punctuation mark
It returns False
"""
check_grammar("Hello, world") # => False

"""
Given a string of words with no capital letters or sentence ending punctuation
It returns False
"""
check_grammar("hello world") # => False

"""
Given a string containing multiple sentences, starting with a capital letter but not ending with a punctuation mark,
It returns False
"""
check_grammar("Hello world. It's nice to meet you") # => False

"""
Given a string containing multiple sentences, starting with a lowercase letter but ending with a punctuation mark,
It returns False
"""
check_grammar("hello world. It's nice to meet you.") # => False

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!
