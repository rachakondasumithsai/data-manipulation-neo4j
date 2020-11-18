import pandas as pd

# Extract all data on parks of Canada from the given CSV file, and create a new CSV file. (e.g.
# file1.csv)
df = pd.read_csv('original.csv',
                 index_col='ParkName')
df[df.Country.str.contains('CANADA', case=False)].to_csv('file1.csv')

# EFrom the newly created CSV file (file1.csv), extract data on ParkName, State, partySize,
# BookingType, RateType, Equipment, and create another CSV file (e.g. file2.csv)
data = pd.read_csv('file1.csv',
                   index_col='ParkName')
df1 = pd.DataFrame(data, columns=["State", "partySize", "BookingType", "RateType", "Equipment"])
df1.to_csv('file2.csv')

# In the newly created CSV file (file2.csv), scan the Equipment column, and replace all “less
# than” with “LT” [e.g. less than 30 ft. after transforming LT30ft], and replace “Single tent” with
# “ST”, and create another CSV (e.g. file3.csv)
df2 = pd.read_csv('file2.csv',
                  index_col='ParkName')
# Values to find & their replacements
find = ['Less than 20ft', 'Less than 30ft', 'Less than 40ft', 'Single Tent']
replace = ['LT20ft', 'LT30ft', 'LT40ft', 'ST']
# Select column (can be A,B,C,D)
col = 'Equipment'
# Finding & replacing values in the selected column
df2[col] = df2[col].replace(find, replace)
df2.to_csv('file3.csv')

# Considering a subset of final CSV file (file3.csv) [Consider parks of “NS” only] as the input
# (file4.csv), build a graph using Neo4j.
df3 = pd.read_csv('file3.csv',
                  index_col='ParkName')
df3[df3.State.str.contains('NS', case=False)].to_csv('file4.csv')
