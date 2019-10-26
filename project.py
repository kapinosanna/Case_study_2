from matplotlib.pyplot import *

# Defining the language
while True:
    language = input('Please choose the language: Russian or English? ')
    if language.lower() == 'russian' or language.lower() == 'русский':
        from vocabulary_rus import *
        break
    elif language.lower() == 'english' or language.lower() == 'английский':
        from vocabulary_eng import *
        break
    print('You typed the language incorrectly. Please, try again.\n')

# Finding out about the subject status
while True:
    alone = input(question1)
    if alone.lower() == 'да' or alone.lower() == 'yes':
        while True:
            kids = input(question_kids)
            if kids.lower() == 'да' or kids.lower() == 'yes':
                status = status_lonepar
                break
            elif kids.lower() == 'нет' or kids.lower() == 'no':
                status = status_subject
                break
            print('Oops, there`s a misprint somewhere! Please, try again!\n')
        break
    elif alone.lower() == 'нет' or alone.lower() == 'no':
        status = status_couple
        break
    print('Oops, there`s a misprint somewhere! Please, try again!\n')

# Finding out about the subject's estimate income
ident = input(income_differ)
if ident.lower() == 'нет' or ident.lower() == 'no':
    month_income = int(input(av_mon_income))
    income = month_income * 12
elif ident.lower() == 'да' or ident.lower() == 'yes':

    # Stating the parameters for the coming cycle
    months = list_months
    income = 0

    # Calculating the annual income month by month
    for z in range(12):
        month_income = int(input(est_mon_income.format(months[z])))
        income += month_income

# Finding out about tax deduction
deduction_sum = int(input(deduction))
income -= deduction_sum


# Defining the function of plotting the step plot for the calculated tax
# The arguments are x and y vectors, also the calculated tax is included
def plot_step(vector_x, vector_y, tax):
    fig, ax = subplots()
    ax.set_facecolor('#E0FFFF')
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
def roll_the_tax_cycle(sum1, sum2, sum3, sum4, sum5, sum6):
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

            # Initializing the plot
            plot_step(x_vector, y_vector, tax)
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

            # Initializing the plot
            plot_step(x_vector, y_vector, tax)
            break


# Calculating the tax based on the subject's status and plotting the beauty
if status == status_subject:
    roll_the_tax_cycle(9075, 36900, 89350, 186350, 405100, 406750)
elif status == status_couple:
    roll_the_tax_cycle(18150, 73800, 148850, 226850, 405100, 457600)
else:
    roll_the_tax_cycle(12950, 49400, 127550, 206600, 405100, 432200)

show()
