import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd

# 図の見た目を調整
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['mathtext.fontset'] ='cm'
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 12
plt.rcParams['ytick.major.size'] = 12
plt.rcParams['xtick.major.pad'] = 18
plt.rcParams['ytick.major.pad'] = 18
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['figure.subplot.bottom'] = 0.2
plt.rcParams['figure.subplot.left'] = 0.2


# CSVファイルから散布図を作成
def scatter(file,xlabel="",ylabel="",i=0,j=1):
    readfile = pd.read_csv(file,usecols=[i,j])
    x = np.array(readfile.iloc[:,0])
    y = np.array(readfile.iloc[:,1])

    # 散布図を作成
    plt.scatter(x, y, s=50, c="white", marker="o",edgecolors="black")

    # 軸ラベルを記入
    plt.xlabel(r"%s"%(xlabel),fontsize = 20)
    plt.ylabel(r"%s"%(ylabel),fontsize=20)

    # CSVファイルと同じ場所に同じ名前のPNGファイルを保存
    plt.savefig(file[0:-4]+".png")
    # 図を表示
    plt.show()

# CSVファイルから散布図を作成して最小二乗法で線形近似
def linear_fit(file,xlabel="",ylabel="",i=0,j=1):
    readfile = pd.read_csv(file,usecols=[i,j])
    x = np.array(readfile.iloc[:,0])
    y = np.array(readfile.iloc[:,1])

    # 散布図を作成
    plt.scatter(x, y, s=50, c="white", marker="o",edgecolors="black")

    # 最小二乗法
    n = len(x)
    a = (np.dot(x,y)-y.sum()*x.sum() /n)/((x**2).sum()-(x.sum())**2/n)

    b = (y.sum()-a*x.sum())/n

    p = np.linspace(np.min(readfile.iloc[:,0]),np.max(readfile.iloc[:,0]))
    q = a * p + b

    plt.xlabel(r"%s"%(xlabel),fontsize=20)
    plt.ylabel(r"%s"%(ylabel),fontsize=20)

    # 最小二乗法の直線の追加
    if b<0:
        plt.plot(p,q,color="black",linestyle="dotted",label=r"$%f$"%(a)+r"$x$"+r"$%f$"%(b))
    else:
        plt.plot(p,q,color="black",linestyle="dotted",label=r"$%f$"%(a)+r"$x$"+r"$+%f$"%(b))

    plt.legend(fontsize=18)

    # 元のCSVファイルと同じ場所に同じ名前のPNGファイルを保存
    plt.savefig(file[0:-4]+".png")
    # 図を表示
    plt.show()

    return a,b

# テスト
if __name__ =="__main__":
    file = "./hall_effect/hoge.csv"
    scatter(file)
    linear_fit(file)
