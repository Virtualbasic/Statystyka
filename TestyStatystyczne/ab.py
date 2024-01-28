from Functions.StatisticsFunctions import arithmetic_average , standard_deviation , variance , critical_value
from math import  sqrt
def hab(x , p , alfa):
    mean = arithmetic_average(p)
    sd = standard_deviation(variance(p, mean))
    testcase = float(((mean-float(x))/sd)*float(sqrt(len(p))))
    wbtestcase = float(abs(testcase))
    ss  = len(p) -1
    criticalvlue = critical_value(ss , alfa, 1)

    if float(wbtestcase) > float(criticalvlue):
        print("NO")
    else:
        print("H0")
