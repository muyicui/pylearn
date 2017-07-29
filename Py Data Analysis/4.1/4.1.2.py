from pandas import read_table
import muyilib as my
df = read_table(
    my.findpath_da("4.1//2.txt")
)
df

df = read_table(
    my.findpath_da("4.1//2.txt"),
    names=['age', 'name'], 
    sep=','
)
df
