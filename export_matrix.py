import pandas as pd
import glob
import os


skipdir = "SKIP Exports"


def load_data(dir):
    to_return = []
    files = glob.glob(os.path.join(dir,"*xlsx"))
    for i in files:
        path = os.path.join(os.getcwd(),i)
        xl = pd.ExcelFile(path)
        df = pd.read_excel(path, sheet_name=xl.sheet_names[0])
        
        df.columns = df.iloc[0]
        df = df.iloc[1:].reset_index(drop=True)
        
        to_add = (df,xl.sheet_names[0])

        to_return.append(to_add)
    return tuple(to_return)

helpstr = "Need Help to perform task (Never done)"
trainstr,taskstr,modstr = "Trainee","Task","Module"


def create_matrix(data):
    for i in data:
        df = i[0]
        sheetname = i[1] + ".xlsx"
        df.dropna(subset=[helpstr],inplace=True)
        df.to_excel(sheetname,index=False)
        
        print(df)
        # for item in all_trainees:
        #     cur_item = df.drop(
        #         df[df[trainstr] != item].index, inplace=False)
        #     cur_item.dropna(subset=[helpstr],inplace=True)
        #     cur_item.to_excel(writer,sheet_name=str(item))


dataset = load_data(skipdir)

create_matrix(dataset)