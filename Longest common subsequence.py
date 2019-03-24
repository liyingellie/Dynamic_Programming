# longest common subsequence
'''
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

optimal structure: the problem can be broken down into smaller, simple "subproblems"
overlapping subproblems: the solution to high-level subproblems often reuse lower level subproblems
'''

'''
1st property: if two sequences both end in the same element, shorten each sequence by removing
the last element

2nd property: if two sequences do not end in the same symbol, look for
max{LCS(Xn,Ym-1), LCS(Xn-1,Ym)}
'''

def lcs(x,y): #
    # create a memo
    memo = [[0 for i in range(0,len(y)+1)] for j in range(0,len(x)+1)]

    for i in range(0, len(x)+1):
        for j in range(0, len(y)+1):
            if x[i] == y[j]:
                if i == 0 or j == 0:
                    memo[i][j] = 0

                else:
                    memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i][j-1], memo[i-1][j])



    return memo[len(x),len(y)]


print(lcs("abcdaf", "acbcf"))