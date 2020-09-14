def rotate_word(word, rotation):
    """ A basic Caesar cypher. Takes a string (word) and an integer
    (rotation). Each character in the word is shifted by the rotation
    number to create a new word.
    """
    
    word_codes = [ord(letter) for letter in word]
    
    for i in range(len(word_codes)):
        if word_codes[i] in range(97, 123):
            word_codes[i] += rotation
            
            if word_codes[i] < 97:
                word_codes[i] += 26
            
            elif word_codes[i] > 123:
                word_codes[i] -= 26
        
        elif word_codes[i] in range(65, 91):
            word_codes[i] += rotation

            if word_codes[i] < 65:
                word_codes[i] += 26
            
            elif word_codes[i] > 91:
                word_codes[i] -= 26
 
    return "".join([chr(i) for i in word_codes])



print(rotate_word("jung gur", -13))