import numpy as np
import scipy.stats as stats


loc = 0
scale = 1
normal = np.random.normal(loc, scale, size=5)
normal2 = np.random.normal(loc, scale, size=1000)
theoretical_mean = loc
theoretical_variance = scale **2
theoretical_standard_deviation = scale
theoretical_skewness = 0
theoretical_kurtosis = 0
mean_list = []
variance_list = []
standard_deviation_list = []
skewness_list = []
kurtosis_list = []


for i in range(50):
    new_distribution = np.random.normal(loc, scale, size=1000)
    mean_list.append(np.mean(new_distribution))
    variance_list.append(np.var(new_distribution))
    standard_deviation_list.append(np.std(new_distribution))
    skewness_list.append(stats.skew(new_distribution))
    kurtosis_list.append(stats.kurtosis(new_distribution))


print('Średnia teoretyczna:', theoretical_mean)
print('Średnia z próbki 5:', np.mean(normal))
print('Średnia z próbki 1000:', np.mean(normal2))
print('Średnia z estymatorów:', np.mean(mean_list))
print('Efektwyność estymatora:', np.std(mean_list)/np.mean(mean_list)*100)
print('')
print('Wariancja teoretyczna:', theoretical_variance)
print('Wariancja z próbki 5:', np.var(normal))
print('Wariancja z próbki 1000:', np.var(normal2))
print("Średnia z estymatorów", np.mean(variance_list))
print('Efektwyność estymatora:', np.std(variance_list)/np.mean(variance_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(normal))
print('Odchylenie standardowez próbki 1000:', np.std(normal2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(normal))
print('Odchylenie standardowe z próbki 1000:', np.std(normal2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Skośność teoretyczna:', theoretical_skewness)
print('Skośność  z próbki 5:', stats.skew(normal))
print('Skośność  próbki 1000:', stats.skew(normal2))
print('Średnia z estymatorów', np.mean(skewness_list))
print('Efektwyność estymatora:', np.std(skewness_list)/np.mean(skewness_list)*100)
print('')
print('Kurtoza teoretyczna:', theoretical_kurtosis)
print('Kurtoza  z próbki 5:', stats.kurtosis(normal))
print('Kurtoza  próbki 1000:', stats.kurtosis(normal2))
print('Kurtoza z estymatorów', np.mean(kurtosis_list))
print('Efektwyność estymatora:', np.std(kurtosis_list)/np.mean(kurtosis_list)*100)
print('')