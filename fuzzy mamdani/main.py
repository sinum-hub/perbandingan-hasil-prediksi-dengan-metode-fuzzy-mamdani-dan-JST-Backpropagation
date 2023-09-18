from functions import *
from system import FuzzyInferenceSystem
from defuzzification import *
from math import *

#Fuzzyfication

#Linguistic: Funding
inadequate = TrapezoidalFuzzyNumber(0, 0, 20, 31)
marginal = TriangularFuzzyNumber(20, 50, 80)
adequate = TrapezoidalFuzzyNumber(60, 78, 100, 100)

#Linguistic: Staffing
small = TrapezoidalFuzzyNumber(0, 0, 30, 56)
large = TrapezoidalFuzzyNumber(40, 60, 100, 100)

#Linguistic: Risk
low = TrapezoidalFuzzyNumber(0, 0, 35,40)
normal = TriangularFuzzyNumber(20, 50, 80)
high = TrapezoidalFuzzyNumber(60, 80, 100, 100)

#rules -> (Funding, Staff) --> Risk
rules = [
    (adequate , small, low),
    (adequate, large, low),
    (marginal, small, low),
    (marginal, large, normal),
    (inadequate, small, high),
    (inadequate, large, high)
]

if __name__ == '__main__':
    
    system = FuzzyInferenceSystem(rules)

    inputs = (25, 55)
    x,y = inputs
    print(inputs)

    #Mamdani
    print('---Mamdani------')
    result1 = system.call_aggregation(inputs, method='mamdani', typ='singleton')
    print("COA: " + str(round(COA(result1), 2)) + "% of risk")
    result2 = system.call_aggregation(inputs, method='mamdani', typ='singleton')
    print("BOA: " + str(round(BOA(result2), 2)) + "% of risk")
    result3 = system.call_aggregation(inputs, method='mamdani', typ='singleton')
    print("MOM: " + str(round(MOM(result3), 2)) + "% of risk")

    #Mamdani
    print('---Larsen------')
    result4 = system.call_aggregation(inputs, method='larsen', typ='singleton')
    print("COA: " + str(round(COA(result4), 2)) + "% of risk")
    result5 = system.call_aggregation(inputs, method='larsen', typ='singleton')
    print("BOA: " + str(round(BOA(result5), 2)) + "% of risk")
    result6 = system.call_aggregation(inputs, method='larsen', typ='singleton')
    print("MOM: " + str(round(MOM(result6), 2)) + "% of risk")