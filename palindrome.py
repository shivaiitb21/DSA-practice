def palindrome(text):
    # Base case - single or empty
    if len(text) <= 1:
        print("Palindrome")
    else:
        if text[0] == text[-1]:
            palindrome(text[1:-1])
        
        else:
            print("Not a palindrome")

palindrome("madam")
palindrome("malayalam")
palindrome("baby")

