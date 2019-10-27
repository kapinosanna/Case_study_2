from functions import *

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

# Calculating the tax based on the subject's status and plotting the beauty
if status == status_subject:
    roll_the_tax_cycle(9075, 36900, 89350, 186350, 405100, 406750, income, status, language)
elif status == status_couple:
    roll_the_tax_cycle(18150, 73800, 148850, 226850, 405100, 457600, income, status, language)
else:
    roll_the_tax_cycle(12950, 49400, 127550, 206600, 405100, 432200, income, status, language)

# Deciding whether to save the plot or just show it
choice_of_path = input(save_or_show)
if choice_of_path == 'show' or choice_of_path == 'показать':
    show()
elif choice_of_path == 'save' or choice_of_path == 'сохранить':
    plot_name = plot_title + '.png'
    savefig(plot_name, dpi=300, bbox_inches='tight')
