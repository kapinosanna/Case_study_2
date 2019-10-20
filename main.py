from matplotlib.pyplot import *

control_sums = [0, 9075, 36900, 89350, 186350, 405100, 406750]
tax_rates = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

x_vector = [0]
for i in range(1, len(control_sums)-1):
    x_vector.append(control_sums[i])
    x_vector.append(control_sums[i])
x_vector.append(control_sums[-1])
print(x_vector)

y_vector = [0, 0]
for i in range(len(tax_rates)-2):
    y_vector.append(tax_rates[i])
    y_vector.append(tax_rates[i])

print(y_vector)

fig, ax = subplots()
ax.plot(x_vector, y_vector)

show()