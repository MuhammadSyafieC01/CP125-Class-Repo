import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    f = pd.read_csv(filename)
    df = pd.DataFrame(f)
    math = df.Math
    print(math)
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    y = math
    plt.plot(x,y)
    plt.xlabel("Math Score")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")
    plt.show()

show_math_trend("labs\lab09\data\students.csv")
