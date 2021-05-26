"""
Probability theory - cumulative distribution function
and probability density function

Example using log-normal distribution

"""
# import libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# variable to evaluate the functions on
x = np.linspace(0, 5, 1000)

p1 = stats.lognorm.pdf(x, 1)
c1 = stats.lognorm.cdf(x, 1)

p2 = stats.lognorm.pdf(x,.1)
c2 = stats.lognorm.cdf(x,.1)

# draw the pdfs
fig, ax = plt.subplots(2, 1, figsize=(4, 7))
ax[0].plot(x, p1/sum(p1))
ax[0].plot(x, p1/sum(p1), x, p2/(sum(p2)))
ax[0].set_ylabel('probability')
ax[0].set_title('pdf(x)')

# draw the cdfs
ax[1].plot(x, c1)
ax[1].plot(x, c1, x, c2)
ax[1].set_ylabel('probability')
ax[1].set_title('cdf(x)')
plt.show()

# computing the cdf from the pdf

c1x = np.cumsum(p1)

plt.plot(x, c1)
plt.plot(x, c1x, '--')
plt.show()

