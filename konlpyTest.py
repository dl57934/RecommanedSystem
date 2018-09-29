from konlpy.tag import Twitter
import pandas as pd

csv = pd.read_csv('./eyeshadow.csv')
type = {'건성': 0, '지성': 1, '중성': 2, '복합성': 3, '민감성': 4}
csv['type'] = csv['type'].map(type)
print(len(csv.loc[csv['type']==0,:]))