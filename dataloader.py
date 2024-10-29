import pandas as pd

class DATALOADER:
    def __init__(self, path):
        self.path = path
    
    def extract_data(self,):
        file_name = self.path.split('\\')[-1]
        print(f'Extracting data from {file_name}')
        return pd.read_csv(self.path)

if __name__ == "__main__":

    path = r'F:\STUDY\python_code\Pract_DA\MIMICIII\ADMISSIONS.csv'
    dl = DATALOADER(path)
    data = dl.extract_data()
    print(data)