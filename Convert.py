import pandas as pd

def To_excel(stores  , name = "excel.xlsx" ,path = '' , _index = True):
    excel = pd.DataFrame(stores)
    if(path == ""):
        excel.to_excel(name , index= _index)
    else : 
        path += '\\' + name
        excel.to_excel(path , index= _index)


def To_json(stores , name = "json.json" , path = ''):
    json = pd.DataFrame(stores)
    if(path == ""):
        json.to_json(name ,orient="records" , indent= 4 )
    else : 
        path += '\\' + name
        json.to_json(path , orient="records" , indent= 4 )


def To_csv_txt(stores , name = "csv.csv" , path ='', _index = False):
    csv = pd.DataFrame(stores)
    if(path == ""):
        csv.to_csv(name , sep='\t' ,index= _index )
    else : 
        path += '\\' +  name
        csv.to_csv(path , sep='\t' , index= _index)





