from collections import Counter

def check_anagram(s1,s2):
    """
        check weather string is anagram or not
    """
    if len(s1) != len(s2):
        return 'no'
    if Counter(s1) == Counter(s2):
        return "yes"
    else:
        return "no"
    
def check_anagram2(s1,s2):
    
    if sorted(s1) == sorted(s2):
        return 'yes'
    else:
        return 'no'
    
    
if __name__ == '__main__':
    s1 = 'aba'
    s2 = 'aab'
    result = check_anagram(s1,s2)
    print( result)
    result = check_anagram2(s1,s2)
    print( result)
    
    