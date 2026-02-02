# wap to input a name and check the characters in the name are vowels or not.
name = input("Enter a name:")
def vowels_in_name(nm):
    vowels = 'aeiouAEIOU'
    vowel_chars = [char for char in nm if char in vowels]
    return vowel_chars
vchars = vowels_in_name(name)
if vchars:
    print(f"The vowels in the name are: {', '.join(vchars)}")
else:
    print("There are no vowels in the name.")