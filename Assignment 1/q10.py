population = 80000
men = population * 52 / 100
women = population - men
literate = population * 48 / 100
literate_men = population * 35 / 100
literate_women = literate - literate_men
illiterate_men = men - literate_men
illiterate_women = women - literate_women
print("Illiterate men:", illiterate_men)
print("Illiterate women:", illiterate_women)
