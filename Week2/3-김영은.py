#21608 상어초등학교
#https: // www.acmicpc.net/problem/21608


n = int(input()) 
student = n*n #학생수는 n*n 
seat = [[0]*n for _ in range(n)] #n*n 자리
preferences = [[] for _ in range(student+1)] #선호도 
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr = []
for _ in range(student): #학생수만큼 진행한다
    input = list(map(int,input().split()))  #학생/좋아하는 학생을 리스트로 입력받는다.
    like = input[1:]
    preferences[input[0]] = like #선호도배열의 인덱스를 학생의 번호로 사용, 배열의 인덱스에 좋아하는 학생 배열을 저장(추후 계산을 위해)
    if student == 0: #첫번째 순서의 학생의 경우
        seat[1][1] = input[0] #자리가 무조건 1,1임
        continue
    
    for x in range(n): #교실을 돌며 자리찾기 시작!
        for y in range(n):
            total_vacancy,total_like=0,0 #자리 주위의 공석과 좋아하는 사람 수 초기화
            for dx,dy in move:
                nx, ny = x + dx, y+dy
                if nx < 0 or nx > n-1 or ny<0 or ny>n-1: #nxn 교실의 범위 체크
                    continue
                if seat[nx][ny] in like: #자리에 있는 사람이 좋아하는 사람이면
                    total_like += 1 #라이크 1 추가
                if seat[nx][ny] == 0: #자리가 공석이면
                    total_vacancy +=1 #공석 1 추가
            arr.append((total_like,total_vacancy,(x,y))) 
    arr.sort(key=lambda x:(-x[0],-x[1],x[2])) #like값이 클수록, 같다면 vacancy값이 클수록, 같다면 행열의 번호가 작은 칸으로 정렬됨
    seat[arr[0][2][0]][arr[0][2][1]] = input[0]


answer = 0

for i in range(n): #교실순회
    for j in range(n):
        temp = 0
        for dx,dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx > n-1 or ny<0 or ny>n-1 : #nxn 교실의 범위 체크
                continue
            if seat[nx][ny] in preferences[seat[nx][ny]]: #
                temp +=1 
                continue
            if temp != 0:
                answer += (10 ** (temp-1))
                
                      
print(answer)           
    
    
