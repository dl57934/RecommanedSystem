import pandas as pd

csvData = pd.read_csv('data/sunblocktest.csv')
newData = pd.DataFrame({'userId':'0', 'name':'니아바이 김상벽', 'popId':'0',
                        'rate':'4.33', 'review':'피부에 너무 좋아요', 'type':'건성'}, index=[0])
print(newData.loc[0])

print(csvData.loc[0])
csvData.loc[len(csvData)] = newData.loc[0]
csvData.to_csv('./data/sunblocktest.csv')