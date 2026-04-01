import pandas as pd


def explore_data(filename):
    info = {"total_students":None,"subjects":None,"math_average":None,"highest_math_student":None}

    df = pd.read_csv(filename)

    size = df.shape
    print(size)

    subject = list(df.columns)
    subject = [subject[2],subject[3],subject[4]]


    info["total_students"] = size[0]
    info["subjects"] = subject
    info["math_average"] = round(float(df["Math"].mean()),1)
    info["highest_math_student"] = None
    
    print(df)
    print("exit function")

    return info



result = explore_data("labs\lab09\data\students.csv")
print(result)

#Push
