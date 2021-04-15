n = len(x)
if n % 2:
     median_ = sorted(x)[round(0.5*(n-1))]
else:
     x_ord, index = sorted(x), round(0.5 * n)
     median_ = 0.5 * (x_ord[index-1] + x_ord[index])

median_