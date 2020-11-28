import matplotlib.pyplot as plt
import csv

SOLD_COLOR = 'seagreen'
ITEM_COLOR = 'salmon'
BG_COLOR = 'beige'

def get_file(single_item_cost):
    x=[]
    y=[]
    with open('data/estimate.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))
        return x, y
def get_input():
    x=[]
    y=[]
    with open('data/input_data.csv','r') as csvfile:
        input_data = csv.reader(csvfile, delimiter=',')
        
        for row in input_data:
            x.append(float(row[0]))
        return x
def get_plt():
    # getting info right
    input_x = get_input();
    currently_in_stock = float(input_x[0]);
    itemcost_per_item = float(input_x[1]);
    stock_count_x = []
    stock_count_y = []
    x, y = get_file(2)
    for i in range(len(x)):
        for j in range(len(y)):
            currently_in_stock -= y[i] * itemcost_per_item
            stock_count_x.append(i)
            stock_count_y.append(currently_in_stock)
    # plotting
    plt.rcParams['axes.facecolor'] = BG_COLOR
    fig = plt.figure(0);
    fig.canvas.set_window_title("Coinage")
    plt.plot(x,y, label='volume', color=SOLD_COLOR)
    plt.plot(stock_count_x,stock_count_y, label='stock for item', color=ITEM_COLOR)
    plt.xlabel('Month')
    plt.ylabel('Volume')
    plt.title('')
    plt.legend()
    plt.show()
    return get_plt
get_plt()
