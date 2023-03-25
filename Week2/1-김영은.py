n,m,k = map(int,input().split())
position = [] #상어의 현재 위치
for _ in range(n):
    position.append(list(map(int,input().split())))

# shark 어따 저장할지
direction = list(map(int,input().split())) #상어의 현재 방향

priorities= [] #방향 우선순위 
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(tuple(map(int, input().split())))
    priorities.append(temp)

move = [(-1,0),(1,0),(0,-1),(0,1)]

smell = [[[0,0]] *n for _ in range(n)] #상어번호, 냄새 남은 시간 



def spread_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1]>0:
                smell[i][j][1] -= 1
            if position[i][j] != 0: #상어가 있는 곳 
                smell[i][j] = [position[i][j],k] #다시 스멜 가득 
                
        

def shark_move():
    arr = [[0]*n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if position[x][y] != 0:
                head = direction[position[x][y]-1] # head에 현재 x,y 좌표 상어의 방향을 가져온다
                found = False
                for i in priorities[position[x][y]-1][head-1]: #우선순위 좌표 획득 
                    nx = x +move[i-1][0]
                    ny = y + move[i-1][1]
                    if 0<=nx<n and 0<=ny <n:#범위체크
                        if smell[nx][ny][1] ==0: #no smell
                            direction[position[x][y]-1] = i #상어 방향 update
                            if arr[nx][ny] ==0:
                                arr[nx][ny]=position[x][y]
                            else:
                                arr[nx][ny] = min(position[x][y],arr[nx][ny])
                                found = True
                                break
                if found:
                    continue
    return arr
                
                    
            


def check_shark():
    for i in range(n):
        for j in range(n):
            if position[i][j]>1:
                return False
    return True        
                
                



for i in range(1,1000):
    spread_smell()
    position = shark_move()
    if(check_shark()):
        print(i)
        break
    

    
    
