import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    f = pd.read_csv(filename)
    df = pd.DataFrame(f)
    science = df.Science
    print(science)
    plt.hist(science, bins=10)
    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Score Distribution")
    plt.show()



show_science_distribution("labs\lab09\data\students.csv")
