def lower_alpha(word):
    return all(char.islower() for char in word)

word = list(input())

if lower_alpha(word) and word == word[::-1] and 1 <= len(word) <= 100:
    print(1)
else:
    print(0)
