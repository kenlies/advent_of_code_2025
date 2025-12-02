def solve():

    input = []
    dial = 50
    ans = 0

    with open("input.txt", "r") as file:
        for line in file:
            input.append(line)

        for i in input:
            if i[0] == "R":
                dial += int(i[1:])
            elif i[0] == "L":
                dial -= int(i[1:])
            dial = dial % 100
            if dial == 0:
                ans += 1

    print(ans)
    

if __name__ == "__main__":
    solve()
