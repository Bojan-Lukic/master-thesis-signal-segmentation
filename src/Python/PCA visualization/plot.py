import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator


def surface_plot(X, tot, label_x, label_y, label_z, view_init_x, view_init_y):
    calibri = {'fontname':'Calibri'}
    fig = plt.figure(figsize = (12, 12))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(*(X.T), s=100)
    ax.plot_surface(tot[0], tot[1], tot[2], alpha=0.6, color='orange')
    ax.set_xlabel(label_x, **calibri, fontsize=14, labelpad=10)
    ax.set_ylabel(label_y, **calibri, fontsize=14, labelpad=10)
    ax.set_zlabel(label_y, **calibri, fontsize=14, labelpad=10)
    ax.tick_params(labelsize=12)
    ax.view_init(view_init_x, view_init_y)


def single_plot(A, label_x, label_y, ax=False):
    calibri = {'fontname':'Calibri'}
    if ax == True:
        ax = plt.figure(figsize = (12, 8)).gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    else:
        plt.figure(figsize = (12, 8))
    plt.grid()
    plt.plot(A)
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)


def TD_plot(tot, label_x, label_y, label_z):
    calibri = {'fontname':'Calibri'}
    fig = plt.figure(figsize = (12, 12))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(tot[0], tot[1], tot[2], s=100)
    ax.set_xlabel(label_x, **calibri, fontsize=14, labelpad=10)
    ax.set_ylabel(label_y, **calibri, fontsize=14, labelpad=10)
    ax.set_zlabel(label_z, **calibri, fontsize=14, labelpad=10)
    ax.tick_params(labelsize=12)