import numpy as np
import scipy.stats as stats


lam = 1
poisson = np.random.poisson(lam, size=5)
poisson2 = np.random.poisson(lam, size=1000)
theoretical_mean = lam
theoretical_variance = lam
theoretical_standard_deviation = np.sqrt(lam)
theoretical_skewness = lam ** (-1/2)
theoretical_kurtosis = lam ** -1
mean_list = []
variance_list = []
standard_deviation_list = []
skewness_list = []
kurtosis_list = []


for i in range(50):
    new_distribution = np.random.poisson(lam, size=1000)
    mean_list.append(np.mean(new_distribution))
    variance_list.append(np.var(new_distribution))
    standard_deviation_list.append(np.std(new_distribution))
    skewness_list.append(stats.skew(new_distribution))
    kurtosis_list.append(stats.kurtosis(new_distribution))

calculations = [theoretical_mean, np.mean(poisson), np.mean(poisson2), np.mean(mean_list), np.std(mean_list) / np.mean(mean_list) * 100, theoretical_variance,
                np.var(poisson), np.var(poisson2), np.mean(variance_list), np.std(variance_list) / np.mean(variance_list) * 100,
                theoretical_standard_deviation, np.std(poisson) , np.std(poisson2), np.mean(standard_deviation_list), np.std(standard_deviation_list) / np.mean(standard_deviation_list) * 100,
                theoretical_skewness, stats.skew(poisson), stats.skew(poisson2), np.mean(skewness_list), np.std(skewness_list) / np.mean(skewness_list) * 100,
                theoretical_kurtosis, stats.kurtosis(poisson), stats.kurtosis(poisson2), np.mean(kurtosis_list), np.std(kurtosis_list) / np.mean(kurtosis_list) * 100]
descriptions = ['Theoretical mean:','Średnia z próbki 5:', 'Średnia z próbki 1000:', 'Średnia z estymatorów:', 'Efektwyność estymatora:',
                '\nWariancja teoretyczna:', 'Wariancja z próbki 5:', 'Wariancja z próbki 1000:', 'Średnia z estymatorów', 'Efektwyność estymatora:',
                '\nOdchylenie standardowe teoretyczne:',  'Odchylenie standardowe z próbki 5:','Odchylenie standardowe z próbki 1000:',
                'Średnia z estymatorów', 'Efektwyność estymatora:', '\nSkośność teoretyczna:', 'Skośność  z próbki 5:', 'Skośność  próbki 1000:',
                'Średnia z estymatorów','Efektwyność estymatora:','\nKurtoza teoretyczna:', 'Kurtoza  z próbki 5:','Kurtoza  próbki 1000:', 'Kurtoza z estymatorów',
                'Efektwyność estymatora:']


for description, calculation in zip(descriptions, calculations):
    print(description, calculation)
