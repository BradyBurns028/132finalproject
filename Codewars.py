def permute_a_palindrome(input): 
    
    isPalindrome = False
    letters = []
    for x in input:
        letters.append(x)
    
    numOfLetter = []
    for x in letters:
        n = letters.index(x)
        numOfLetter.append(letters.count(x))
    
    print(letters)
    print(numOfLetter)
    
    oddCounter = 0    
    for i in numOfLetter:
        print(i)
        if (i % 2 == 0):
            isPalindrome= True
        else: 
            oddCounter += 1
    
    if oddCounter > 1:
        isPalindrome = False
    return isPalindrome

def spin_words(sentence):

    words = sentence.split(" ")
    
    for w in words:
        if len(w) > 4:
            reversed = w[::-1]
            words[words.index(w)] = reversed
    
    return " ".join(words)


print(spin_words("I like cheeseburgers"))
