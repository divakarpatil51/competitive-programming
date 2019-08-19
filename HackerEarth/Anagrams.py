# Anagrams: Anagram of a word is formed by rearranging the letters of the word.
# e.g ABC --> CBA, CAB, BCA,ACB etc


def get_letters_to_be_deleted(str1, str2):
    if len(str1) == 0 or len(str2) == 0 or str1 == str2:
        return 0
    for letter in str1:
        if str2.count(letter) != 0:
            str1 = str1.replace(letter, "", 1)
            str2 = str2.replace(letter, "", 1)
    return len(str1) + len(str2)


if __name__ == "__main__":
    for each in range(0, int(input())):
        print(get_letters_to_be_deleted(input(), input()))
