import scipy.stats as stats
var = 10
p_12_or_more = 1 - stats.poisson.cdf(11, var)
p_12_to_18 = stats.poisson.cdf(18, var) - stats.poisson.cdf(11, var)
print("Probability of observing 12 or more days of rain:", p_12_or_more)
print("Probability of observing between 12 and 18 days of rain:", p_12_to_18)