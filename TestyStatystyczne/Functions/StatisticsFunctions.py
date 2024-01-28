from math import sqrt
from scipy.stats import t
def arithmetic_average(data):
    length = len(data)
    sum = 0
    i=0
    while i < length:
        sum+=data[i]
        i+=1
    return sum/length


def median(data):
    data.sort()
    length = len(data)
    if length %2!=0:
        med = float(data[int((length+1)/2)])
    else:
        med = float(data[int(length/2)] + data[int((length/2)+1)]/2)
    return med

def test_range(data):
    data.sort()
    Trang = float(data[len(data) -1] - data[0])
    return Trang

def variance(data , mean):
    s2 = 0
    i = 0
    while i < len(data):
        difference = float(data[i]- mean)
        square = float(difference*difference)
        s2 += square
        i+=1
    return float(s2/len(data))

def standard_deviation(s2):
    return float(sqrt(s2))

def kwartyl_u(data , med):
    data.sort()
    handler = []
    i = 0
    while i < len(data):
        if data[i] > med:
            handler.append(data[i])
        i+=1
    return median(handler)

def kwartyl_d(data , med):
    data.sort()
    handler = []
    i = 0
    while i < len(data):
        if data[i] < med:
            handler.append(data[i])
        i+=1
    return median(handler)

def kwartyl_diffrence(kw1 , kw2):
    return float(kw2-kw1)

def moda(data):
    value = {}
    for i in data:
        if i in value:
            value[i]+=1
        else:
            value[i] = 1
    b = 0
    keyb = 0
    for key , val in value.items():
        if val >b:
            keyb = key
            b = val
    return  keyb

def critical_value(degree, alfa, two_sided_test ):
    if two_sided_test ==1:
        alfa = alfa/2
    value = t.ppf(1-alfa, degree)
    return value