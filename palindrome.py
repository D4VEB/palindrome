import re

def strip_text(text):
     match = re.sub(r"\W", "", text)
     stripped = match.lower()
     return stripped


def palindrome_test(backward, forward, word):
    if backward <= forward:
        return True
    if word[backward] != word[forward]:
        return False
    else:
        return palindrome_test(backward - 1, forward + 1, word)

def palindrome(string):

    string_to_test = strip_text(string)
    forward = 0
    backward = len(string_to_test) - 1

    return palindrome_test(backward, forward, string_to_test)