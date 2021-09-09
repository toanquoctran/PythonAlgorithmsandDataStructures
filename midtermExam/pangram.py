def pangramCheck(str):
    letters = []
    str = str.lower()
    for i in range(len(str)):
        letters.append(ord(str[i]))
    for i in range(97, 123):
        if i not in letters:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    str = input()
    if pangramCheck(str):
        print("YES")
    else:
        print("NO")