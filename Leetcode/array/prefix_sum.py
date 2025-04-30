
def prefix_sum(arr, i, j):
    """
        returns sum for the given range of index
    """
    
    if len(arr) == 0:
        return 0
    else:
        return sum(arr[i:j])
    
    
if __name__ == '__main__':
    arr = [2,4,6,7,8]
    i,j=3,5
    result = prefix_sum(arr, i, j) 
    print(f'prefix sum: {result}')