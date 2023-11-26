t = int(input())
for _ in range(t):
    v = int(input())
    votes = {}
    for _ in range(v):
        
        
        n = int(input())
        
        if n in votes:
            votes[n] += 1
        else:
            votes[n] = 1


    max_v = max(votes.values())
    most_p = [n for n, count in votes.items() if count == max_v]


    print(min(most_p))