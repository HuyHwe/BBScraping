import pandas as pd
# stores = [
#     {
#         "storeName": "Cửa hàng A",
#         "address": "123 Đường Lê Lợi, Quận 1, TP.HCM",
#         "activeTime": "8:00 AM - 10:00 PM",
#         "price": "200,000 - 500,000 VND",
#         "canBeOrderAt": "App A",
#         "phone": "090-123-4567",
#         "rating": 4.5,
#         "mapLink": "http://maps.example.com/storeA"
#     },
#     {
#         "storeName": "Cửa hàng B",
#         "address": "45 Đường Cầu Giấy, Quận Cầu Giấy, Hà Nội",
#         "activeTime": "9:00 AM - 11:00 PM",
#         "price": "150,000 - 300,000 VND",
#         "canBeOrderAt": "App B",
#         "phone": "091-234-5678",
#         "rating": 4.2,
#         "mapLink": "http://maps.example.com/storeB"
#     },
#     {
#         "storeName": "Cửa hàng C",
#         "address": "678 Đường Nguyễn Huệ, Quận 1, TP.HCM",
#         "activeTime": "10:00 AM - 9:00 PM",
#         "price": "100,000 - 250,000 VND",
#         "canBeOrderAt": "App C",
#         "phone": "092-345-6789",
#         "rating": 4.7,
#         "mapLink": "http://maps.example.com/storeC"
#     },
#     {
#         "storeName": "Cửa hàng D",
#         "address": "90 Đường Võ Văn Kiệt, Quận Ninh Kiều, Cần Thơ",
#         "activeTime": "7:00 AM - 9:00 PM",
#         "price": "180,000 - 350,000 VND",
#         "canBeOrderAt": "App D",
#         "phone": "093-456-7890",
#         "rating": 4.8,
#         "mapLink": "http://maps.example.com/storeD"
#     },
#     {
#         "storeName": "Cửa hàng E",
#         "address": "112 Đường Trần Phú, Quận Hải Châu, Đà Nẵng",
#         "activeTime": "8:30 AM - 10:30 PM",
#         "price": "220,000 - 400,000 VND",
#         "canBeOrderAt": "App E",
#         "phone": "094-567-8901",
#         "rating": 4.3,
#         "mapLink": "http://maps.example.com/storeE"
#     },
#     {
#         "storeName": "Cửa hàng F",
#         "address": "75 Đường Phan Chu Trinh, TP. Đà Lạt, Lâm Đồng",
#         "activeTime": "6:00 AM - 8:00 PM",
#         "price": "90,000 - 200,000 VND",
#         "canBeOrderAt": "App F",
#         "phone": "095-678-9012",
#         "rating": 4.1,
#         "mapLink": "http://maps.example.com/storeF"
#     },
#     {
#         "storeName": "Cửa hàng G",
#         "address": "20 Đường Lê Duẩn, Quận Thanh Khê, Đà Nẵng",
#         "activeTime": "7:30 AM - 10:00 PM",
#         "price": "120,000 - 280,000 VND",
#         "canBeOrderAt": "App G",
#         "phone": "096-789-0123",
#         "rating": 4.6,
#         "mapLink": "http://maps.example.com/storeG"
#     },
#     {
#         "storeName": "Cửa hàng H",
#         "address": "15 Đường Hùng Vương, TP. Huế, Thừa Thiên Huế",
#         "activeTime": "9:00 AM - 11:00 PM",
#         "price": "180,000 - 330,000 VND",
#         "canBeOrderAt": "App H",
#         "phone": "097-890-1234",
#         "rating": 4.0,
#         "mapLink": "http://maps.example.com/storeH"
#     },
#     {
#         "storeName": "Cửa hàng I",
#         "address": "30 Đường Bạch Đằng, Quận Sơn Trà, Đà Nẵng",
#         "activeTime": "8:00 AM - 8:00 PM",
#         "price": "160,000 - 350,000 VND",
#         "canBeOrderAt": "App I",
#         "phone": "098-901-2345",
#         "rating": 4.9,
#         "mapLink": "http://maps.example.com/storeI"
#     },
#     {
#         "storeName": "hugn vu",
#         "address": "88 Đường Nguyễn Trãi, Quận 5, TP.HCM",
#         "activeTime": "10:00 AM - 9:30 PM",
#         "price": "200,000 - 450,000 VND",
#         "canBeOrderAt": "App J",
#         "phone": "099-012-3456",
#         "rating": 4.4,
#         "mapLink": "http://maps.example.com/storeJ"
#     }
# ]
def To_excel(stores  , name = "excel.xlsx" ,path = '' , _index = False):
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

# def To_txt(stores , name = "text.txt" , path ="", _index = True):
#     csv = pd.DataFrame(stores)
#     if(path == ""):
#         csv.to_csv(name , sep='\t' ,index= _index )
#     else : 
#         path += name
#         csv.to_csv(path , sep='\t' , index= _index)



