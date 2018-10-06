

import matplotlib.pyplot as plt
from collections import defaultdict
def create_hist(len,count,filename):
    # temp=defaultdict(count,0)
    x=[i for i in range(1,len+1)]
    y=[count[i] for i in range(1,len+1)]
    plt.xlabel("page of questhons")
    plt.ylabel("number of questions")
    plt.xticks(x)
    plt.title(filename)
    plt.bar(x,y,width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white',lw=1)
    plt.savefig("./img/{0}.jpg".format(filename))
    # plt.show()

if __name__ == '__main__':
    create_hist()