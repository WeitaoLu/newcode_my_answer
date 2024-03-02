#https://ac.nowcoder.com/acm/contest/11187/D
import sys
large = 998244353
line1 = sys.stdin.readline().split()
n = int(line1[0])
x = int(line1[1])
y = int(line1[2])

edges = []
nodes = set()
for line in sys.stdin:
    line = line.split()
    edges.append((int(line[0]), int(line[1])))
    nodes.add(int(line[0]))
    nodes.add(int(line[1]))
#dp[cur][0/1][0/1]  
for edge in edges:
    if edge[1] in nodes:
        nodes.discard(edge[1])
root = nodes.pop()
dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n)]
G = [[] for _ in range(n + 1)]
for u, v in edges:
    G[u].append(v)
   # G[v].append(u)

dp = [[[0, 0] for _ in range(2)] for _ in range(n + 1)]

def DFS(cur, pre):
    dp[cur][0][0] = dp[cur][0][1] = x
    dp[cur][1][0] = y
    dp[cur][1][1] = y - 1

    for nxt in G[cur]:
        if nxt == pre:
            continue
        DFS(nxt, cur)
        
        dp[cur][0][0] *= (dp[nxt][1][0] + dp[nxt][0][0]) % large
        dp[cur][0][0]
        dp[cur][1][0] *= (dp[nxt][0][1] + dp[nxt][1][1]) % large
        dp[cur][1][0] 
        dp[cur][0][1] *= (dp[nxt][1][0] + dp[nxt][0][0]) % large
        dp[cur][0][1] 
        dp[cur][1][1] *= (dp[nxt][0][1] + dp[nxt][1][1]) % large
        dp[cur][1][1] 
 
DFS(root, 0)
result = (dp[root][0][0] + dp[root][1][0]) % large
print(result)
