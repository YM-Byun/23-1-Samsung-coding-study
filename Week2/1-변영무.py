UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

directions = ["null", (-1, 0), (1, 0), (0, -1), (0, 1)]


class Shark:
    def __init__(self):
        self.id = 0
        self.direction = 0
        self.location = (0, 0)
        self.priority = {UP: [], DOWN: [], LEFT: [], RIGHT: []}

    def move_to_empty(self, smell_map, N):
        for p_index in self.priority[self.direction]:
            dr, dc = directions[p_index]
            nr, nc = dr + self.location[0], dc + self.location[1]

            if 0 <= nr < N and 0 <= nc < N:
                if smell_map[nr][nc] == 0:
                    self.location = (nr, nc)
                    self.direction = p_index
                    return True

    def move_to_mine(self, smell_map, N):
        for p_index in self.priority[self.direction]:
            dr, dc = directions[p_index]
            nr, nc = dr + self.location[0], dc + self.location[1]

            if 0 <= nr < N and 0 <= nc < N:
                if type(smell_map[nr][nc]) is tuple and smell_map[nr][nc][0] == self.id:
                    self.location = (nr, nc)
                    self.direction = p_index
                    return True

    def move(self, smell_map, N):
        moved = self.move_to_empty(smell_map, N)
        if not moved:
            self.move_to_mine(smell_map, N)


def remove_shark(sharks):
    location = set()
    new_shark = []
    count = 0

    for shark in sharks:
        if shark.location in location:
            continue
        else:
            new_shark.append(shark)
            count += 1
            location.add(shark.location)

    return new_shark, count


def decrease_smell(smell_map, N):
    for row in range(N):
        for col in range(N):
            if type(smell_map[row][col]) is tuple:
                id, smell = smell_map[row][col]
                if smell == 1:
                    smell_map[row][col] = 0
                else:
                    smell_map[row][col] = (id, smell - 1)


def mark_smell(smell_map, sharks, k):
    for shark in sharks:
        r, c = shark.location
        smell_map[r][c] = (shark.id, k)


if __name__ == "__main__":
    N, M, k = map(int, input().split(" "))
    smell_map = []
    sharks = [Shark() for _ in range(M)]

    ''' Init smell map and shark  '''
    for row in range(N):
        column = list(map(int, input().split(" ")))

        for column_index in range(len(column)):
            if column[column_index] != 0:
                shark_id = column[column_index]
                sharks[shark_id - 1].id = shark_id
                sharks[shark_id - 1].location = (row, column_index)
                column[column_index] = (shark_id, k)
        smell_map.append(column)

    ''' Init direction '''
    init_direction = list(map(int, input().split(" ")))
    for direction_index in range(M):
        sharks[direction_index].direction = init_direction[direction_index]

    ''' Get priority '''
    for shark in sharks:
        shark.priority[UP] = list(map(int, input().split(" ")))
        shark.priority[DOWN] = list(map(int, input().split(" ")))
        shark.priority[LEFT] = list(map(int, input().split(" ")))
        shark.priority[RIGHT] = list(map(int, input().split(" ")))

    for time in range(1, 1001):
        for shark in sharks:
            shark.move(smell_map, N)

        sharks, shark_count = remove_shark(sharks)
        decrease_smell(smell_map, N)
        mark_smell(smell_map, sharks, k)

        if shark_count == 1:
            print(time)
            break
    else:
        print("-1")
