def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        i=0
        j=0
        k=0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k]= leftHalf[i]
                i=i+1
            else:
                alist[k]=rightHalf[j]
                j=j+1
            k=k+1
        while i < len(leftHalf):
            alist[k]=leftHalf[i]
            i=i+1
            k=k+1
        while j < len(rightHalf):
            alist[k]=rightHalf[j]
            j=j+1
            k=k+1
alist = [11,22,55,44,77,66,44,33,88]
mergeSort(alist)
print(alist)