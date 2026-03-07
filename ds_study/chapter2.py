# 1 
import pandas as pd

age=pd.Series([25, 34, 19, 45, 60])
age
type(age)

data=['spring', 'summer', 'fall', 'winter']
season=pd.Series(data)
season

season.iloc[2]

# 2
import pandas as pd

score=pd.DataFrame([[85,96,40,95],
                    [73,69,45,80],
                    [78,50,60,90]
                    ])

score
type(score)

score.index
score.columns

print(score.iloc[1,2])


# 1차원 배열 numpy<->pandas
import pandas as pd
import numpy as np

w_np=np.array([65.4, 71.3, np.nan, 57.8])
weight=pd.Series(w_np)
weight

w_np2=pd.Index.to_numpy(weight)
w_np2

# 2차원 배열 numpy<->pandas
import pandas as pd
import numpy as np

s_np=np.array([[85,96,40,95],
               [73,69,45,80],
               [78,50,60,90]
                ])
s_np
score2=pd.DataFrame(s_np)
score2

score_np=score2.to_numpy()
score_np

# 실습
# 1. 다음의 월평균기온 통계표를 pandas 데이터프레임에 저장하시오.
import pandas as pd

data = [
    [-0.1, 0.0, -0.1, -0.2],
    [1.8, 2.0, 1.6, 1.6],
    [6.4, 6.8, 5.8, 5.9],
    [12.3, 12.9, 11.5, 11.5],
    [17.9, 18.5, 17.1, 17.1],
    [22.2, 22.8, 21.6, 21.5]
]

index = ['1월','2월','3월','4월','5월','6월']
columns = ['전북','전주','군산','부안']

temp = pd.DataFrame(data, index=index, columns=columns)

temp

# 2.절대위치 인덱스를 이용하여 전주의 3월 평균 기온을 출력하시오.
temp.iloc[2,1]

# 3.절대위치 인덱스를 이용하여 부안의 4월 평균 기온을 출력하시오.
temp.iloc[3,3]

# 4.레이블 인덱스를 이용하여 군산의 1월 평균 기온을 출력하시오.
temp.loc['1월','군산']

# 5.레이블 인덱스를 이용하여 전북의 6월 평균 기온을 출력하시오.
temp.loc['6월','전북']