"""essentially made up my own leetcode problem to avoid copilot sticking 
its silly little head in my learning.

Validate an email address. a string s is provided and is an example email address.
Validate if it has the following criteria:
-username all alphanumeric (aside from periods)
-periods cannot start or end a username, also no consecutive periods
-1 @ symbol after a username. No others in the email address
-domain is after the @ symbol. This can have periods, but again, same rules as username apply
-TLD (the ending - .com, .io, .gov, etc) TLD must be at least 2 characters long
-email address cannot end with a period
"""


#example of good working email
s = "alex.emailValidator@gmail.com"

def isLegitEmail(string):
    #all emails should be lowercase
    lowerCase = string.lower()
    print("lowercase: " + lowerCase)

    #check for spaces
    spaceTest = lowerCase.split(" ")
    if len(spaceTest) > 1:
        print("not valid")
        return False
    else:
        print("no spaces")

        #split at the @ symbol - there should only be one
    beforeAtSymbol = lowerCase.split("@")

        #there can be periods in the username, but no other non-alnum characters
    if beforeAtSymbol[0].replace('.', '').isalnum() == True:
        print("Username looks good")
        print(beforeAtSymbol[0])
    else:
        print("Username is not valid")
        return False
    
        #check for multiple @ symbols
    if len(beforeAtSymbol) == 2:
        print("only one @")
    else:
        print("more at symbols than would be valid")
        return False
    
        #check if there is a username and domain
    if beforeAtSymbol[0] == "" or beforeAtSymbol[1] == "":
        print("no username or domain")
        return False
    else:
        print("moving on")

        #verify there is at least a period after the @ symbol to start the TLD (.com, etc)
    domExtCheck = "."
    if domExtCheck not in beforeAtSymbol[1]:
        print("no period after @ symbol")
        return False
    
        #TLD must be over 1 character
    domainCheck = beforeAtSymbol[1].split(".")
    if len(domainCheck[-1]) < 2:
        print("the length of the extension is too short")
        return False
    
        #since domain check is the array of strings between the periods, periods are
        #ignored and we are now checking for only alnum characters
    for i in domainCheck:
        if i.isalnum() == False:
            print("invalid characters in domain")
            return False            
        else:
            print("good!")
            
        #check for period at the start of a username or at the end of a username
    if beforeAtSymbol[0].startswith('.') or beforeAtSymbol[0].endswith('.'):
        print("username cannot start or end with a period")
        return False

        #check after at symbol's periods - periods not allowed to start, end,
        #or be consecutive at this point
    periods = lowerCase.split(".")
    for period in periods:
        if period == "":
            print("empty domain or extension")
            return False
        else:
            continue
    return True

if isLegitEmail(s) == True:
    print("All Tests passed! Hooray!")