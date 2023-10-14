import openpyxl
import pandas as pd
import itertools

if __name__ == "__main__":
    # 写数据到excel
    data1 = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']
    }
    df = pd.DataFrame(data1)
    # df.to_excel('E:\demo.xlsx', index=True)
    # 打开文件
    data = pd.read_excel('E:\demo.xlsx')
    excelBook = data.values
    excelBook = iter(excelBook)
    while True:
        try:
            row = next(excelBook)
            print(row[1])
        except StopIteration:
            exit(0)
    # 修改Excel文件
    wb = openpyxl.load_workbook('E:\demo.xlsx')
    # 获取指定sheet
    sheet = wb['Sheet1']
    # 修改单元格数据
    sheet['B2'] = "updated value"
    # 添加新的sheet
    new_sheet = wb.create_sheet("sheet2")
    # 保存修改后的excel文件
    wb.save('E:\demo_modified.xlsx')
