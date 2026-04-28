import string
def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open(data,"r")
    n=a.read()
    b=string.digits
    digit=[]
    for i in n:
        j=0
        while len(b)>j:
            if b[j]==i:
                digit+=[i]
            j+=1
    return digit
print(main("data/data03.txt"))

# Read data from file
