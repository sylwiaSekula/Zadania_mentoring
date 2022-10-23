import numpy as np
import scipy.stats as stats


p = 0.35
geo = np.random.geometric(p, size=5)
geo2 = np.random.geometric(p, size=1000)
theoretical_mean = 1/p
theoretical_variance = (1 - p) / p ** 2
theoretical_standard_deviation = np.sqrt((1 - p) / p ** 2)
theoretical_skewness = (2 - p) / np.sqrt(1 - p)
theoretical_kurtosis = 6 + ((p ** 2) / (1 - p))
mean_list = []
variance_list = []
standard_deviation_list = []
skewness_list = []
kurtosis_list = []


for i in range(50):
    new_distribution = np.random.geometric(p, size=1000)
    mean_list.append(np.mean(new_distribution))
    variance_list.append(np.var(new_distribution))
    standard_deviation_list.append(np.std(new_distribution))
    skewness_list.append(stats.skew(new_distribution))
    kurtosis_list.append(stats.kurtosis(new_distribution))


print('Średnia teoretyczna:', theoretical_mean)
print('Średnia z próbki 5:', np.mean(geo))
print('Średnia z próbki 1000:', np.mean(geo2))
print('Średnia z estymatorów:', np.mean(mean_list))
print('Efektwyność estymatora:', np.std(mean_list)/np.mean(mean_list)*100)
print('')
print('Wariancja teoretyczna:', theoretical_variance)
print('Wariancja z próbki 5:', np.var(geo))
print('Wariancja z próbki 1000:', np.var(geo2))
print('Średnia z estymatorów', np.mean(variance_list))
print('Efektwyność estymatora:', np.std(variance_list)/np.mean(variance_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(geo))
print('Odchylenie standardowez próbki 1000:', np.std(geo2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(geo))
print('Odchylenie standardowe z próbki 1000:', np.std(geo2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Skośność teoretyczna:', theoretical_skewness)
print('Skośność  z próbki 5:', stats.skew(geo))
print('Skośność  próbki 1000:', stats.skew(geo2))
print('Średnia z estymatorów', np.mean(skewness_list))
print('Efektwyność estymatora:', np.std(skewness_list)/np.mean(skewness_list)*100)
print('')
print('Kurtoza teoretyczna:', theoretical_kurtosis)
print('Kurtoza  z próbki 5:', stats.kurtosis(geo))
print('Kurtoza  próbki 1000:', stats.kurtosis(geo2))
print('Kurtoza z estymatorów', np.mean(kurtosis_list))
print('Efektwyność estymatora:', np.std(kurtosis_list)/np.mean(kurtosis_list)*100)
print('')