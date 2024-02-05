import agate
import pandas 
#from agate.stats import correlation
column_names=['s.no','value1','value2  ']
data=[
    (1,10,100),(2,20,200),(3,30,300)
]
table=agate.Table(data,column_names)
print("Tree Structure")
print(table)
print("column_names")
print(table.column_names)
print("statistics")
print(table.aggregate([

('Mean value1', agate.Mean('value1')),
('Mean value2', agate.Mean('value2'))]))
df=pandas.DataFrame(data,columns=column_names)
matrix=df.corr()
print(matrix)
