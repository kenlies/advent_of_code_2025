def solve():

    input = []
    ans = 0

    with open("input.txt", "r") as file:
        for line in file:
            input.append(line.strip())

        for bank in input:
            first_battery = 0
            for i, f_battery in enumerate(bank[:-1]):
                if int(f_battery) > first_battery:
                    second_battery = 0
                    first_battery = int(f_battery)
                for s_battery in (bank[i+1:]):
                    if int(s_battery) > second_battery:
                        second_battery = int(s_battery)
            ans += int(str(first_battery) + str(second_battery))

        print(ans)


if __name__ == "__main__":
    solve()
