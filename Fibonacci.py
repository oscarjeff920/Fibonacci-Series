import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#This function generates the Fibbonacci Series, from intial terms and total number of terms
#Where the default series generated is the standard Fibbonacci series, with 20 terms
def Fibonacci_series(Term1 = 0, Term2 = 1, series_length = 20):
    while series_length > 100:
        series_length = int(input("The upper limit of allowed generated terms is 100.\n"
        "Please select a different number of terms generated.\n - "))
    while series_length < 2:
        series_length = int(input("The minimum number of generated terms is 2.\n"
        "Please select a different number of terms generated.\n - "))
        
    L = [Term1, Term2]
    for n in range(1, series_length):
        L.append(L[n] + L[n-1])
    return L

#This function is used to plot a generated fibonacci series
#The series needs to be edited a bit to generate the classic spiral

def Plot_Fib(series):
    plot = series

#The first changes are to edit the sign(+/-) of every other term 
    for n in range(len(series)):
        if n % 2 == 0:
            plot[n] *= -1
    print(plot, "\n")

#The second edit adds in 0 to the x and y coordinates so that a straight line isn't created
    coords = dict(x = plot.copy(), y = plot.copy())
    for n in range(2*len(series)):
        if n % 2 == 0:
            coords["x"].insert(n,0)
        else:
            coords["y"].insert(n,0)

    plt.plot(coords["x"], coords["y"])
    plt.show()

#This last function bundles the two previous ones together,
#to make the whole thing easliy executable 
def Fibonacci(Term1 = 0, Term2 = 1, series_length = 20):
    series = Fibonacci_series(Term1,Term2,series_length)
    Plot_Fib(series)

if __name__ == "__main__":
    Fibonacci()


