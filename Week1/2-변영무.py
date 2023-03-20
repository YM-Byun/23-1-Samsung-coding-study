directions = ["null", (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def move_cloud_add_water(data_map, d, s, N, clouds):
    added_grid = list()
    cloud_map = [[0 for _ in range(N)] for _ in range(N)]

    for cloud in clouds:
        r, c = cloud
        new_r = (r + (directions[d][0] * s)) % N
        new_c = (c + (directions[d][1] * s)) % N

        added_grid.append((new_r, new_c))

        cloud_map[new_r][new_c] = -1

    for grid in added_grid:
        r, c = grid
        data_map[r][c] = data_map[r][c] + 1

    clouds.clear()

    return added_grid, cloud_map


def copy_water(data_map, N, added_grid):
    for grid in added_grid:
        r, c = grid
        count = 0

        for direction in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            nr, nc = r + direction[0], c + direction[1]

            if 0 <= nr < N and 0 <= nc < N:
                if data_map[nr][nc] > 0:
                    count += 1

        data_map[r][c] = data_map[r][c] + count


def generate_cloud(data_map, N, cloud_map, clouds):
    for row in range(N):
        for col in range(N):
            if data_map[row][col] >= 2 and cloud_map[row][col] != -1:
                clouds.append((row, col))
                data_map[row][col] = data_map[row][col] - 2


def count_water(data_map, N):
    count = 0
    for row in range(N):
        for col in range(N):
            count += data_map[row][col]

    return count


if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    data_map = list()

    for r in range(N):
        data_map.append(list(map(int, input().split(" "))))

    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    for c in range(M):
        d, s = list(map(int, input().split(" ")))
        added_grid, cloud_map = move_cloud_add_water(data_map, d, s, N, clouds)
        copy_water(data_map, N, added_grid)
        generate_cloud(data_map, N, cloud_map, clouds)

    print(count_water(data_map, N))
