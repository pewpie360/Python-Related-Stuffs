User = input("Put a word or a number: ")
#print(User.lower())
#slicing it and add negative one to reverse the word or num
change = User[::-1]

#pali = "madam", "121", "racecar"
#for User in pali:
    if User in range(0, 2):
        print("this is palindrome")
        break
    else:
        print("This is not a palindrome")


