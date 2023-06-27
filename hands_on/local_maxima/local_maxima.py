def local_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    sort_x = sorted(x, reverse=True)
    list_original = x
    maximum = []
    index_m = []
    for i in range(2):
    	maximum.append(list_original.index(sort_x[i]))
    
    return maximum

maximum = local_maxima([1,3,-2,0,2,1])
print(maximum)

#maximum = local_maxima([-1,-1,0,-1])
#print(maximum)

#maximum = local_maxima([4,2,1,3,1,5])
#print(maximum)

#maximum = local_maxima([1,2,2,1])
#print(maximum)

#maximum = local_maxima([1,2,2,3,1])
#print(maximum)
