def solve():

    final_ans = 0
    input = []

    with open("input.txt", "r") as file:
        for line in file:
            sdfa = line.strip().split(" ")
            sdfa = list(filter(("").__ne__, sdfa))
            input.append(sdfa)

        for col in zip(*input):
            ans = 0
            op = col[len(col) - 1]
            for val in col[:-1]:
                if op == "+":
                    ans += int(val)
                elif op == "*":
                    if ans == 0:
                        ans = 1
                    ans *= int(val)
            final_ans += ans
        
        print(final_ans)
                

if __name__ == "__main__":
    solve()
