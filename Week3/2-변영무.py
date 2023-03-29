from collections import deque


class Robot:
    def __init__(self):
        self.container = None


class Container:
    def __init__(self, durability):
        self.empty = True
        self.durability = durability
        self.robot = None
        self.prev = None
        self.next = None


def need_to_remove(robot, belt, N):
    return robot.container == belt[N - 1]


if __name__ == "__main__":
    belt = deque()
    N, K = map(int, input().split(" "))
    durability = list(map(int, input().split(" ")))

    for index in range(N * 2):
        new_container = Container(durability[index])

        if 0 < index:
            if index == N * 2 - 1:
                new_container.next = belt[0]
                belt[0].prev = new_container

            new_container.prev = belt[index - 1]
            belt[index - 1].next = new_container

        belt.append(new_container)

    robots = deque()

    step = 1
    exit = False
    while not exit:
        ' Step 1 '
        move_to_up = belt.pop()
        belt.appendleft(move_to_up)

        if not belt[N - 1].empty:
            deleted_robot = belt[N - 1].robot
            belt[N - 1].empty = True
            belt[N - 1].robot = None
            robots.remove(deleted_robot)

        ' Step2 '
        new_robots = deque()
        for r in robots:
            container = r.container
            if container.next.empty and container.next.durability > 0:
                container.empty = True
                container.robot = None

                container.next.empty = False
                container.next.durability -= 1
                container.next.robot = r

                r.container = container.next

                if r.container == belt[N - 1]:
                    belt[N - 1].empty = True
                    belt[N - 1].robot = None
                else:
                    new_robots.append(r)

            else:
                new_robots.append(r)

        robots = new_robots

        ' Step 3 '
        upload_container = belt[0]
        if upload_container.durability > 0 and upload_container.empty:
            new_robot = Robot()
            robots.append(new_robot)
            new_robot.container = upload_container
            upload_container.empty = False
            upload_container.durability -= 1
            upload_container.robot = new_robot

        ' End condition '
        empty_count = 0
        for container in belt:
            if container.durability == 0:
                empty_count += 1

            if empty_count >= K:
                print(step)
                exit = True
                break

        step += 1
