def get_children(graph,v,n):
    ans = [0] * n

def dfs(v,c,used,graph):
    if used[v]:
        return
    used[v] = c
    l = get_children(graph,v)
    for index in range(len(l)):
        if not used[index] and graph[index]:
            dfs(index,c,used,graph)

def main():
    n, m = list(map(int, input().split()))
    mat = [[0]*n for i in range(n)]
    for _ in range(m):
        i, j = list(map(int, input().split()))
        mat[i-1][j-1] = 1
        mat[j-1][i-1] = 1
    used = [0] * n
    c = 1
    for i in range(len(used)):
        t = used[i]
        if t == 0:
            dfs(i,c,used,mat)
            c+=1
    ans = [[] for _ in range(c-1)]
    print(len(ans))    
    for i in range(len(used)):
        ans[used[i]-1].append(i+1)
    for x in ans:
        print(len(x))
        for y in x:
            print(y, end=' ')
        print()

if __name__ == '__main__':
    main()