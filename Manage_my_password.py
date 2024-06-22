import pandas as pd
import numpy as np
file_path = 'private_pass.csv' # important row = 3, column = 3
passdata = pd.read_csv(file_path, delimiter='\t')
passdata.columns = passdata.columns.str.strip()

class passmanazer():
    def __init__(self, safekey) -> None:
        _safekey = str(safekey)
    def savepass(self,your_key : str, password : str):
        your_key = str(your_key)
        password = str(password)
        global passdata
        x, y = (passdata.shape)
        data = {
            'key' : your_key,
            'passwords' : password,
            'counter' : x+1
        }
        passdata = passdata._append(data, ignore_index = 1)
        # Write the updated DataFrame back to the CSV file
        passdata.to_csv(file_path, sep='\t', index=False)
        print("saved")

    def getpassword(self, key : str):
        key = str(key)
        try:
            index = list(passdata[passdata['key'].str.strip() == key].index)
            pas = list(passdata.iloc[index, 1])
            pas = pas[0].strip()
            print(pas)
        except:
            print("invalid key")

    def changepass(self, key : str, oldpass : str, newpass : str):
        key = str(key)
        oldpass = str(oldpass)
        newpass = str(newpass)

        index = list(passdata[passdata['key'].str.strip() == key].index)
        _oldpass = list(passdata.iloc[index, 1])
        _oldpass = _oldpass[0].strip()

        if (oldpass == _oldpass):
            passdata.loc[index, 'passwords'] = newpass
            passdata.to_csv(file_path, sep='\t', index=False)
            print("updated")

        else:
            print("Wrong oldpass")

    def deletepass(self, key):
        pass

        
def main():
    manager = passmanazer("safekey")
    manager.savepass()
    manager.getpassword()
    manager.changepass()
    manager.deletepass()

if __name__ == "__main__":
    main()