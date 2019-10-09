# 二分查找

def binary_chop(alist, data):
    """
    非递归解决二分查找
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last+first)//2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False

def binary_chop2(alist, data):
    """
    递归解决二分查找
    """
    n = len(alist)
    if n < 1:
        return False
    mid = n // 2
    if alist[mid] > data:
        return binary_chop2(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_chop2(alist[mid+1:], data)
    else:
        return True

if __name__ == "__main__":
    lis = [2,4, 5, 12, 14, 23]

    print("非递归解决二分查找：%s" % str(binary_chop(lis, 23)))
    print("递归解决二分查找：%s" % str(binary_chop2(lis, 22)))
