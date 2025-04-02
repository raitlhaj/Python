

def sum_dict(  d1,  d2):
    
    
    for k , v in d2.items():
        if(k in d1.keys()):
            d1[k]+= v
        else:
            d1[k]= v
    print(set(" Hello world!"))
    return d1


print(sum_dict({"H":2, "L" : 34}, {"H":2, "J" : 34} ))