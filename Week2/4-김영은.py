#20055 컨베이어벨트
#https: // www.acmicpc.net/problem/20055

from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
step = 0
#올리는 위치 q[0], 내리는 위치 q[n-1]

while(True):
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 #
    if sum(robot):  # 로봇이 존재할 때만 돈다.
        for i in range(n-2, -1, -1):
            # 현재 위치에 로봇이 있고, 다음 위치에 없고, 다음위치 벨트의 웨이트가 1이상
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
            robot[-1] = 0  # 마지막 로봇이 있다면 컨베이어 밑으로 내려줌 즉시 내려야함
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    step += 1
    if belt.count(0) >= k:
        break
print(step)





