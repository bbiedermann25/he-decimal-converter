import pandas as pd

index = 0
data = pd.read_csv("Health Equity Data Entry - December 2020 - Week of Dec. 1.csv",header = 2)
newdf = data[['Unnamed: 0','White','Black/African American','Asian',
                      'American Indian/Alaska Native','Native Hawaiian/Pacific Islander',
                        '2+ races', 'Other', 'Unknown', 'Hispanic (all races)',
                        'Non-Hispanic', 'Not Specified', 'Cumulative Cases','Race Total',
                        'Ethnicity Total']]
county_column = data['Unnamed: 0']
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
##cleaned = pd.DataFrame()
##while (data.empty == False):
##    if i == 0:
##        cleaned = pd.concat(county_column, data[column_names])
##        data = data.drop(columns = column_names)
##        i = 1
##    else:
##        index = 1
##        c = {}
##        while index < len(column_names):
##            name = column_names[index] + '.' + str(i)
##            c[name] = column_names[index]
##            data = data.drop(name)
##            index += 1
##
##        data.rename(c)
##        cleaned.append(pd.concat(county_column, data[column_names]))
            

for i in column_names:
    x = pd.to_numeric(newdf[i], errors='coerce')
    newdf[i] = x


rows = len(newdf)
edit = pd.DataFrame(columns = ['Unnamed: 0','White','Black/African American','Asian',
                      'American Indian/Alaska Native','Native Hawaiian/Pacific Islander',
                        '2+ races', 'Other', 'Unknown', 'Hispanic (all races)',
                        'Non-Hispanic', 'Not Specified', 'Cumulative Cases','Race Total',
                        'Ethnicity Total'])

while index < rows:
    for j in test_colums:
        try:
            x = newdf.at[index, j]
            if (x > 0) and (x < 1):
                newdf.at[index, j] = newdf.at[index, j] * newdf.at[index, 'Cumulative Cases']

        except TypeError:
            pass
    index += 1


            
                
                
