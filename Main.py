import matplotlib.pyplot as plt,tabulate
Data=[]
x_val =[]
y_val =[]
def f(x,y):
    return (x**2)+y

def euler(x,y,h,n):
    for i in range(n):
        y=y+h*f(x,y)
        y_val.append(y)
        x=x+h
        x_val.append(x)
    Data.append(x_val)
    Data.append(y_val)
    print('Result is : ',round(y,4))
x0=float(input("the value of x0: "))
y0=float(input("the value of y0: "))
h=float(input("the value of h: "))
n=int(input("number of output (which is equal to interval+1): "))

euler(x0,y0,h,n)

print(tabulate.tabulate(Data,tablefmt='fancy_grid'))

plt.title("Euler Method",color='lime')
plt.xlabel('x-axis',color='red')
plt.ylabel('y-axis',color='red')
plt.plot(x_val,y_val,color='deepskyblue',linewidth=1,marker='o',markersize=3,label='y value')
plt.legend()
plt.show()
