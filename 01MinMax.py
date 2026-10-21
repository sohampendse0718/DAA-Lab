def MinMax(i,j,min,max):
    if( i == j):
        min[0] = max[0] = a[i]

    elif ( i == j-1):
        if( a[i] > a[j]):
            max[0] = a[i]
            min[0] = a[j]
        else:
            max[0] = a[j]
            min[0] = a[i]
    
    else:

        mid = (i+j)//2

        MinMax(i,mid,min,max)
        min1 = [0]
        max1 = [0]

        MinMax(mid+1,j,min1,max1)

        if(max1[0] > max[0]):
            max[0] = max1[0]

        if(min1[0] < min[0]):
            min[0] = min1[0]

a = []
n = int(input("Enter no. of elements\n"))
for i in range(n):
    a.append(int(input(f"Enter element {i}: ")))

min = [0]
max = [0]

MinMax(0,n-1,min,max)
print("Maximum = ", max[0])
print("Minimum = ", min[0])