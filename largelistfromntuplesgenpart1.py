#Growth rate: approx. tetration level

j=2
while True:
    a=eval(str("[("+"{},"*(j-1)+"{}) for {} in range({})"+" for {} in range(1,{}+1)"*(j-1)+"]").format(*["v"+str(i) for i in range(j)],"v0",str(j+1),*["v"+str(i//2*3-i+1) for i in range(j*2-2)]))
    print(j)
    print(a)
    j=len(a)
