from numpy import abs, exp

eps = 0.0001

xold = 1.0
xnew = 2.0
while abs(xnew - xold) > eps:
	xold = xnew
	xnew = 1./(1 + exp(xold))
	print(xnew)