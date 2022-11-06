# Wygeneruj próbkę o długości 50 z rozkładu wykładniczego.
# a. Wyznacz parametryczny przedział ufności dla średniej i dla odchylenia standardowego
# b. Wyznacz nieparametryczny przedział ufności dla średniej i dla odchylenia standardowego
# c. Porównaj uzyskane przedziały - parametryczny vs. nieparametryczny - który jest lepszy i dlaczego?
import numpy as np
from scipy.stats import norm

np.random.seed(0)
lamb = 1.5
exp = np.random.exponential(scale=1/lamb, size=50)
mean = exp.mean()
std = exp.std()
confidence = 0.95
crit_value = np.abs(norm.ppf((1 - confidence) / 2))

# parametric
parametric_mean = (mean - crit_value * std / np.sqrt(len(exp)), mean + crit_value * std / np.sqrt(len(exp)))
parametric_std = (std / (1 + crit_value / np.sqrt(2 * len(exp))), std / (1 - crit_value / np.sqrt(2 * len(exp))))

# nonparametric
means = [np.random.choice(exp, size=len(exp), replace=True).mean() for i in range(1000)]
nonparametric_mean = np.quantile(means, [(1 - confidence) / 2, (1 - (1 - confidence) / 2)])
stds = [np.random.choice(exp, size=len(exp), replace=True).std() for i in range(1000)]
nonparametric_std = np.quantile(stds, [(1 - confidence) / 2, (1 - (1 - confidence) / 2)])


print("PARAMETRYCZNA ŚREDNIA:", parametric_mean)
print("NIEPARAMETRYCZNA ŚREDNIA",nonparametric_mean)
print("PARAMETRYCZNAE STD:", parametric_std)
print("NIEPARAMETRYCZNE ODCHYLENIE", nonparametric_std)