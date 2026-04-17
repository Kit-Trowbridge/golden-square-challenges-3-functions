# Reading Time Estimator Function Design Recipe

## 1. Describe the Problem

_As a user_
_So that I can manage my time_
_I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text):
    """Determines the number of minutes it will take a user to read a text, with the formula of 200 words per minute.

    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way--in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.")

    Returns: (state the return value and its type)
        an integer representing the estimated number of minutes it will take the user
        to read the given text
        (e.g. 5)

    Side effects:
        This function doesn't print anything or have any other side-effects
    """
    pass 

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string
It returns 0
"""
estimate_reading_time("") => 0

"""
Given a string of exactly 200 words
It returns 1
"""
estimate_reading_time("-->string containing 200 words with no punctuation<--") => 1

"""
Given a string of exactly 400 words
It returns 2
"""
estimate_reading_time("-->string containing 400 words<--") => 2

"""
Given a None value
It throws an error
"""
estimate_reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
