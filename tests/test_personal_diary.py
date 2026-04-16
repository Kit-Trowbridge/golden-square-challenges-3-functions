from lib.personal_diary import *

# given a string of "hello there", count_words() can split the string into 
# the words ["hello", "there"]

def test_count_words_can_identify_words():
    result = count_words("Hello there")   
    assert result == ["Hello", "there"]
