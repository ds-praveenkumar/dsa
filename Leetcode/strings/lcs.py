
def lcs(s1, s2, m, n):
    """
        solving longest common subsequence using recursion
    """
    if m == 0 or n ==0:
        return 0
    elif s1[m-1] == s2[n-1]:
        return 1 +lcs(s1, s2 , m-1 , n-1)
    else:
        return max(lcs(s1,s2, m,n-1), lcs(s1,s2, m-1,n))
    
def lcs_dp(s1, s2):
    """
        Solving LCS with DP
    """
    m = len(s1)
    n = len(s2)
    if m == 0 or n==0:
        return 0
    
    mem = [[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j ==0:
                mem[i][j] = 0
                
            elif s1[i-1] == s2[j-1]:
                mem[i][j] = mem[i-1][j-1]+1
                
            else:
                mem[i][j] = max(mem[i-1][j], mem[i][j-1])
            print(mem)
                    
    return mem[m][n]        
if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print ("Length of LCS is ", lcs(X, Y, len(X), len(Y)))
    print ("Length of LCS is ", lcs_dp(X, Y))