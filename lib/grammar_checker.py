def check_grammar(text):
    # if text checks that text is not empty string
    # because an empty string returns false (anything else -> True)
    if text and text[0].isupper():
        if "!" or "." in text:
            return True
    return False