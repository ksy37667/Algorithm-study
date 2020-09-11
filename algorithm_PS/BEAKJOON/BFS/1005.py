import sys
T = int(sys.stdin.readline())
results = []

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    R = []
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        R.append([X, Y])
    W = int(sys.stdin.readline())

    # 잔여 시간 정보
    operating_map = {}
    for building, time in enumerate(D):
        operating_map[building+1] = time

    # 각 건물의 선행 건물에 대한 정보
    rule_map = {}
    for i in range(N):
        rule_map[i+1] = set()
    for rule in R:
        X = rule[0]
        Y = rule[1]
        rule_map[Y].add(X)

    # 완성된 건물
    done = set()
    time = 0
    
    # 목표 건물 W 가 완료된 건물에 포함될 때까지,
    while W not in done:
        # 건설 진행 중인 건물들
        bases = []
        for building in rule_map:
            # 잔여 건물 중, 선행 건물들이 모두 완료되었을 경우 건설 중인 건물에 추가.
            if done.issuperset(rule_map[building]) and building not in done: 
                bases.append(building)
        
        # 건설 중인 건물 중 잔여 최소 시간 계산 후, 총 시간(time)에 더함.
        time_step = min([operating_map[base] for base in bases])
        time += time_step

        # 건설 잔여 시간 갱신
        for base in bases:
            operating_map[base] -= time_step
            # 잔여 시간이 0일 경우 done에 추가
            if operating_map[base] == 0:
                done.add(base)

    results.append(time)

for result in results:
    sys.stdout.write(str(result)+'\n')