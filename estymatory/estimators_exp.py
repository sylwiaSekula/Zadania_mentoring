import numpy as np
import scipy.stats as stats


scale = 1.5
exp = np.random.exponential(1/scale, size=5)
exp2 = np.random.exponential(1/scale, size=1000)
theoretical_mean = 1/scale
theoretical_variance = 1/(scale**2)
theoretical_standard_deviation = np.sqrt(1/(scale**2))
theoretical_skewness = 2
theoretical_kurtosis = 6
mean_list = []
variance_list = []
standard_deviation_list = []
skewness_list = []
kurtosis_list = []


for i in range(50):
    new_distribution = np.random.exponential(1/scale, size=1000)
    mean_list.append(np.mean(new_distribution))
    variance_list.append(np.var(new_distribution))
    standard_deviation_list.append(np.std(new_distribution))
    skewness_list.append(stats.skew(new_distribution))
    kurtosis_list.append(stats.kurtosis(new_distribution))


print('Średnia teoretyczna:', theoretical_mean)
print('Średnia z próbki 5:', np.mean(exp))
print('Średnia z próbki 1000:', np.mean(exp2))
print('Średnia z estymatorów:', np.mean(mean_list))
print('Efektwyność estymatora:', np.std(mean_list)/np.mean(mean_list)*100)
print('')
print('Wariancja teoretyczna:', theoretical_variance)
print('Wariancja z próbki 5:', np.var(exp))
print('Wariancja z próbki 1000:', np.var(exp2))
print('Średnia z estymatorów', np.mean(variance_list))
print('Efektwyność estymatora:', np.std(variance_list)/np.mean(variance_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(exp))
print('Odchylenie standardowez próbki 1000:', np.std(exp2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(exp))
print('Odchylenie standardowe z próbki 1000:', np.std(exp2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Skośność teoretyczna:', theoretical_skewness)
print('Skośność  z próbki 5:', stats.skew(exp))
print('Skośność  próbki 1000:', stats.skew(exp2))
print('Średnia z estymatorów', np.mean(skewness_list))
print('Efektwyność estymatora:', np.std(skewness_list)/np.mean(skewness_list)*100)
print('')
print('Kurtoza teoretyczna:', theoretical_kurtosis)
print('Kurtoza  z próbki 5:', stats.kurtosis(exp))
print('Kurtoza  próbki 1000:', stats.kurtosis(exp2))
print('Kurtoza z estymatorów', np.mean(kurtosis_list))
print('Efektwyność estymatora:', np.std(kurtosis_list)/np.mean(kurtosis_list)*100)
print('')