import matplotlib.pyplot as plt
import csv

SOLD_COLOR = 'seagreen'
ITEM_COLOR = 'salmon'
BG_COLOR = 'beige'

def get_file(single_item_cost):
    x=[]
    y=[]
    with open('data/finances.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
        return x, y
def get_input():
    x=[]
    y=[]
    with open('data/input_data.csv','r') as csvfile:
        input_data = csv.reader(csvfile, delimiter=',')
        for row in input_data:
            x.append(int(row[0]))
            y.append(int(row[1]))
        return x, y
def get_cost(single_item_cost, volume):
    return [single_item_cost * volume]
    
def get_plt():
    input_x, input_y = get_input();
    stock_count_x = []
    stock_count_y = []
    x, y = get_file(2)
    for i in x:
        for j in y:
            stock_count_x.append(i)
            stock_count_y.append(j)
    plt.rcParams['axes.facecolor'] = BG_COLOR
    fig = plt.figure(0);
    fig.canvas.set_window_title("Coinage")
    
    
    plt.plot(x,y, label='volume', color=SOLD_COLOR)
    plt.plot(stock_count_x,stock_count_y, label='stock for item:', color=ITEM_COLOR)
    plt.xlabel('Month')
    plt.ylabel('Income €')
    plt.title('')
    plt.legend()
    plt.show()
    return get_plt
get_plt()
