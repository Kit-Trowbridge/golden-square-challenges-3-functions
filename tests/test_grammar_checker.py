from lib.grammar_checker import *
"""
Given a blank text
It returns False
"""
def test_check_grammar_returns_false_for_empty_string():
    result = check_grammar("")
    assert result == False

"""
Given a single sentence text starting with a capital letter and ending with a period
It returns True
"""
def test_check_grammar_returns_true_for_single_sentence():
    result = check_grammar("Hello, world!")
    assert result == True