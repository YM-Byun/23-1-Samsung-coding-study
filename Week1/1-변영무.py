PURIFIER = -1
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def diffusion(R, C, data_map):
    diffusion_map = [[0 for _ in range(C)] for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if data_map[row][col] != PURIFIER:
                moved_dust = 0

                for dr, dc in delta:
                    if 0 <= dr + row < R and 0 <= dc + col < C and data_map[dr + row][dc + col] != PURIFIER:
                        moving_dust = data_map[row][col] // 5
                        diffusion_map[dr + row][dc + col] += moving_dust
                        moved_dust += moving_dust

                diffusion_map[row][col] += data_map[row][col] - moved_dust
            else:
                diffusion_map[row][col] = PURIFIER

    return diffusion_map


def purifying(R, C, data_map, upper_purifier, lower_purifier):
    if upper_purifier != 0:
        ''' Top down '''
        for row in range(upper_purifier - 1, 0, -1):
            data_map[row][0] = data_map[row - 1][0]
        data_map[0][0] = data_map[0][1]

        ''' Top left '''
        for col in range(1, C - 1):
            data_map[0][col] = data_map[0][col + 1]
        data_map[0][C - 1] = data_map[1][C - 1]

        ''' Top up '''
        for row in range(1, upper_purifier):
            data_map[row][C - 1] = data_map[row + 1][C - 1]

    data_map[upper_purifier][C - 1] = data_map[upper_purifier][C - 2]

    ''' Top right '''
    for col in range(C - 2, 1, -1):
        data_map[upper_purifier][col] = data_map[upper_purifier][col - 1]
    data_map[upper_purifier][1] = 0

    if lower_purifier != R - 1:
        ''' Bottom up '''
        for row in range(lower_purifier + 1, R - 1):
            data_map[row][0] = data_map[row + 1][0]
        data_map[R - 1][0] = data_map[R - 1][1]

        ''' Bottom left '''
        for col in range(1, C - 1):
            data_map[R - 1][col] = data_map[R - 1][col + 1]
        data_map[R - 1][C - 1] = data_map[R - 2][C - 1]

        ''' Bottom down '''
        for row in range(R - 2, lower_purifier, -1):
            data_map[row][C - 1] = data_map[row - 1][C - 1]

    data_map[lower_purifier][C - 1] = data_map[lower_purifier][C - 2]

    ''' Bottom right '''
    for col in range(C - 2, 1, -1):
        data_map[lower_purifier][col] = data_map[lower_purifier][col - 1]
    data_map[lower_purifier][1] = 0


def find_air_purifier(R, data_map):
    upper = -1
    lower = -1

    for row in range(R):
        if data_map[row][0] == -1:
            upper = row
            lower = row + 1
            break
    return upper, lower


def get_dusts(R, C, data_map):
    dust = 0
    for row in range(R):
        for col in range(C):
            dust += data_map[row][col]
    return dust + 2


if __name__ == "__main__":
    R, C, T = map(int, list(input().split(" ")))
    data_map = []

    for r in range(R):
        data_map.append(list(map(int, list(input().split(" ")))))

    upper_purifier, lower_purifier = find_air_purifier(R, data_map)

    for test_case in range(T):
        data_map = diffusion(R, C, data_map)
        purifying(R, C, data_map, upper_purifier, lower_purifier)

    print(get_dusts(R, C, data_map))
