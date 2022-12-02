"""
Set:
----
Louis hhas graduated from school and now wants to teach Zortans 
how to talk in English. But English is complicated, so lets try
to simplify it using Sets.

Set is all about being 'unique', it's very useful for certain operations.

Info:
-----
In a Set all values are nuique
"""

# --------------------------------------------------------------------------------------
# Louis wants to impress by showing some English magic, but Zortans are
# Confused, they want him to first show unique alphabets in his magic
# ----------------------------------------------------------------------------------------

magic_word = 'ahkadaejlakjdlksajfhdasfbasdfkajsd;lfajshdfjgasjkdfha'

unique_alphabet: set[str] = set(magic_word)
print(f"Unique Alphabets: {unique_alphabet}")

sentence = "the big blue sky and the big blue ocean"
unique_alphabets = set(sentence)
print(f"Unique Alphabets: {unique_alphabets}")

# What happens if we wnat to see list of unique words instead of alphabets
word_list = sentence.split(' ')
unique_words = set(word_list)
print(f"Unique Words in Sentence: {unique_words}")

# ----------------------------------------------------------------------------------------
# Zortans are impressed and they want to add more words to the set
# ----------------------------------------------------------------------------------------

unique_words.update(['this', 'can', 'me', 'Miclem'])

print(f"Unique Words in Sentence: {unique_words}")

# ----------------------------------------------------------------------------------------
# Zortans dont like the word Miclem
# ----------------------------------------------------------------------------------------

unique_words.remove('Miclem')
print(f"Unique Words in Sentence: {unique_words}")


"""
Read more about operations such as union, intersection, etc.
"""
