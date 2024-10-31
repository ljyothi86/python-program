"""
import numpy as np
import pandas as pd
a=np.arange(0,11,2)
b=pd.Series(a)
print(b)
x=pd.Series(a,index=['jyo','navy','madhu','divya','arya','aadhya'])
print(x)
m=pd.Series(50,index=[10,20,30,40,50])
print(m)
s=pd.Series({1:'a',2:'b',3:'c'})
print(s)
s5=pd.Series([10,20,30,40,50])
print(s5)
s6=pd.Series([10,20,30,40,50])
print(s6)
s7=pd.Series('MANGO')
print(s7)
"""
#mathamatical operation
"""
import numpy as np
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s*2)
print(s**2)
print(s[s>30])
print(s[s<40])
"""
"""
import pandas as pd
import numpy as np
s=pd.Series([10,20,30,40,50])
p=pd.Series([1,2,3,4,5])
print(s+p)
print(s.add(p))
"""
"""
import pandas as pd
import numpy as np
s=pd.Series([10,20,30,40,50])
p=pd.Series([1,2,3])
print(s.add(p,fill_value=0))
"""
"""
import pandas as pd
import numpy as np
x=np.arange(1,101,2)
s=pd.Series(x)
print(s)
print(s.head())
print(s.tail())
"""
#indexing and slicing
"""
import pandas as pd
s=pd.Series([10,20,30,40,50,60,70,80,90,99])
print(s)
print(s.loc[0:3])
print(s.loc[:])
print(s.loc[1:5])
print(s.loc[0:3])
print(s[0:6:2])
"""
#Creating a datafram using series
"""
import pandas as pd
import numpy as np
x=np.arange(1,21,2)

s=pd.Series(x)
d=pd.DataFrame(s)
print(d)
"""
"""
import numpy as np
import pandas as pd
x=np.array((['Rani','Krishna','Anil','Jyo'],['Kumari','KKv','Cse','Nive']))
d=pd.DataFrome(x)
print(d)
"""
#Row wise example:-
"""
import pandas as pd
l=[{'name':'Gopi','sirname':'krishna'},{'name':'vinod','sirname':'raju'}]
df1=pd.DataFrame(l)
print(df1)
for(row_index,row_value)in df1.interows():
    print('Row value is ::')
    print('/n Row index is ::',row_index)
    print(row_values)

"""
#column
"""

import pandas as pd
l=[{'name':'bachin','sunname':'jyothi'},{'name':'sree','sunname':'banu'}]
df1=pd.DataFrame(l)
print(df1)
for(col_index,col_value) in df1.iteritems():
    print(col_index,col_value)
"""
#homw work
"""
#1 set all the values of vowels to 10 and display the series?
import pandas as pd
vowels=pd.Series([1,2,3,4,5],index=list('aeiou'))
print(vowels)
print()
vowels[vowels!='nottex']=10
print(vowels)
#2 Divide all values of vowels by 2 and disply the serives?
import pandas as pd
vowels=pd.Series([1,2,3,4,5],index=list('aeiou'))
print(vowels)
print()
vowels[vowels!='notten']=10
print(vowels)
vowels=vowels/2
print(vowels)
#3 create another serives vowels having 5 elements with index lables 'a','e','i','o',and 'u' having vowels[2,5,6,3,8] respectively
import pandas as pd
vowels=pd.Series([2,5,6,3,8],index=list('aeiou'))
print(vowels)
#4 add vowels and vowels1 and assign the result to vowels3?
import pandas as pd
vowels=pd.Series([1,2,3,4,5],index=list('aeiou'))
print()
vowels[vowels!='notten']=10
vowels=vowels/2
vowels1=pd.Series([2,5,6,3,8],index=list('aeiou'))
vowels3=vowels1+vowels
print(vowels3)
#5 subract multiply and divide vowels by vowels1?
import pandas as pd
vowels=pd.Series([1,2,3,4,5],index=list('aeiou'))
print()
vowels[vowels!='notten']=10
vowels=vowels/2
vowels1=pd.Series([2,5,6,3,8],index=list('aeiou'))
vowels3=vowels1+vowels
print(vowels3)
subtract=vowels-vowels1
multiply=vowels*vowels
divide=vowels/vowels1
#6 alter the lables of vowels to ['A','E','I','O','u']
vowels1.index=['A','E','I','O','u']
print(vowels1)
"""
# siz of element nd array
"""
import numpy as np
import sys
l=[10,20,30,40,50,60,70,80,90,20,45,79,90,45,30,20]
a=np.array([10,20,30,40,50,60,70,80,100,120,40,120])
print('the siz of list:',sys.getsizeof(l))
print('the siz of ndarray:',sys.getsizeof(a))
"""
"""
l=[10,20,30]
type(1)
"""


 
