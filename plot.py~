import matplotlib.pyplot as plt
import csv
F_COLOR = 'seagreen'
BG_COLOR = 'beige'
x = []
y = []

def get_file():
    with open('data/finances.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
        return plots
def get_plt():
    plots = get_file()
    plt.rcParams['axes.facecolor'] = BG_COLOR
    fig = plt.figure(0);
    fig.canvas.set_window_title("Coinage")
    plt.plot(x,y, label='', color=F_COLOR)
    plt.xlabel('Month')
    plt.ylabel('Income €')
    plt.title('')
    plt.legend()
    plt.show()
    return get_plt
get_plt()
