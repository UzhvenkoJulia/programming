n = int(input())
kyky = list(map(int, input().split()))

u_m_set = set(abs(x) for x in kyky)

print(len(u_m_set))