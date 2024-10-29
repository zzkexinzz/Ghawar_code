import pandas as pd
import os
tests = pd.read_csv(r'C:\Users\yjy73\Desktop\tests.csv')
label = ''
with open(r'F:\STUDY\python_code\Pract_DA\prepocess\test_label.txt', 'w') as file:
    for i in tests['label']:
        label += (str(i)+',')
    file.write(label)
    