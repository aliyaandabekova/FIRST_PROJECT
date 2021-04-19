# data = ['Wt', 'Ht', 342432423424324, 5.996, 5.77778,
        'Insurance_History_2', 34243242342432124545312312534534534, 'Insurance_History_4',
        'Insurance_History_5', 'Insurance_History_7', 234242049004328402384023849028402348203,
        55, 66, 11, 'Medical_Keyword_3',
        'Medical_Keyword_4', 'Medical_Keyword_5', 'Medical_Keyword_6', 34243242342432124545312312534534534534503495345,
        'lalalalallalalalalalalalalalalala', 23409284028430928420483209482904380428, 'Medical_Keyword_10',
        'Medical_Keyword_11',
        92384923849023849023842903482934324290, 93429423018319238192004829423482942, 'Medical_Keyword_14',
        'Medical_Keyword_15',
        'Medical_Keyword_16', 5.888, 'Medical_Keyword_18asfdasfdasfdasfdasdfasdfas', 'Medicagsfgsfgsfkgjsfkg',
        9.131, 0.978, 'Famidasdasdlasdlaspdlaspdlasp2948203948',
        'Familygsdglksflg2849023840923;fksdkgsd234234234238409238490238', 'Family_Hist_4',
        'Family_Hist_5', 9.19, 'Medical_History_2', 'Medical_History_3', 'Medical_History_4',
        13, 'Medical_History_6', 'Medical_History_7', 111, 'Medical_History_9',
        123.7773, 'Medical_History_41', 55823428882482374824828472348, 'Product_Info_3', 1111111111111111111111,
        'Product_Info_5',
        ]
#
# print("1-СПОСОБ")
# print(len(data))
# i = 0
# while i < len(data):
#     obj = data[i]
#     if isinstance(obj,float):
#         if obj % 1 >= 0.8 or obj % 1 <= 0.2:
#             data[i] = round(obj)
#         else:
#             data[i] = int(obj)
#     elif isinstance(obj,int):
#         if len(str(obj)) >= 20:
#             del data[i]
#             i -= 1
#     elif isinstance(obj,str):
#             if len(obj) > 50:
#                 del data[i]
#                 i -= 1
#     i += 1
# print(data)
# print("ДОДЕЛАНО")

# clear_data = []
# i = 0
# while i < len(data):
#     obj = data[i]
#     if isinstance(obj,float):
#         if obj % 1 >= 0.8 or obj % 1 <= 0.2:
#             clear_data.append(round(obj))
#         else:
#             clear_data.append(int(obj))
#     elif isinstance(obj,int):
#         if len(str(obj)) <= 20:
#             clear_data.append(str(obj))
#     elif isinstance(obj,str):
#         if len(obj) < 50:
#             clear_data.append(obj)
#     i -= 1
#     print(clear_data)