'''
This program is designed to implement the rational knapsack greedy strategy
as well as the O-1 Knapsack dynamic strategy. It should read data from
testData.txt for the input unless specified by the user.
'''
global TEST
TEST = "testData.txt"

def grabFileName():
    print("Please enter a file name below. \n(**Note: Do not enter the" +
            " .txt file type, only enter the name)\n", end='')
    fileName = str(input("File name -> ")) + ".txt"
    return fileName

'''
This file takes in a file name and retrieves the data from that file. It
then parses the data and returns all of it from the file. This returns 4
values: n, weights, profits, capacity
Args:
    -fileName: file name entered by the user, defaults to testData.txt
'''
def storeData(fileName=TEST):
    file = open(fileName, 'r')
    data = ""
    
    # 1st line is size of problem
    n = int(file.readline())
    
    # 2nd Line is the weights
    temp = str(file.readline())
    weights = list()
    
    for val in temp:
        if val != ' ':
            data += val
        else:
            data.rstrip('\n')
            weights.append(int(data))
            data = ""
    
    # Have to store remaining data in weights
    data = data.rstrip('\n')
    weights.append(int(data))
    data = ""
    
    # 3rd line is the profits
    temp = str(file.readline())
    profits = list()
    for val in temp:
        if val != ' ':
            data += val
        else:
            #print(data, end=' ')
            data.rstrip('\n')
            #print(data, end=' ')
            profits.append(int(data))
            data = ""
    
    # Have to store remaining data in profits
    data = data.rstrip('\n')
    profits.append(int(data))

    # 4th line is the capacity
    apacity = int(file.readline())
    return n, weights, profits, capacity

'''
This function takes in the data from the file and applys the rational
knapsack greedy algorithm. It evaluates the proplem then returns the
total profit and the optimal solution.
    Args:
        - n: problem size
        - weights: array containing the weights
        - profits: array containing the profits, the profits elements
          should match up with the weights elements.
        - capacity: total memory to available in the knapsack
'''
def rationalKnapsack(n, weights, profits, capacity):
    Oi = list()
    for i in range(n):
        t = (profits[i] / weights[i])
        Oi.append((t, weights[i], profits[i]))
    
    Oi = sorted(Oi, reverse=True)
    M = capacity
    # Solution vector
    Xi = [ 0 for x in range(n) ]
    i = 0
    prof = 0
    while M > 0:
        if M >= Oi[i][1]:
            Xi[i] = 1
            M = M - Oi[i][1]
        else:
            Xi[i] = (M / Oi[i][1])
            break
        i += 1

    for x in range(n):
        prof = Oi[x][2] * Xi[x] + prof
    return prof, Xi

'''
This function performs the 0-1 Knapsack algorithm. It builds the graph
associated with the dynamic programming approach to the rational knapsack
and the maximum value should always be in the final position. It returns the
final solution and the solution graph.
    Args:
        -n: size of knapsack
        -weights: list of n weights in ascending order
        -profits: list of profits associated with each weight
        -capacity: total memory available for this knapsack
'''
def Knapsack_0_1(n, weights, profits, capacity):
    # Initializes x-axis
    solution = [ x for x in range(capacity + 1) ]

    # Adds an empty index
    solution = [ [' '] + solution ]

    # Initializes y-axis
    for x in range(n + 1):
        solution.append([x])
    for i in range(1, n + 2):
        wi = pi = i - 2
        for j in range(1, capacity + 2):
            if (solution[i][0] == 0):
                solution[i].append(0)
            else:
                if j <= weights[wi]:
                    solution[i].append(solution[i - 1][j])
                else:
                    val = max(profits[pi] + solution[i - 1][j - weights[wi]],
                                solution[i - 1][j])
                    solution[i].append(val)
    return solution, solution[n + 1][capacity + 1]

'''
This function performs an iterative approach to the traceback. It only tracks
one final profit in the knapsack and will not produce all possible combinations
but the solution produced is always optimal. It will return the solution vector
for the knapsack.
    Args:
        -solution: a 2D-array created in the Knapsack_0_1 function
        -fProfit: final profit from the solution
        -weights: list of weights in ascending order
        -capacity: memory available in this knapsack
'''
def traceback_01K(solution, fProfit, n, weights, capacity):
    i = n + 1
    j = capacity + 1
    wi = n - 1
    solVector = []
    while (solution[i][j] != 0):
        if (solution[i - 1][j] != solution[i][j]):
            j = j - weights[wi]
            solVector = [1] + solVector
        else:
            solVector = [0] + solVector
        i -= 1
        wi -= 1
    return solVector

'''
This function just calculates the total memory used out of the capacity.
    Args:
        -weights: weights in ascending order
        -solVector: solution vector from the traceback_01K function
'''
def calculateCapacity(weights, solVector):
    capacity = 0
    for i in range(len(solVector)):
        if solVector[i] == 1:
            capacity += weights[i]
    return capacity
