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
