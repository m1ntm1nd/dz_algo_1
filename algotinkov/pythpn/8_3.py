def dfs(v,used,graph):
    if used[v]:
        return
    used[v] = True
    for index in range(len(graph[v])):
        if not used[index] and graph[v][index]:
            dfs(index,used,graph)

def main():
    n, m = list(map(int, input().split()))
    mat = [[int(k) for k in input().split()]for i in range(n)]
    used = [False] * n
    dfs(m-1,used,mat)
    print(sum(used))

if __name__ == '__main__':
    main()