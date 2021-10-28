"""
溫度露點差 與 PM2.5之比較圖    
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling

def TEMP_def(row):
    return row['TEMP'] - row['DEWP']


df = pd.read_csv('a.csv')
print(f'原本:{len(df)}')
df = df.dropna(axis=0, how='any')
print(f'刪除後:{len(df)}')

a = df[['PRES', 'TEMP', 'Iws','DEWP','Is','Ir','pm2.5']]

a.insert(2, "Comparison", np.ones(41757))
a['Comparison'] = a.apply(TEMP_def, axis=1)

a.loc[df['pm2.5'] > 0, 'PM'] = int(0)
a.loc[df['pm2.5'] > 150, 'PM'] = int(1)

re = a[['pm2.5','PM', 'Comparison']]
t_i = 0
m_i = 0
def test_view(row):
    global t_i
    global m_i
    if row['PM'] == 0 :
        t_i = t_i + 1
        if row['Comparison'] < 10:
            m_i = m_i +1

re.apply(test_view, axis=1)
print(f'{m_i}/{t_i}')


x =  a[['Comparison']].to_numpy()
y = a[['pm2.5']].to_numpy()
plt.title('PM2.5 and depression of the dew point')
plt.scatter(x, y, s=5)
plt.xlabel('depression of the dew point')
plt.ylabel('PM2.5')
plt.savefig('foo.png')
#plt.show()