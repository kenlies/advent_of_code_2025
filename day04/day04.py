def solve():

    input = []
    ans = 0

    def check_adjacent_rolls(x, y):
        rolls = 0
        directions = {
            (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)
        }
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(input) and 0 <= ny < len(input[nx]):
                if input[nx][ny] == "@":
                    rolls += 1
        if rolls < 4:
            return True
        return False

    with open("input.txt", "r") as file:
        for line in file:
            input.append(line.strip())
        
        for x, line in enumerate(input):
            for y, c in enumerate(line):
                if c == "@" and check_adjacent_rolls(x, y):
                    ans += 1

        print(ans)


if __name__ == "__main__":
    solve()
