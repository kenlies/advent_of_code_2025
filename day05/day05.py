def solve():

    fresh_ids = []
    available_ids = []
    ans = 0

    with open("input.txt", "r") as file:
        flag = True
        for line in file:
            if line[0] == "\n":
                flag = False
                continue
            if flag:
                fresh_ids.append(line.strip().split("-"))
            else:
                available_ids.append(line.strip())

        for a_id in available_ids:
            for f_id in fresh_ids:
                if int(f_id[0]) <= int(a_id) <= int(f_id[1]):
                    ans += 1
                    break

        print(ans)


if __name__ == "__main__":
    solve()
