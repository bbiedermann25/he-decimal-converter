import pandas as pd


index = 0
data = pd.read_csv("Health Equity Data Entry - November 2020 - Week of Nov. 1.csv",header = 2)
county_column = data[['Unnamed: 0']]
data = data.drop(columns = ['Unnamed: 0','Unnamed: 1'])
column_names = ['White','Black/African American','Asian',
                        'American Indian/Alaska Native','Native Hawaiian/Pacific Islander',
                        '2+ races', 'Other', 'Unknown', 'Hispanic (all races)',
                        'Non-Hispanic', 'Not Specified', 'Cumulative Cases','Race Total',
                        'Ethnicity Total']

test_colums = ['White','Black/African American','Asian','American Indian/Alaska Native',
               'Native Hawaiian/Pacific Islander','2+ races', 'Other', 'Unknown',
               'Hispanic (all races)','Non-Hispanic', 'Not Specified','Race Total',
               'Ethnicity Total']
cleaned = pd.DataFrame()
itr = 0
while (data.empty == False):
    if itr == 0:
        cleaned = pd.concat([county_column, data[column_names]], axis=1)
        data = data.drop(columns = column_names)
        itr = 1
    else:
        c = {}
        idx = 0
        while idx < len(column_names):
            name = column_names[idx] + '.' + str(itr)
            c[name] = column_names[idx]
            idx += 1
        data = data.rename(columns = c)
        cleaned = cleaned.append(pd.concat([county_column, data[column_names]], axis=1))
        data = data.drop(columns = column_names)
        itr += 1
            
cleaned.reset_index(drop=True, inplace=True)
for i in column_names:
    x = pd.to_numeric(cleaned[i], errors='coerce')
    cleaned[i] = x


rows = len(cleaned)
while index < rows:
    for j in test_colums:
        try:
            x = cleaned.at[index, j]
            if (x > 0) and (x < 1):
                cleaned.at[index, j] = cleaned.at[index, j] * cleaned.at[index, 'Cumulative Cases']

        except TypeError:
            pass
    index += 1


            
                
                
