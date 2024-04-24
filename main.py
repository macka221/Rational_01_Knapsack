import Rational_Knapsack_01_Knapsack as greedy
def __main__():
    pass
if __name__ == "__main__":
    file = greedy.grabFileName()
    if file != ".txt":
        n, weights, profits, capacity = greedy.storeData(file)
    else:
        n, weights, profits, capacity = greedy.storeData()
    profit1, solution1 = greedy.rationalKnapsack(n, weights,
                                                profits, capacity)
    solution2, profit2 = greedy.Knapsack_0_1(n, weights, profits,
                                            capacity)
    sVector = greedy.traceback_01K(solution2, profit2, n, weights, capacity)
    tCapacity = greedy.calculateCapacity(weights, sVector)
    print("Greedy Ration Knapsack:")
    print("-----------------------")
    print("Profit -> " + str(profit1))
    print("Solution vector -> ", end="")
    print(solution1)
    print("\n 0-1 Rational Knapsack:")
    print("-----------------------")
    for i in range(n + 2):
        print(" ", end="")
        print(solution2[i])
    print("Profit -> " + str(profit2))
    print("Solution -> " + str(sVector))
    print("Capacity used -> " + str(tCapacity))
