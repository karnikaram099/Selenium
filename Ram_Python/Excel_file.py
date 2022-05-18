# import xlrd
# path = r"C:\Users\karni\OneDrive\Desktop\Sample 1.xlsx"
# xl_obj = xlrd.open_workbook(path)
# xl_sheet = xl_obj.sheet_by_name(RAM)
# data = xl_sheet.get_rows()
# objects = {row[0].value:(row[1].value, row[2].value) for row in data}
# print(objects)


# #print(data)
# #for row in data:   #    print(row)
# for row in data:
#     print(row[0].value, row[1].value)

"""ex"""
import time

import xlrd
# path = r'https://d.docs.live.net/56d17557817a74f2/Documents/register.xlsx'
# path1 = r"C:\Users\karni\OneDrive\Documents\register.xlsx"
# sp =xlrd.open_workbook(path1)
# xl_sheetname =sp.sheet_by_name("login")
# data = xl_sheetname.get_rows()
# # objects = {rows[0].value: rows[1].value for rows in data}
# # print(objects)
# # for i in data:print(i)
# # print(data)

# import xlrd
# path3 = r"C:\Users\karni\OneDrive\Documents\Sample_Practice1.xlsx"
# pp = xlrd.open_workbook(path3)
# sh = pp.sheet_by_name("Practice")
# data2 = sh.get_rows()
# for i in data2:
#     print(i)
# import xlrd
# path = r"C:\Users\karni\OneDrive\Documents\Sample_Practice1.xlsx"
# a1 = xlrd.open_workbook(path)
# a2 = a1.sheet_by_name("Practice ")
# a3 = a2.get_rows()
# for i in a3:
#     print(i)

with open("sample.html") as f:
    with open("sample2.txt") as f1:
         a = f1.read()
         b = f.read()
         if a in b:
             print("True")
         else:
             print("False")













