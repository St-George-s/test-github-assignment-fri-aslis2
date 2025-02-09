def upppercase(word):
    # Get ASCII value of first character
    firstChar = ord(word[0])
    if firstChar >= 97 and firstChar <=122:
        firstChar = firstChar - 32 
        word = (chr(firstChar) + word[1:])
    return word 

upppercase("asli")