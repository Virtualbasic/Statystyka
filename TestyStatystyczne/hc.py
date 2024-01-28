from Functions.StatisticsFunctions import arithmetic_average , standard_deviation , variance , critical_value
from math import  sqrt

def hc(x , p1 , p2 , alfa):
    s1 = arithmetic_average(p1)
    s2 = arithmetic_average(p2)
    v1 = variance(p1, s1)
    v2 = variance(p2, s2)
    l1 = len(p1)
    l2 = len(p2)
    testcase = float(((s1 - s2)/float(sqrt((l1*v1) + (l2 + v2))))*float(sqrt(((l1*l2)/(l1+l2))*(l1+l2-2))))
    ss = (l1 + l2 -2 )
    criticalvalue = critical_value(ss,alfa,1)
    wb = float(abs(testcase))
    if float(wb)> float(criticalvalue):
        print("NO")
    else:
        print("H0")