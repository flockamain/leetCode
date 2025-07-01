word = "ere"
letters = list(word)
print(letters)

output=1

for i in range(len(letters)):
    if i == 0:
        print("skipping first letter")
    elif letters[i] == letters[i - 1]:
        output += 1
    print("Current letter: " + letters[i] + str(output))
if output == len(letters) + 1:
    output -= 1

print("Number of consecutive letters: " + str(output))