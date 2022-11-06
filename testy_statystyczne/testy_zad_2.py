# 100 razy wylosuj z rozkładu normalnego N(5,2) (wielkość pojedynczej próbki - 50).
# Wyznacz przedziały ufności dla każdej próbki i sprawdź czy prawdziwa średnia znalazłasię w przedziale.
# W ilu % przypadków prawdziwa średnia znalazła się w przedziale ufności?

import numpy as np
from scipy.stats import norm

result = [np.random.normal(loc=5, scale=2, size=50) for i in range(100)]
confidence = 0.95
mean = 5
crit_value = np.abs(norm.ppf((1 - confidence) / 2))
success = 0

for x in result:
    if np.mean(x) - crit_value * np.std(x)/np.sqrt(len(x)) < mean < np.mean(x) +  crit_value * np.std(x)/ np.sqrt(len(x)):
        success += 1
        print("OK - średnia:", mean, ", przedział ufności:", (np.mean(x) - crit_value * np.std(x) / np.sqrt(len(x)), np.mean(x) + crit_value * np.std(x) / np.sqrt(len(x))))
    else:
        print("NOT OK - średnia:", mean, ", przedział ufności:", (np.mean(x) - crit_value * np.std(x) / np.sqrt(len(x)), np.mean(x) + crit_value * np.std(x) / np.sqrt(len(x))))

print(success, "% sukcesów")



