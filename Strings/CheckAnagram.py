s1 = input().replace(" ", "").lower()
s2 = input().replace(" ", "").lower()
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
