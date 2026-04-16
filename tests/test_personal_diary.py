# A function called make_snippet that takes a string as an argument 
# and returns the first five words and then a '...' if there are more than that.

# Given a string, it returns a string
def test_make_snippet_returns_string():
    result = make_snippet("Hello")
    assert result == "Hello"