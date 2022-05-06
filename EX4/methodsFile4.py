# HomeWork_3
import sympy as sp
import math
from sympy import lambdify
eps = 0.0001


def Calculate_derivative(f):
    f_prime = f.diff(x)
    return f_prime


x = sp.symbols('x')


def error(start, end):
    upup = eps / (end - start)
    up = (-1) * math.log(upup, math.e)
    return (up // math.log(2, math.e)) + 1


def Bisection_Method(func, start, end):
    a = start
    b = end
    c = (a + b) / 2
    f = lambdify(x, func)
    counter = 0
    while abs(a - b) > eps:
        if counter > error(start, end):
            return "The function does not converge"
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
        c = (a + b) / 2
        counter += 1

    print("num of iterition {}".format(counter))
    return c


def Newton_Raphson(func, func_tag, start, end):
    xr = (start+end)/2
    f = lambdify(x, func)
    fn = lambdify(x, func_tag)
    xr_1=xr-(f(xr)/fn(xr))
    counter=1
    while abs(xr-xr_1)>eps:
        if counter > 100:
            return "The function does not converge"
        xr = xr_1
        xr_1 = xr - (f(xr) / fn(xr))
        counter += 1

    print("num of iterition {}".format(counter))
    return xr_1


def secant_method(func, start, end):
    xr_minus1 = start
    xr = end
    f = lambdify(x, func)
    xr_1 = (xr_minus1*f(xr)-xr*f(xr_minus1))/(f(xr)-f(xr_minus1))
    counter = 1
    while abs(xr - xr_1) > eps:
        if counter > 100:
            return "The function does not converge"
        xr_minus1=xr
        xr=xr_1
        xr_1=(xr_minus1*f(xr)-xr*f(xr_minus1))/(f(xr)-f(xr_minus1))
        counter += 1

    print("num of iterition {}".format(counter))
    return xr_1


def help(func, start, end, n):
    f = lambdify(x, func)
    func_tag = Calculate_derivative(func)
    fn = lambdify(x, func_tag)
    next = start + 0.1
    next = round(next, 2)
    while round(start,2) < end:
        if f(start) * f(next) < 0:
            if n == 1:
                print("x = {}".format(round(Bisection_Method(func, start, next),6)))
            if n == 2:
                print("x = {}".format(round(Newton_Raphson(func,func_tag, start, next),6)))
            if n == 3:
                print("x = {}".format(round(secant_method(func, start, next),6)))
        if f(start) == 0:
            print("x = {}".format(start))

        start += 0.1
        start = round(start, 2)
        next += 0.1
        next = round(next, 2)
    if f(end) == 0:
        print("x = {}".format(end))


def main():

    choice = input("\nchoose method for solve :\n1 - Bisection Method\n - Newton-Raphson method\n3 - Secant Method\n")

    f = x ** 4 + 1 * x ** 3 - 3 * x ** 2

    start = -4
    end = 6

    if choice == "1":
        help(f, start, end, int(choice))
        main()
    elif choice == "2":
        help(f, start, end, int(choice))
        main()
    elif choice == "3":
        help(f, start, end, int(choice))
        main()
    else:
        print("end program. goodbye")



main()


