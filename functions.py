from matplotlib.pyplot import *


# Defining the function of plotting the step plot for the calculated tax
# The arguments are x and y vectors, also the calculated tax is included
def plot_step(vector_x, vector_y, tax, status, language):
    global plot_title, status_heading, tax_heading, your_income, relevant_tax_rates
    if language.lower() == 'russian' or language.lower() == 'русский':
        from vocabulary_rus import plot_title, status_heading, tax_heading, your_income, relevant_tax_rates
    elif language.lower() == 'english' or language.lower() == 'английский':
        from vocabulary_eng import plot_title, status_heading, tax_heading, your_income, relevant_tax_rates

    fig, ax = subplots()
    fig.canvas.set_window_title(plot_title)
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
def roll_the_tax_cycle(sum1, sum2, sum3, sum4, sum5, sum6, income, status, language):
    global income_between, ann_tax, big_income
    if language.lower() == 'russian' or language.lower() == 'русский':
        from vocabulary_rus import income_between, ann_tax, big_income
    elif language.lower() == 'english' or language.lower() == 'английский':
        from vocabulary_eng import income_between, ann_tax, big_income

    # Defining the parameters
    control_sums = [0, sum1, sum2, sum3, sum4, sum5, sum6]
    tax_rates = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

    # Initializing the cycle for summing the tax depending on the income
    for i in range(len(control_sums)):

        # Checking if the income is between two of adjacent control sums
        if control_sums[i] <= income <= control_sums[i + 1]:
            print('\n' + '-'*60)
            print(income_between.format(control_sums[i], control_sums[i + 1], income).replace(',', ' '))

            # Calculating the tax-part which can't be cycled
            tax = (income - control_sums[i]) * tax_rates[i]

            # Rolling the cycle to count the residual of the tax
            for k in range(i):
                tax += tax_rates[k] * (control_sums[k + 1] - (control_sums[k]))
            print(ann_tax.format(tax).replace(',', ' '))
            print('-'*60)

            # Making x and y vectors for the plot
            if income < control_sums[1]:
                x_vector = [income]
            else:
                x_vector = control_sums[:i + 1] + [income]
            if income < control_sums[1]:
                y_vector = [tax_rates[0]]
            else:
                y_vector = tax_rates[:i + 1] + [tax_rates[i]]

            # Initializing the plot (derived from "functions" file)
            plot_step(x_vector, y_vector, tax, status, language)
            break

        elif income >= (control_sums[-1] + 1):  # When the income is higher than the biggest control sum
            print('\n' + '-'*60)
            print(big_income.format(control_sums[-1], income).replace(',', ' '))

            # Calculating the tax-part which can't be cycled
            tax = (income - control_sums[-1]) * tax_rates[-1]

            # Rolling the cycle to count the residual of the tax
            for k in range(len(control_sums) - 1):
                tax += tax_rates[k] * (control_sums[k + 1] - (control_sums[k]))
            print(ann_tax.format(tax).replace(',', ' '))
            print('-'*60)

            # Making x and y vectors for the plot
            x_vector = control_sums + [income]
            y_vector = tax_rates + [tax_rates[-1]]

            # Initializing the plot (derived from "functions" file)
            plot_step(x_vector, y_vector, tax, status, language)
            break
