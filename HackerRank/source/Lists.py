# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        list_command = input().split()
        if list_command[0] == "insert":
            my_list.insert(int(list_command[1]), int(list_command[2]))
        elif list_command[0] == "print":
            print(my_list)
        elif list_command[0] == "remove":
            my_list.remove(int(list_command[1]))
        elif list_command[0] == "append":
            my_list.append(int(list_command[1]))
        elif list_command[0] == "sort":
            my_list.sort()
        elif list_command[0] == "pop":
            my_list.pop()
        elif list_command[0] == "reverse":
            my_list.reverse()
