import matplotlib.pyplot as plt


def multiplot(results, label_x, label_y):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (12, 8))
    plt.grid()
    for i in range (0, len(results)):
        plt.plot(results[i])
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)


def single_plot(A, label_x, label_y):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (12, 8))
    plt.grid()
    plt.plot(A)
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)


def bar_plot(y_pos, ratiolistcount, label_x, label_y):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (16, 8))
    plt.bar(y_pos, ratiolistcount, align='center', alpha=0.5)
    for i in range(len(ratiolistcount)):
        plt.text(i, int(ratiolistcount[i]) + 2, int(ratiolistcount[i]), ha = 'center', fontsize = 14)
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)