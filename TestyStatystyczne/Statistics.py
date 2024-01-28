from Functions.read_data import read_data
from Functions.indicators import position_indicators_scattering
from ab import hab
from hc import hc
import random
import  matplotlib.pyplot as plt

def hist(p):
    plt.hist(p , bins=26, color = "green", edgecolor = "black")
    plt.xlabel("w1")
    plt.ylabel("hz")
    plt.title("proba")
    plt.show()


if __name__ == "__main__":
    def sp(data):
        handler = []
        i =0
        while i < len(data):
            selection = random.randint(0,1)
            if selection ==1:
                handler.append(data[i])
            i+=1
        return handler
    DATA  = read_data("6.csv")
    p_1_1 =  sp(DATA[0])
    p_1_2 =  sp(DATA[0])
    p_2_1 =  sp(DATA[1])
    p_2_2 =  sp(DATA[1])

    print("----test statystyczny dla próby 1 populacji 1")
    hist(p_1_1)
    position_indicators_scattering(p_1_1, "1", "1")
    u1 = int(input("x populacji"))
    print(f"Hipoteza A: H0:u1={u1}, H1:u1=/={u1}")
    hab(u1,p_1_1, 0.05)

    print("----test statystyczny dla próby 1 populacji 2")
    hist(p_2_1)
    position_indicators_scattering(p_1_2, "1", "2")
    u2 = int(input("x populacji"))
    print(f"Hipoteza A: H0:u1={u2}, H1:u1=/={u2}")
    hab(u1, p_2_1, 0.05)

    print("Hipoteza C: H0:u1-u2=/=0, H1: u1-u2=/=x")
    value = int(input("x"))
    hc(value,p_1_2, p_2_1,0.05)


    #-------------------------------------------------------------------------------------------------------------------
    print("----test statystyczny dla próby 2 populacji 1")
    hist(p_1_2)
    position_indicators_scattering(p_1_2, "2", "1")
    u1 = int(input("x populacji"))
    print(f"Hipoteza A: H0:u1={u1}, H1:u1=/={u1}")
    hab(u1, p_1_2, 0.05)

    print("----test statystyczny dla próby 2 populacji 2")
    hist(p_2_2)
    position_indicators_scattering(p_2_2, "2", "2")
    u2 = int(input("x populacji"))
    print(f"Hipoteza A: H0:u1={u2}, H1:u1=/={u2}")
    hab(u1, p_2_2, 0.05)

    print("Hipoteza C: H0:u1-u2=/=0, H1: u1-u2=/=x")
    value = int(input("x"))
    hc(value, p_1_2, p_2_2, 0.05)
