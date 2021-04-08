"""
SOLVING
"""
_inf = -100000

def main():
    S = input()
    #S = wwoow
    #1 - w
    #2 - ww
    #3 - wwo
    #4 - wo
    #5 - wo
    #dp_w = 0
    #dp_wo = 0
    #dp_wow = 0
    dp_w, dp_wo, dp_wow = 0, 0, 0
    for i in range(len(S)):
        if i > 0 and S[i] == 'v' and S[i-1] == 'v':
            dp_w += 1
            dp_wow += dp_wo
        if S[i] == 'o':
            dp_wo += dp_w

    print(dp_wow)    
if __name__ == '__main__':
    main() 