from distributions import Binomial

b = Binomial()
p = round(b.pdf(5), 5)
print(p)
