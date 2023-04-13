def merge_the_tools(string, k):
    ListSubStrings = []
    for i in range(0, len(string), k):
        ListSubStrings.append(string[i:i+k])
    for i in ListSubStrings:
        unique_str = ""
        for char in i:
            if char not in unique_str:
                unique_str += char
        print(unique_str)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
