def main(data:str):
    a=open(data,"r")
    n=a.read()
    ls=[]
    ls.extend(n)
    return ls
print(main("data/data04.txt"))
