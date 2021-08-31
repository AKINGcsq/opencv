import bisect
while True:
    try:
        a,b = int(input(), map(int, input().split()))
        q = []
        for v in b:
            pos = bisect.bisect_left(q,v)
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))
    except:
        break

