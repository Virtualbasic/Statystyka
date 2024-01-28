def read_data(path):
    from  decimal import  Decimal
    def renotation(num):
        side = num.split("e")
        side = Decimal(side[0])*pow(10, Decimal(side[1]))
        return  float(side)
    populationv1 = []
    populationv2 = []
    with open(path, "r") as specdata:
        for i in specdata:
            i = i.replace('\n',"")
            sides = i.split(",")
            populationv1.append(renotation(sides[0]))
            populationv2.append(renotation(sides[1]))
        specdata.close()
    return [populationv1, populationv2]