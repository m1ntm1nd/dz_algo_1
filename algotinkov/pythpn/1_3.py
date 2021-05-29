def main():
    x, y = list ( map ( int , input () . split () ) )
    lngs = [[]for _ in range(x)]
    allang = []
    for i in range(x):
        lngs[i] = list ( map ( int , input () . split () ) )[1:]
        allang += lngs[i]
        allang = list(set(allang))
    cnt = 0
    for i in range(len(lngs)):
        if len(lngs[i]) == 0:
            cnt += 1
    y = len(allang)
    base = []
    for k in range(len(lngs)):
        base.append(lngs[k].copy())
        b = lngs[k].copy()
        for i in range(len(lngs)):
            for j in range(len(lngs[i])):
                if lngs[i][j] in b:
                        b+= lngs[i]
                        b = list(set(b))
                        base[k] = b
                        break
    t = []
   
    base.sort(key= lambda x: len(x),reverse=True)
    for i in range(len(base)):
        tn = list(set(base[i]+t))
        if tn != t:
            cnt += 1
            t = tn

    print(cnt-1)

if __name__ == '__main__':
    main()