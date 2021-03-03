''' main '''
# 使用自建的套件 myMath 來計算使用者輸入的五個數的平均值
from myMath.myStatistics import myMean
A = []
for i in range(5):
    A.append(float(input('請輸入數字: ')))
print('平均值: ',myMean(A))    
    
