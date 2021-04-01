import numpy as np
n = 100
def DivideRow(A, B, row, divider):
    if divider != 0:
        A[row,] /= divider
        B[row,0] /= divider
        #A[row] = [a / divider for a in A[row]]
    #print("\n",A)
        
def SwapRows(A, B, row1, row2):
    A[[row1,row2]] = A[[row2,row1]]
    B[[row1,0]] = B[[row2,0]]
    #print("\n",A)
    
def CombineRows(A, B, row, destination_row, weight):
    for i in range(n):
        A[destination_row,i] += weight*A[row,i]
    B[destination_row,0] += weight*B[row,0]
    #print("\n",A)

def matrix_to_triangle_view(A,B):
    for i in range(n):
        maximum = A[i,i]
        maxstr = i
        for j in range(i+1,n):
            if maximum < A[j,i]: 
                maxstr = j
        if maxstr != i:
            SwapRows(A,B,i,maxstr)
        DivideRow(A,B,maxstr,A[maxstr][i])
        for j in range(i+1,n):
            if A[j][i] != 0:
                DivideRow(A,B,j,A[j][i])
                CombineRows(A,B,maxstr,j,-1)
        
def matrix_reversed_solving(A,B):
    ANS = [B[n-1,0]/A[n-1,n-1]]
    cnt = 0
    #print(B[n-1,0],A[n-1,n-1],ANS)
    for i in range(n-2,-1,-1):
        partial_sum = 0
        t = 0
        for j in range(n-1,n-(len(ANS)+1),-1):
            partial_sum += A[i][j] * ANS[t]
            t += 1
        b1 = B[i,0]
        delim = A[i][j-1]
        ANS.append((B[i,0]-partial_sum)/A[i][j-1])
        cnt += 1
    #lost = (B[0,0]-partial_sum-ANS[len(ANS)-1]*A[0,1])/A[0][0]  #баг - непонятно, почему теряется одно значение
    #ANS.append(lost)
    return np.flipud(np.array(ANS))


def Gaussian_method(A,B):
    matrix_to_triangle_view(A,B)
    return matrix_reversed_solving(A,B)

def main():
    A = np.zeros((n-1,n),dtype=np.float)
    for i in range(1,n-1):
        A[i][i-1] = 1
        A[i][i] = 10
        A[i][i+1] = 1
    A[0][0] = 10
    A[0][1] = 1
    A = np.vstack((A,np.ones(n)))
    #print(A.shape)
    f = np.zeros((n,1))
    for i in range(n):
        f[i][0] = i+1
    matrix_to_triangle_view(A,f)
    print(A)
    print(np.linalg.solve(A,f).reshape(1,n))
    print(Gaussian_method(A,f))

if __name__ == "__main__":
    main()


