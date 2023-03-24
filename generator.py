from scipy.stats import beta
import numpy as np

minBeta = 0.1
maxBeta = 10
alpha = 1
truncate = 2

def generate(n):
    arr = np.random.randint(2,size=(n,n))
    arr = arr.astype(np.float64)

    print('Unaltered random array: ')
    print(arr)
    print(f'Mean: {np.mean(arr)}')
    print(f'Standard deviation: {np.std(arr)}')
    for iteration in range (30): # number of times the array gets iterated through
        for (x,y), val in np.ndenumerate(arr):
            if val == 1: # minBeta case
                arr[x, y] = round(beta.rvs(alpha, minBeta), truncate)
            elif val == 0: # maxBeta case
                arr[x, y] = round(beta.rvs(alpha, maxBeta), truncate)
            else:
                # current value at arr[x, y] is set to the expected value of the beta distribution
                desiredBeta = (1 - val)/val
                arr[x, y] = round(beta.rvs(alpha, desiredBeta), truncate)
        print(f'Array at iteration {iteration}:')
        print(arr)
        print(f'Mean: {np.mean(arr)}')
        print(f'Standard deviation: {np.std(arr)}')

generate(8)