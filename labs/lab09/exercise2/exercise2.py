import pandas as pd

def compare_averages(filename):
    subject = []
    result = {}
    f = pd.read_csv(filename)
    df = pd.DataFrame(f)
    column = df[["Math","Science","English","Physics","Chemistry"]]
    print(column)
    
    
compare_averages("labs\lab09\data\students.csv")