"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
def is_palindrome(word):
    return word == word[::-1]

with open("file_reading_practice/sowpods.txt") as file:
    text = file.read()
    words = text.splitlines()
    palindromes = []
    max_length = 0
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
            if len(word) > max_length:
                max_length = len(word)
    longest_palindromes = []
    for p in palindromes:
          if len(p) == max_length:
              longest_palindromes.append(p)
    print(f"Longest palindrome length: {max_length}")
    for p in longest_palindromes:
        print(p)

