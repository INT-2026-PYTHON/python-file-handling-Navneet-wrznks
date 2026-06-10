"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
with open("file_reading_practice/sowpods.txt") as file:
    text = file.read()
    words = text.splitlines()
    vowels = set('aeiou')
    words_with_all_vowels = []
    
    for word in words:
        lower_word = word.lower()
        if all(vowel in lower_word for vowel in vowels):
            words_with_all_vowels.append(word)
    print("Words with all vowels:")
    for w in words_with_all_vowels:
        print(w)
    print(f"Total words with all vowels: {len(words_with_all_vowels)}")

