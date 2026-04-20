def check_grammar(text):
    # if text checks if the text is empty or not
    # text evaluates to false if string is empty
    if text and text[0].isupper() and (text[-1] == "!" or text[-1] == "."):
        return True
    return False