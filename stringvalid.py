def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def is_alpha(s):
    return s.isalpha()