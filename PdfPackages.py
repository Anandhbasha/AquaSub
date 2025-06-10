# pdfplumber
import pdfplumber
# with pdfplumber.open(r'C:\Users\Admin\Downloads\Core Java Syllabus and Advance Java(J2EE) 2022 (1).pdf') as file:
#     for page in file.pages:
#         text = page.extract_text()
#         table = page.extract_table()
#         if table:
#             for table in table:
#                 for row in table:
#                     print(row)


# with pdfplumber.open(r'C:\Users\Admin\Downloads\Core Java Syllabus and Advance Java(J2EE) 2022 (1).pdf') as file:
#     for page in file.pages:
#         exactArea = page.crop((100,100,200,400))
#         text = exactArea.extract_text()
#         print(text)

        # print(text)
        # print(table)
import pandas as pd
newData = []
existingInfo = [
    ['S.no', 'Name', 'Age', 'City'],['1', 'xyz', '28', 'CBE'],['2', 'murugan', '22', 'CBE']
]

with pdfplumber.open(r"C:\Users\Admin\Downloads\save.pdf") as file:
    for page in file.pages:
        table = page.extract_table()
        for row in table:
            newData.append(row)

pdfData = pd.DataFrame(newData[1:],columns=newData[0])
mixedData = pd.DataFrame(existingInfo[1:],columns=existingInfo[0])

newComposed = pd.concat([pdfData,mixedData],ignore_index=True)
# newComposed['S.no'] = range(1,len(newComposed)+1)
newComposed.to_csv("exporeted.csv",index=False)
print("Suceesfully Done")
# pypdf2
