
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:],T[1:])))



def fast_MED(S, T, MED={}):
    # TODO -  implement memoization
    dp = [[0] * (len(S)+1) for _ in range(len(T)+1) ]
    for i in range(len(S)+1): dp[0][i] = i
    for i in range(len(T)+1): dp[i][0] = i
    
    for i in range(1,len(T)+1):
        for j in range(1, len(S)+1):
            if S[j-1] == T[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[-1][-1]

for case in test_cases:
    print(MED(case[0],case[1]), fast_MED(case[0],case[1]))

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    dp = [[0] * (len(S)+1) for _ in range(len(T)+1) ]
    for i in range(len(S)+1): dp[0][i] = i
    for i in range(len(T)+1): dp[i][0] = i
    allign_s = []
    allign_t = []
    for i in range(1,len(T)+1):
        for j in range(1, len(S)+1):
            if S[j-1] == T[i-1]:
                dp[i][j] = dp[i-1][j-1]
                allign_s.append(S[j-1])
                allign_t.append(S[j-1])
            else:             
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                mini = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                if mini == dp[i-1][j]:
                    allign_s.append('-')
                    allign_t.append(T[i-1])
                elif mini == dp[i][j-1]:
                    allign_s.append(S[i-1])
                    allign_t.append('-')


    return (''.join(allign_s), ''.join(allign_t))

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)

test_MED()                           
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        print(align_S, align_T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

test_align()
