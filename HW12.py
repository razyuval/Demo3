import numpy as np
import pandas as pd

# 1 + 2
g= np.random.randint(0, 9,(3 ,3))
print("in array \n", g)

if len(g[g==0])==0:
    print("there are no zeros in the array")
else:
    print(format("there are %d zeros in the array") % len(g[g==0]) )


# 3
x= np.empty(38-12)
x = np.arange(12,38,1)
print("#3 array \n",  x)

# 4

print("#4 array in reverse \n ",  x[::-1])



# 5
dict = {
    'Yuval' :123 ,
    'Meirav' : 234,
    'Hadas':345,
    'Dekel': 456,
    'Nofar': 567

}

S = pd.Series(dict)

print ("#5 Series: \n", S)

# 6

nts = pd.Series(x)

print(nts)

# 7


import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = myclient["ex12_db"]
mycol = mydb["ex12_col"]
# #Create Data
# mylist = [
# {'name':'Efi','Address':'Haornim 42'},
# {'name':'Liad','Address':'Haornim 43'},
# {'name':'Yuval','Address':'shvil kislev 23'},
# {'name':'Ella','BlaBla':'kdksms'},
# {'name':'Barucv','POBox':'37611'},
# {'name':'Cruvi','Age':'34'},
# {'name':'Arik','Bike':'Honda'},
# {'name':'Bentz','Bike':'Ducati'},
# ]
# x=  mycol.insert_many(mylist)
# print(x.inserted_ids)

#Read data and write to csv
data = pd.DataFrame(list(mycol.find()))
data.to_csv("data.csv")


