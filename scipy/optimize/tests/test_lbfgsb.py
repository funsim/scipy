from scipy.optimize import minimize, rosen, rosen_der, fmin_l_bfgs_b
from scipy.optimize import _lbfgsb
import numpy as np
print _lbfgsb.setulb.__doc__

def inner(n, x, xinc, y, yinc):
    assert xinc == yinc == 1
    return np.dot(x, y)

x0 = [1.3, 0.7, 0.8, 1.9, 1.2]

fmin_l_bfgs_b(rosen, x0, fprime=rosen_der, pgtol=1e-6, disp=True, inner_product=inner)
fmin_l_bfgs_b(rosen, x0, fprime=rosen_der, pgtol=1e-6, disp=True)
