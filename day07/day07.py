def solve():

    ans = 0
    input = []
    pos = []

    with open("input.txt", "r") as file:
        for line in file:
            row = []
            for i, char in enumerate(line.strip()):
                row.append(char)
                if char == "S":
                    pos = [i, 0]
            input.append(row)

        def check(pos):
            nonlocal ans
            if pos[1] == len(input) - 1:
                return
            if input[pos[1]][pos[0]] == "^":
                ans += 1
                pos_l = pos.copy()
                pos_r = pos.copy()
                pos_l[0] -= 1
                pos_r[0] += 1
                check(pos_l)
                check(pos_r)
            elif input[pos[1]][pos[0]] == ".":
                input[pos[1]][pos[0]] = "|"
                pos[1] += 1
                check(pos)

        pos[1] += 1 
        check(pos)

        print(ans)
                

if __name__ == "__main__":
    solve()
