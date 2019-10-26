from matplotlib.pyplot import *

control_sums = [0, 9075, 36900, 89350, 186350, 405100, 406750, 500000]
tax_rates = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396, 0.396]

fig, ax = subplots()

ax.step(control_sums, tax_rates, color = 'orange', where='post')
ax.set_xticks(control_sums)
ax.tick_params('x', labelrotation=20)
ax.set_yticks(tax_rates)
ax.tick_params('y', labelsize=12)
ax.set_title('plot_title', fontsize=15)
ax.legend()

show()