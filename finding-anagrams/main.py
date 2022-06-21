# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# find anaagrams in a list of words


def find_anagrams(word, anagram):
    # create a list of anagram and word
    word_list = list(word)
    anagram_list = list(anagram)

    # sort the list
    word_list.sort()
    anagram_list.sort()

    # trim whitespace
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    iteration_position = 0
    matches = True

    # check if the two lists are equal
    while iteration_position < len(word_list) and matches:
        if word_list[iteration_position] == anagram_list[iteration_position]:
            iteration_position += 1
        else:
            matches = False

    return matches
    
print(find_anagrams("below", "elbow"))
print(find_anagrams("hello", "check"))