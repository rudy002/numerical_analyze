# Gad Nadjar - 337744155
# Shmuel Malikov - 313530537
# Rudy Haddad - 337744155


import sympy as sp
import math
from sympy.utilities.lambdify import lambdify


def Calculate_derivative(f):
    f_prime = f.diff(x)
    return f_prime


x = sp.symbols('x')


def I(func, a, b):
    f = lambdify(x, func)
    return 0.5 * (b - a) * (f(a) + f(b))


def TrapezoidalRule(func, a, b, n):
    h = float(b - a) / n
    sum = 0.0
    for i in range(n):
        sum += I(func, a, a + h)
        a += h
    return sum


def SimpsonRule(func, a, b, n):
    f = lambdify(x, func)
    if n % 2 != 0:
        return "n must be even"
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            integral += 2 * f(k)
        else:
            integral += 4 * f(k)
    integral *= (h / 3)
    return integral


ff = (sp.sin(2 * sp.exp(-2 * x))) / (x ** 2 + 5 * x + 6)
print(SimpsonRule(ff, -0.4, 0.4, 4))
