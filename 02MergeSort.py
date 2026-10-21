def Merge(low, mid, high):
    h = low 
    j = mid+1
    b = []

    while h<= mid and j<= high:
        if(a[h] <= a[j]):
            b.append(a[h])
            h += 1
        
        else:
            b.append(a[j])
            j += 1

    while h <= mid:
        b.append(a[h])
        h += 1
    
    while j <= high:
        b.append(a[j])
        j += 1

    for i in range(len(b)):
        a[low+i] = b[i]


def MergeSort(low, high):

    if(low<high):
        mid = ( low + high ) // 2
        MergeSort( low, mid)
        MergeSort( mid+1, high)
        Merge( low, mid, high)

n = int(input("Enter no. of elements\n"))
a = []

for i in range(n):
    a.append(int(input(f"Enter element {i} :")))

MergeSort(0,n-1)
print("Sorted array: ", a)