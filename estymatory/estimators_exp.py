import numpy as np
import scipy.stats as stats

scale = 1.5
exp = np.random.exponential(1 / scale, size=5)
exp2 = np.random.exponential(1 / scale, size=1000)
theoretical_mean = 1 / scale
theoretical_variance = 1 / (scale ** 2)
theoretical_standard_deviation = np.sqrt(1 / (scale ** 2))
theoretical_skewness = 2
theoretical_kurtosis = 6
mean_list = []
variance_list = []
standard_deviation_list = []
skewness_list = []
kurtosis_list = []

for i in range(50):
    new_distribution = np.random.exponential(1 / scale, size=1000)
    mean_list.append(np.mean(new_distribution))
    variance_list.append(np.var(new_distribution))
    standard_deviation_list.append(np.std(new_distribution))
    skewness_list.append(stats.skew(new_distribution))
    kurtosis_list.append(stats.kurtosis(new_distribution))

calculations = [theoretical_mean, np.mean(exp), np.mean(exp2), np.mean(mean_list),
                np.std(mean_list) / np.mean(mean_list) * 100, theoretical_variance,
                np.var(exp), np.var(exp2), np.mean(variance_list),
                np.std(variance_list) / np.mean(variance_list) * 100, theoretical_standard_deviation,
                np.std(exp), np.std(exp2), np.mean(standard_deviation_list),
                np.std(standard_deviation_list) / np.mean(standard_deviation_list) * 100,
                theoretical_standard_deviation, np.std(exp), np.std(exp2), np.mean(standard_deviation_list),
                np.std(standard_deviation_list) / np.mean(standard_deviation_list) * 100,
                theoretical_skewness, stats.skew(exp), stats.skew(exp2), np.mean(skewness_list),
                np.std(skewness_list) / np.mean(skewness_list) * 100,
                theoretical_kurtosis, stats.kurtosis(exp), stats.kurtosis(exp2), np.mean(kurtosis_list),
                np.std(kurtosis_list) / np.mean(kurtosis_list) * 100]
descriptions = ['Theoretical mean:', 'Średnia z próbki 5:', 'Średnia z próbki 1000:', 'Średnia z estymatorów:',
                'Efektwyność estymatora:',
                '\nWariancja teoretyczna:', 'Wariancja z próbki 5:', 'Wariancja z próbki 1000:',
                'Średnia z estymatorów', 'Efektwyność estymatora:',
                '\nOdchylenie standardowe teoretyczne:', 'Odchylenie standardowe z próbki 5:',
                'Odchylenie standardowez próbki 1000:', 'Średnia z estymatorów',
                'Efektwyność estymatora:', '\nOdchylenie standardowe teoretyczne:',
                'Odchylenie standardowe z próbki 5:', 'Odchylenie standardowe z próbki 1000:',
                'Średnia z estymatorów', 'Efektwyność estymatora:', '\nSkośność teoretyczna:', 'Skośność  z próbki 5:',
                'Skośność  próbki 1000:',
                'Średnia z estymatorów', 'Efektwyność estymatora:', '\nKurtoza teoretyczna:', 'Kurtoza  z próbki 5:',
                'Kurtoza  próbki 1000:', 'Kurtoza z estymatorów',
                'Efektwyność estymatora:']

for description, calculation in zip(descriptions, calculations):
    print(description, calculation)
