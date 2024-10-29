from dataloader import DATALOADER

path = r'F:\STUDY\python_code\Pract_DA\MIMICIII\ADMISSIONS.csv'
111
dl = DATALOADER(path)
data = dl.extract_data()
print(data)