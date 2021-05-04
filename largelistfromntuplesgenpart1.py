#This code generates large lists of n-tuples of from v0 to v_(n) (v0>=v1>=v2>=...>=v_(n-1)>=v_(n)>=1)

j=2
while True:
    a=eval(str("[("+"{},"*(j-1)+"{}) for {} in range({})"+" for {} in range(1,{}+1)"*(j-1)+"]").format(*["v"+str(i) for i in range(j)],"v0",str(j+1),*["v"+str(i//2*3-i+1) for i in range(j*2-2)]))
    print(j)
    print(a)
    j=len(a)
