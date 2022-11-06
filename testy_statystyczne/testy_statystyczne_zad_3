#Wylosuj próbkę o wielkości 40 z rozkładu chi-kwadrat o 3 stopniach swobody korzystając
#z definicji zmiennej z rozkładu chi kwadrat (czyli zrób to bez korzystania z funkcji np.random.chisquare)
#a. Stwórz histogram i boxplot utworzonej zmiennej
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

norm1 = np.random.normal(0, 1, size=40)
norm2 = np.random.normal(0, 1, size=40)
norm3 = np.random.normal(0, 1, size=40)

my_chi2 = (norm1 **2 + norm2 ** 2 + norm3**2)
x = np.linspace(0, 15, 1000)

plt.hist(my_chi2, 10, density=True, color='#006666', edgecolor='k')
plt.plot(x, chi2.pdf(x, df=3))
plt.show()

plt.boxplot(my_chi2)
plt.show()
