from matplotlib.pyplot import *
from vocabulary_eng import *
from vocabulary_rus import *


# Defining the function of plotting the step plot for the calculated tax
# The arguments are x and y vectors, also the calculated tax is included
def plot_step(vector_x, vector_y, tax, status):
    fig, ax = subplots()
    bgcolor = '#E0FFFF'
    ax.set_facecolor(bgcolor)
    fig.patch.set_facecolor(bgcolor)
    ax.step(vector_x, vector_y, where='post', linestyle='--', label=(status_heading.format(status) +
                                                                     tax_heading.format(tax).replace(',', ' ')))
    ax.set_xticks(vector_x)
    ax.tick_params('x', labelrotation=20)
    ax.set_xlabel(your_income)
    ax.set_yticks(vector_y)
    ax.tick_params('y', labelsize=12)
    ax.set_ylabel(relevant_tax_rates)
    ax.set_title(plot_title, fontsize=15)
    ax.legend()


# Defining the function of counting the tax depending on the income
# The arguments are control sums, relevant to the subject's status
def roll_the_tax_cycle(sum1, sum2, sum3, sum4, sum5, sum6, income, status):
    # Defining the parameters
    control_sums = [0, sum1, sum2, sum3, sum4, sum5, sum6]
    tax_rates = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

    # Initializing the cycle for summing the tax depending on the income
    for i in range(len(control_sums)):

        # Checking if the income is between two of adjacent control sums
        if control_sums[i] <= income <= control_sums[i + 1]:
            print(income_between.format(control_sums[i], control_sums[i + 1], income).replace(',', ' '))

            # Calculating the tax-part which can't be cycled
            control_sums[0] = -1
            tax = (income - control_sums[i]) * tax_rates[i]

            # Rolling the cycle to count the residual of the tax
            for k in range(i):
                tax += tax_rates[k] * (control_sums[k + 1] - (control_sums[k] + 1))
            print(ann_tax.format(tax).replace(',', ' '))

            # Making x and y vectors for the plot
            control_sums[0] = 0
            x_vector = control_sums[:i] + [income]
            y_vector = tax_rates[:i] + [tax_rates[i - 1]]

            # Initializing the plot (derived from "functions" file)
            plot_step(x_vector, y_vector, tax, status)
            break

        elif income >= (control_sums[-1] + 1):  # When the income is higher than the biggest control sum
            print(big_income.format(control_sums[-1], income).replace(',', ' '))

            # Calculating the tax-part which can't be cycled
            control_sums[0] = -1
            tax = (income - control_sums[-1]) * tax_rates[-1]

            # Rolling the cycle to count the residual of the tax
            for k in range(len(control_sums) - 1):
                tax += tax_rates[k] * (control_sums[k + 1] - (control_sums[k] + 1))
            print(ann_tax.format(tax).replace(',', ' '))

            # Making x and y vectors for the plot
            control_sums[0] = 0
            x_vector = control_sums + [income]
            y_vector = tax_rates + [tax_rates[-1]]

            # Initializing the plot (derived from "functions" file)
            plot_step(x_vector, y_vector, tax, status)
            break
