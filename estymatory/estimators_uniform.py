import numpy as np
import scipy.stats as stats


low = 2
high = 5
uni = np.random.uniform(low, high, size=5)
uni2 = np.random.uniform(low, high, size=1000)
theoretical_mean = ((low + high) / 2)
theoretical_variance = ((high - low) ** 2 / 12)
theoretical_standard_deviation = np.sqrt((high - low) ** 2 / 12)
theoretical_skewness = 0
theoretical_kurtosis = -6/5
mean_list = []
variance_list = []
standard_deviation_list = []
skewness_list = []
kurtosis_list = []


for i in range(50):
    new_distribution = np.random.uniform(low, high, size=1000)
    mean_list.append(np.mean(new_distribution))
    variance_list.append(np.var(new_distribution))
    standard_deviation_list.append(np.std(new_distribution))
    skewness_list.append(stats.skew(new_distribution))
    kurtosis_list.append(stats.kurtosis(new_distribution))


print('Średnia teoretyczna:', theoretical_mean)
print('Średnia z próbki 5:', np.mean(uni))
print('Średnia z próbki 1000:', np.mean(uni2))
print('Średnia z estymatorów:', np.mean(mean_list))
print('Efektwyność estymatora:', np.std(mean_list)/np.mean(mean_list)*100)
print('')
print('Wariancja teoretyczna:', theoretical_variance)
print('Wariancja z próbki 5:', np.var(uni))
print('Wariancja z próbki 1000:', np.var(uni2))
print('Średnia z estymatorów', np.mean(variance_list))
print('Efektwyność estymatora:', np.std(variance_list)/np.mean(variance_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(uni))
print('Odchylenie standardowez próbki 1000:', np.std(uni2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Odchylenie standardowe teoretyczne:', theoretical_standard_deviation)
print('Odchylenie standardowe z próbki 5:', np.std(uni))
print('Odchylenie standardowe z próbki 1000:', np.std(uni2))
print('Średnia z estymatorów', np.mean(standard_deviation_list))
print('Efektwyność estymatora:', np.std(standard_deviation_list)/np.mean(standard_deviation_list)*100)
print('')
print('Skośność teoretyczna:', theoretical_skewness)
print('Skośność  z próbki 5:', stats.skew(uni))
print('Skośność  próbki 1000:', stats.skew(uni2))
print('Średnia z estymatorów', np.mean(skewness_list))
print('Efektwyność estymatora:', np.std(skewness_list)/np.mean(skewness_list)*100)
print('')
print('Kurtoza teoretyczna:', theoretical_kurtosis)
print('Kurtoza  z próbki 5:', stats.kurtosis(uni))
print('Kurtoza  próbki 1000:', stats.kurtosis(uni2))
print('Kurtoza z estymatorów', np.mean(kurtosis_list))
print('Efektwyność estymatora:', np.std(kurtosis_list)/np.mean(kurtosis_list)*100)
print('')