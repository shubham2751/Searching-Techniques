def Linear_Search(l, n, key):

    for i in range(n):

        if l[i] == key:
            return i

    return -1


n = int(input())

l = [int(input()) for i in range(n)]

key = int(input())

ans = Linear_Search(l, n, key)

print(ans)
