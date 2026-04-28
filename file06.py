def main(data:str):
    a=open(data,"r")
    n=a.read()
    ls=n.split("\n")
    m=[]
    for i in ls:
        m+=[len(i)]
    return m
print(main("data/data06.txt"))