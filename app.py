
#importing the library for solving expressions and equations
import sympy as sp
import numpy as np
#introducing 3 variables
a, b, alpha = sp.symbols("a b alpha")

#the expression to be solved
expression = a**4 + 2*b**4 + a**2*b**2 + 2*a + b
input_points = np.array([0,0])
#partial differential equations to a and b, respectively
a_prime = sp.diff(expression, a)
b_prime = sp.diff(expression, b)
#print(a_prime, b_prime)

#substitution of variables with the values given in the problem (0,0)
partial_a = a_prime.subs(a, 0)
partial_b = b_prime.subs(b, 0)
partials = np.array([partial_a, partial_b])
print(f"Partials derivatives when a,b are zeros:{partial_a, partial_b}")
#solving phi value
alpha_a = partial_a*alpha
alpha_b = partial_b*alpha
phi = expression.subs([(a, alpha_a), (b, alpha_b)])
alpha_0 = sp.diff(phi, alpha)
alpha_real = sp.solve(alpha_0)[0]
print(alpha_real)
#input_points - alpha * partials
x1 = np.subtract(input_points, alpha_real * partials)
print(x1)
x2 = np.add(x1, alpha_real**2 * partials)
print(x2)
phi_1 = expression.subs([(a, x2[0]), (b, x2[1])])
print(sp.solve(phi_1, 0))