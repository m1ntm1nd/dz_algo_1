def main():
    n, m = list(map(int, input().split()))
    mat = [[0]*n for i in range(n)]
    for _ in range(m):
        i, j = list(map(int, input().split()))
        mat[i-1][j-1] = 1
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=' ')
        print()

if __name__ == '__main__':
    main() 