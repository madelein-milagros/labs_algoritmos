#ejercicio 2-----   4(palimdrome)
def is_palimdrome(s):
    s = s.lower().replace(' ', '')
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palimdrome(s[1:-1])
print(is_palimdrome("A man a plan a canal Panama"))
print(is_palimdrome("Able was I ere I saw Elba"))   
print(is_palimdrome("Hello")) 
