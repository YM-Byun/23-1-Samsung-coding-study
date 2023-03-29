from heapq import heappush, heappop

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Student:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority
        self.location = (0, 0)


def find_loc(matrix, N, student):
    empty_seats = []

    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 0:
                like_count = 0
                empty_count = 0

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < N and 0 <= nc < N:
                        if matrix[nr][nc] in student.priority:
                            like_count += 1
                        elif matrix[nr][nc] == 0:
                            empty_count += 1

                heappush(empty_seats, (-like_count, -empty_count, row, col))

    _, _, r, c = heappop(empty_seats)
    matrix[r][c] = student.id
    student.location = (r, c)


def get_score(students, matrix, N):
    score = 0
    for student in students:
        r, c = student.location
        like_cnt = 0

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] in student.priority:
                    like_cnt += 1

        if like_cnt == 1:
            score += 1
        elif like_cnt == 2:
            score += 10
        elif like_cnt == 3:
            score += 100
        elif like_cnt == 4:
            score += 1000

    return score


if __name__ == "__main__":
    N = int(input())
    students = []
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(N ** 2):
        info = list(map(int, input().split(" ")))
        students.append(Student(info[0], {info[1]: False, info[2]: False, info[3]: False, info[4]: False}))

    for student in students:
        find_loc(matrix, N, student)

    print(get_score(students, matrix, N))
