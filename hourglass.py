def hourglassSum(arr):
    max = 0
    s=[]
    for i in range(len(arr)-2):
        for j in range(len(arr) - 2):
            s.append(arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1] + arr[i][j]+ arr[i+1][j-1]+ arr[i+1][j]+arr[i+1][j+1])
    return max(s)
