from linkFetch import getLinksByPrompt
from storeFetch import storeFetcher
from Convert import To_excel, To_json, To_csv_txt

def main():
    searchArea = input("Enter the area you want to search: ") # Tạo box nhập vùng tìm kiếm
    searchKeyword = input("Enter the keyword you want to search: ") # Tạo box nhập từ khóa quán ăn

    # Tạo box "Start"
    storeLinks = getLinksByPrompt(searchArea, searchKeyword)
    storeData = storeFetcher(storeLinks, 5)
    print("Done fetching data")

    # Tạo box cho export, khi nhấn vào export sẽ hiện ra menu để người dùng chọn định dạng file
    # while (True):
    #     export = input("chose your file format: 1. Excel 2. Json 3. Csv")
    #     if (export == "1"):
    #         To_excel(storeData  , name = "excel.xlsx" ,path = '')
    #         break
    #     elif (export == "2"):
    #         To_json(storeData , "json.json" ,"")
    #         break
    #     elif (export == "3"):
    #         To_csv_txt(storeData , "csv.csv" , "")
    #         break
    #     else: print("Invalid option")
if __name__ == "__main__":
    main()