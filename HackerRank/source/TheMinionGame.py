def check_alpha(sub_string):
    if sub_string.startswith("A") or sub_string.startswith("I") or sub_string.startswith("O") or sub_string.startswith("U") or sub_string.startswith("E"):
        return True
    else:
        return False


def count_sub_strings(sub, string):
    counter = 0
    for i in range(len(string)-len(sub)+1):
        help_string = ""
        for j in range(i, len(string)):
            help_string += string[j]
        if help_string.startswith(sub):
            counter += 1
    return counter


def minion_game(string):
    stuard_score = 0
    kevin_score = 0
    counted_sub_string = {""}
    sub_string = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            sub_string += string[j]
            if check_alpha(sub_string) and sub_string not in counted_sub_string:
                kevin_score += count_sub_strings(sub_string, string)
                #print(f"Kevin-{kevin_score}-added-{string.count(sub_string)} - string - {sub_string} ")
                counted_sub_string.add(sub_string)
            elif not check_alpha(sub_string) and sub_string not in counted_sub_string:
                stuard_score += count_sub_strings(sub_string, string)
                #print(f"Stuard-{stuard_score}-added-{string.count(sub_string)} - string - {sub_string}  ")
                counted_sub_string.add(sub_string)

        sub_string = ""

    print(f"Kevin {kevin_score}: Stuard {stuard_score}")
    if stuard_score > kevin_score:
        print(f"Stuard {stuard_score}")
    elif stuard_score < kevin_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
