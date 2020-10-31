def Binary_Search(l, i, j, key):

    if i <= j:

        mid = (i+j)//2

        if l[mid] == key:
            return mid

        elif key < l[mid]:
            return Binary_Search(l, i, mid-1, key)

        elif key > l[mid]:
            return Binary_Search(l, mid+1, j, key)

    return -1


def Binary_Search_ls(a, l, h, key):

    while l <= h:

        mid = (l+h)//2

        if key == a[mid]:
            return mid

        elif key < a[mid]:
            h = mid-1

        elif key > a[mid]:
            l = mid+1

    return -1


n = int(input())

l = [int(input()) for i in range(n)]

key = int(input())

ans = Binary_Search(l, 0, len(l)-1, key)  # recursion

print(ans)

ans = Binary_Search_ls(l, 0, len(l)-1, key)  # linear

print(ans)

# TIME COMPLEXITY ==> O(LOG N), BECAUSE WE DIVIDING THE LIST OR ARRAY BY N/2.
# SPACE COMPLEXITY ==> O(1), BECAUSE WE ARE NOT USING ANY EXTRA SPACE.
