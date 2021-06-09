#anagram is when the two stringss can be written using the exact same letters
def anagram(s1,s2):
    s1=s1.replace(' ','').lower()
    s2=s2.replace(' ','').lower()
    return sorted(s1)==sorted(s2)
print(anagram('dog','god'))
print(anagram('my name is','Birhanu'))
