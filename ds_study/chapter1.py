# 실습
# 1.1부터 100까지의 합계를 출력하시오.(for문)
total=0
for i in range(1,101):
    total+=i
print(total)    

# 2.1부터 100 사이의 정수 중 짝수만 출력하시오.
for i in range(1,101):
    if(i%2==0):
        print(i)
    
# 3.구구단 2단부터 9단까지 출력하시오.
for a in range(2,10):
    for b in range(1,10) :
        print(a, "x", b, "=", a*b)  
        
# 4.두 숫자를 입력하면 두 숫자의 차이에 대한 절대값을 반환하는 함수를 작성하고 테트스하시오.       
def diff_abs(a,b):
     return abs(a-b)
 
x=int(input("첫 번째 숫자 입력: "))
y=int(input("두 번째 숫자 입력: "))
 
result=diff_abs(x,y)
 
print("두 숫자의 차이의 절대값: ", result)

# 5.1부터 500 사이의 임의의 정수 50개를 생성한 뒤, 평균, 합계, 표준편차를 출력하시오.
import random
import statistics

numbers=[random.randint(1,500) for i in range(50)]

total=sum(numbers)

avg=total/len(numbers)

std=statistics.stdev(numbers)

print("생성된 숫자:", numbers)
print("합계:", total)
print("평균:", avg)
print("표준편차:", std)

# 다른 방법
import random
import math

numbers=[random.randint(1,500) for i in range(50)]

total=sum(numbers)
avg=total/len(numbers)

var=0
for x in numbers:
    var+=(x-avg)**2
    
var=var/len(numbers)
std=math.sqrt(var)    

print("합계:", total)
print("평균:", avg)
print("표준편차:", std)