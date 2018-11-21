# -*- coding: utf-8 -*-
"""
This module is to analyse the iMotion data
21 Nov 2018
@author: Chng Eng Siong
"""
import numpy as np
import matplotlib.pyplot as plt


import argparse

import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt

def my_main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--order", type=int, default=3, help="order of Bessel function")
    parser.add_argument("--output", default="plot.png", help="output image file")
    args = parser.parse_args()

    print('Hello')
    # Compute maximum
    f = lambda x: -special.jv(args.order, x)
    sol = optimize.minimize(f, 1.0)

    # Plot
    x = np.linspace(0, 10, 5000)
    plt.plot(x, special.jv(args.order, x), '-', sol.x, -sol.fun, 'o')
    plt.show()
    print(x)
    
    # Produce output
    plt.savefig(args.output, dpi=96)

def test_interpolate():
# Create data with missing y values
    x = [i for i in range(0, 100)]
    y = [i**2 + i**3 for i in range(0, 100)]

    # convert to numpy arrays
    x = np.array(x)
    y = np.array(y)


    y[40:50] = np.nan
    y[70:85] = np.nan

    # drop NaNs
    idx_finite = np.isfinite(y)
    f_finite = interpolate.interp1d(x[idx_finite], y[idx_finite])
    ynew_finite = f_finite(x)

    # Interpolation attempt 1: Use scipy's interpolate.interp1d
    f = interpolate.interp1d(x, y)
    ynew = f(x)

    # Interpolate attempt 2: Use pandas.Series.interpolate
    yp = pd.Series(y)
    yp = yp.interpolate(limit_direction='both', kind='cubic')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'o',label="true")
    ax.plot(x, ynew, '-',label="interp1d")
    ax.plot(x, ynew_finite, '--',label="interp1d finite")
    ax.plot(x, yp, 'x',label="pandas")
    plt.legend()
    plt.show()

print('hello world')
test_interpolate()
#my_main()

