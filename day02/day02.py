import re

def solve(part):

    input = []
    ans = 0

    with open("input.txt", "r") as file:
        ranges = file.readline().split(",")
        for r in ranges:
            input.append(r.split("-"))

        for id_range in input:
            steps = int(id_range[1]) - int(id_range[0])
            for i in range(steps + 1):
                check = int(id_range[0]) + i
                if part == 1 and bool(re.fullmatch(r"(.+)\1", str(check))):
                    ans += check
                elif part == 2 and bool(re.fullmatch(r"(.+)\1+", str(check))):
                    ans += check

        print(ans)


if __name__ == "__main__":
    solve(1)
    solve(2)
