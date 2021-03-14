import pandas as pd

# create dataframe
df_marks = pd.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
     'physics': [68, 74, 77, 78],
     'chemistry': [84, 56, 73, 69],
     'algebra': [78, 88, 82, 87]})

# create excel writer
writer = pd.ExcelWriter('output1.xlsx')
# write dataframe to excel sheet named 'marks'
df_marks.to_excel(writer, 'marks')
# save the excel file
writer.save()
print('DataFrame is written successfully to Excel Sheet.')
