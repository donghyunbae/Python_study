import numpy
import sys
import copy
from random import randint

#=======================================================================================================================
#<data 타입>
'''
mutable 객체 : 수정 가능 (list, set, dict)
immutable 객체 : 수정 불가능 (int, float, complex, bool, string, tuple, frozen set)
'''

#=======================================================================================================================
#<integet>
#int is immutable object
a = 10
print(id(a))

a= a+1
print(id(a))

#integer는 -5~256 정수는 항상 캐시해둔다 (보관)
#두 객체가 같은지 확인 하는 방법은 'is' 사용, 객체의 값이 같은지 확인하기 위해서는 '=='을 사용한다.
a = 256
b= 256
print(a is b)

#=======================================================================================================================
#<float>
#integer -> float 구분하는 방법은 소숫점 '.'의 유무 -> '1.' 은 float 타입임
print(type(1.))

#같은 값을 가진 실수 객체라고 해도 동일한 객체가 아니기 때문에 is 연산자 대신 ==연산자로 비교해야한다.

a = 1.1
b = 1.1
print(a is b)               # a와 b의 객체는 서로 다르므로 false가 나옴
print(a==b)                 # 그러나 값은 같기 때문에 true

a = 0.1 + 0.1 + 0.1         #파이썬에서 소수는 부동소수로 표현된다. 정확한 실수 값을 표현하는 대신에 근사값으로 표현을 한다.
print(a)                    #0.300000000000004 임 0.3이 아님
print(a==0.3)
#이럴때 round함수를 이용하면 됨
print(round(a,1)==0.3)          #round(argument, 자리수)

#=======================================================================================================================
#<string>
print(type('a'))

#줄바꿈 사용 '\n'
print("hello\npython")

#string 결합 가능 (+)
print("hello" + "python")

#문자열 * 숫자 가능
print("@" * 50)

#indexing
str = 'Python'
print(str[0])
print(str[1:])
print(str[0] + str[1:])

########문자열은 수정이 불가능 함.
#ex)
#str = 'python'
#print(str[0])                   # 'p'
#str[0] = 'b'                    # error

# 수정을 하기 위해서는 새로운 객체(object)를 생성하거나 replace함수를 사용해야함
#<수정>
a = 'abc'
print(a)
b = 'bbc'

#<replace 함수>
c = a.replace('a', 'b')
print(c)

#문자열의 객체 = a~z, A~Z, 0~9 , _ 만 있는 문자열은 기존 객체가 있다면 객체를 변경하지 않음
#즉,
a = 'abcdABCD1234_'
b = 'abcdABCD1234_'

print(id(a))
print(id(b))
print(a is b)                       #객체가 서로 같기 때문에 true임

#<주의사항>
#문자열 연산을 하더라도 객체는 변경되지 않는다. 그러나 새로운 변수에 대입할 경우 객체가 달라진다.
#ex
a1 = 'a'
a2 = 'bc'
b = 'abc'
print(a1 + a2 is b)                 #객체는 서로 다름
print(a1 + a2 == b)                 #그러나 객체의 값은 같음

#만약 여기서 항상 같은 객체로 처리하고 싶다면 'sys.intern' method를 사용하면 된다.

a = sys.intern(a1+a2)
b = sys.intern('abc')
print(a is b)                       #이렇게하면 true

#=======================================================================================================================
#<list>
#리스트는 대괄호[] 안에 각기 다른 타입의 데이터를 넣을 수 있음
mylist = [1, 1.0, 'a']
print(mylist)
print(type(mylist[0]))
print(type(mylist[1]))
print(type(mylist[2]))

#안에 원소가 같더라도 순서가 다르면 다른 리스트가 된다.
a = [1,2,3]
b = [1,3,2]
c = [1,2,3]
print(a is c)                       #원소가 같더라도 변수가 다르기 때문에 객체는 다른것임
print(a == b)

#복사
a = [1,2,3]
b = a                               #b에 a리스트 대입
c = copy.copy(a)                    #얕은복사?
d = copy.deepcopy(a)                #깊은복사?

print(id(a), id(b), id(c), id(d))       #대입하면 같은 객체를 갖지만, 복사하면 다른 객체가 생성됨.

#만약 여기서 b의 값을 바꾼다면?
b[0] = 100
print(a,b,c,d)                              #a의 원소에도 영향을 미침(객체가 같기때문에), 그러나 c와 d에서는 영향을 미치지 않음


#복합 객체의 복사
# 기존 리스트가 복합 객체의 경우 얕은복사를 하면 새로 생성된 리스트 객체의 원소가 기존 리스트 객체의 원소를 참조한다.

a = [['a', 'b', 'c'], [1,2,3]]
b = copy.copy(a)
print(a is b)                               #서로 객체는 다름 false
print(a,b)                                  #그러나 값은 같음 true

# 그렇기 때문에 둘중 어느 객체의 값을 변경하더라도 양쪽 객체의 값에 동일하게 반영된다.
a[0].append('hello')
print(a,b)

#깊은복사(deepcopy)의 경우에는 객체의 타입 (mutable/immutable)에 따라 달라짐
#mutable type : 수정 가능 -> 새로운 객체로 생성
#immutable type : 수정 불가능 -> 기존 객체 참조

a = [['a', 'b', 'c'], 1, 257]
b = copy.deepcopy(a)

print(a is b)
print(a[0] is b[0])                     #a[0] = list임(mutable type) -> 수정 가능 -> 새로운 객체로 생성
print(id(a), id(b))
#즉, 이경우에는 객체가 서로 다르기 때문에 a와 b중 하나를 append, pop를 사용해 수정하더라도 객체의 값이 서로 다르게 나옴(서로 객체에 영향을 주지 않음)

#그러나, immutable type의 경우
print(a[1] is b[1])
print(id(a), id(b))                     #a[0] = integer (immutable type) -> 기존 객체 참조

#=======================================================================================================================
#<slicing> [이상:미만:간격]
#list를 자르는 것. 말 그대로 슬라이싱하여 일부를 잘라냄

A = [1,2,3,4,5,6,7]
print(A[0:4:2])
print(A[4:])
print(A[:])
print(id(A))

#list의 크기를 나타내는 len()함수, 새로운 원소를 추가하는 append()메소드
print(len(A))
A.append(8)
print(id(A))
print(A)

#list안에 list
A = [[1,2,3],[4,5,6],[7,8,9]]       #dimension = 2
print(A[1])
print(A[0][1])

#slicing한 list는 원본에 영향을 주지 않는다.
A = [1,2,3,4,5,6,7]
B = A[0:4]
print(B)
B[0] = 0
print(B)
print(A)

#range 함수를 사용하여 연속적인 숫자로 구성된 리스트 생성
A = list(range(0,10))
print(A)
A.pop()
print(A)

#=======================================================================================================================
#<tuple> : list와 동일하나 수정은 할 수 없음 '소괄호()' 사용
T = (1, 0.01, 'a')          #여러 타입의 원소를 가질 수 있다.
print(type(T))
print(type(T[0]))
print(type(T[1]))
print(type(T[2]))

#slicing tuple
T = (1,2,3,4,5)
print(T[0:3])

#tuple은 서로 같은 원소라도 다른 객체임
a = (1,2,3)
b = (1,2,3)
print(a is b)

#tuple은 수정이 불가능하지만, list로 변환 후 다시 tuple로 변환하면 사용이 가능하다

a = (1,2,3)
b = list(a)
b[0] = 1
c = tuple(b)

print("a = ", a)
print("c = ", c)

#tuple은 immutable 객체지만 객체 값으로 mutable 객체에 대한 참조를 포함할 수 있다.
#tuple은 값을 변경할 수 없는 객체지만, 원소가 참조하고 있는 mutable객체의 값은 수정할 수 있다.
a = (1, 'abc', [1,2,3])
a_second_id = id(a[2])
a[2].append(4)
print(a)

#a[2] = 5                               #이렇게 다른 type의 객체로 변경할 수 없음

#tuple packing
t = 1,2                                 #packing
print(t)
x,y = t                                 #unpacking
print(x)
print(y)

#=======================================================================================================================
#<dictionary>
# {key : value} 가 하나의 쌍으로 이루어짐

A = {'apple':'사과', 'banana':'바나나', 'grape' : '포도'}
print(A['apple'])

#값 변경
A['apple'] = 'orange'                           #'사과' -> orange
print(A)

#key/ value로 분리하는 방법
A = {'apple':'사과', 'banana':'바나나', 'grape' : '포도'}
for key, value in A.items():
    print(key,value)

#=======================================================================================================================
#<set> 집합
#중복된 데이터가 없는 데이터타입

fruit_1 = {'apple', 'banana', 'orange'}
print(type(fruit_1))                              #<class 'set'>

fruit_2 = {'apple', 'banana', 'orange'}

#순서가 달라도, 원소값이 같기 때문에 같은 집합이다.
print(fruit_1 == fruit_2)

#집합에 특정 원소가 있는지 검사하는 방법
#'in' 사용

a = {1,2,2,3,4,1,2,5}                             #집합 생성 시 중복된 원소는 자동으로 제거됨.
print(a)

print(1 in a)                                     #1이 a에 있나요?

#=======================================================================================================================
#<제어문> Control Statement

#if문
#true / false 를 판정하여 다음 오는 블록의 코드를 실행함. 뒤에 무조건 ':' 콜론이 들어가야함. // 들여쓰기는 필수!


#예제 만들며 if문 연습
#숫자 맞추기게임 만들기!

'''
anwser = randint(0, 100)                                 #랜덤 숫자(0~100)중 1개를 생성

count = 0                                                #시도한 횟수 체크용

while True:
    number = int(input("내가 생각하는 정답을 입력하세요 : "))
    count += 1                                           #while문 반복하면서 count를 1씩 증가시킴 (**count+=1 -> count = count + 1 과 같음)

    if anwser < number:
        print("%d보다 작습니다." % number)

    elif anwser > number:
        print("%d보다 큽니다." % number)

    else :
        print("정답을 맞추었습니다. 시도한 횟수 : %d ." % count)
        break                                             #무한루프 빠져나오기
'''

#=======================================================================================================================
#<for문> : ~동안
#튜플, 리스트, 문자열 등 데이터 타입의 원소를 하나씩 가져오는 것을 반복하기 위해 사용

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:                                    #days에 값을 앞에서부터 차례대로 day에 넣는것을 반복
    print(day)

#enumerate
#index값을 같이 가져오기 위해선 'enumerate' 를 사용하면 된다.
for index, day in enumerate(days):
    print("일주일 중 %d 번째요일은 %s입니다." %(index+1, day))

#zip
#2개이상의 리스트 또는 튜플에서 원소를 튜플로 묶어서 가져올땐 'zip'을 사용한다.
english_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
korean_days =['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

#각 리스트 또는 튜플에서 원소를 한개씩 가져와 튜플로 묶음
#변수 2개를 사용해 다시 각각 값으로 받음

for E, K in zip(english_days, korean_days):
    print("%s is %s입니다." %(E, K))

#range(범위)
#일정 범위의 숫자까지 반복하기 위해 range사용

for k in range(0,10,2):                     #0이상 10미만 간격:2
    print(k)

#시작값이 0 이면 생각 가능
for k in range(10):
    print(k)


#<while문> : True인 동안만 작업을 반복
# 'continue' : 다음 줄에 있는 코드를 무시하고 반복문의 처음으로 되돌아감,
# 'break' : while문 중지
'''
# 예제
my_num = int(input('숫자를 입력하세요 : '))

count = 0
sum = 0

while True:
    count += 1                          #0부터 숫자를 하나씩 셈

    if count%2 == 0:                    #만약 현재숫자(count) 나누기 2의 나머지가 0일때 == 짝수일때, 다시 맨위로 올라가서 시작 (짝수는 무시하겠다는이야기)
        continue
    sum += count                        #짝수는 계산하지 않고, 홀수는 전부 결과(sum)에 더해 저장한다.

    if count >= my_num:                 # count(총 합)가 내가 입력한 my_num보다 크거나 같다면
        print('%d까지 홀수 합은 %d입니다.' %(my_num, sum))
        break
'''

#=======================================================================================================================
#<함수> funtion(arguments)
# 'def' 사용하여 함수를 정의함
# 함수에서 호출한 지점으로 리턴할 값을 'return'문에 적는다.

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

c = plus(3,2)
d = minus(10,3)
print(c)
print(d)


#전역변수에서도 사용 가능
a = 5
b= 5
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

print(plus(a,b))
print(minus(a,b))


#전역변수는 수정이 불가능하므로 수정하기 위해선 global 을 사용
a = 4
b= 4
def plus():
    global a
    global b
    a = 6
    b= 3
    return a+b

def minus():
    global a
    global b
    a = 10
    b = 7
    return a-b

print(plus())
print(minus())

