#20055 컨베이어벨트
#https: // www.acmicpc.net/problem/20055

from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split()))) 
robot = deque([0]*n) #벨트와 로봇의 회전을 쉽게 하기 위해 deque사용
step = 0
#올리는 위치 q[0], 내리는 위치 q[n-1]

while(True):
    belt.rotate(1) #벨트 회전
    robot.rotate(1) #로봇 회전
    robot[-1] = 0 #로봇이 내리는 위치에 있다면 즉시 내린다
    if sum(robot):  # 로봇이 존재할 때만 돈다
        for i in range(n-2, -1, -1):
            # 현재 위치에 로봇이 있고, 다음 위치에 없고, 다음위치 벨트의 웨이트가 1이상
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1 #로봇을 다음 위치로 옮긴다
                robot[i] = 0 #현재 위치 로봇을 없앤다
                belt[i+1] -= 1 #벨트 웨이트 -1
            robot[-1] = 0  # 로봇이 내리는 위치에 있다면 즉시 내린다
    if robot[0] == 0 and belt[0] >= 1: #올리는 위치에 로봇이 없고, 벨트의 웨이트가 1 이상이면
        robot[0] = 1 #로봇을 올린다
        belt[0] -= 1
    step += 1
    if belt.count(0) >= k: #내구도가 0인 칸의 개수가 0개 이상이라면 종료
        break
print(step)





