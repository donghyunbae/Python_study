import numpy as np

#넘파이 배열 : "N차원 배열 객체(ndarray)로 모든 원소는 같은 타입, 같은 크기를 가짐"
# 차원개수만큼의 정수로 인덱싱 된다.

a = np.array([0.1, 0.2, 0.3])
print(a)
print(type(a))              #ndarray형식의 type
print(a.dtype)              #실수의 default dtype : float64

x = [1,2,3]                 #이런식으로 미리 생성한 리스트를 사용해서도 넘파이 배열 생성 가능
b = np.array(x)
print(b)
print(b.dtype)              #정수의 default dtype : int32

'''
<data type>
- bool : true/false
- int8 : 8bit integer (-128~127)
- int16 : 16bit intege (-32768 ~ 32767)
- int32 : 32bit integer (-2147483648 ~ 2147483647)
    '
    '
    '
- uint8 : unsigned 8bit integer (0~255)
- uint16 : unsigned 16bit integer (0 ~ 65535)
- uint32 : unsigned 32bit integer (0 ~ 4294967295)

- float16 : 16bit float
- float32 : 32bit float
- float64 : 64bit float

- complex64 : 복소수, 32bit float type 2개로 실수와 허수를 나타냄
- complex128 : 복소수, 64bit float type 2개로 실수와 허수를 나타냄

'''

#=======================================================================================================================
#array배열의 type지정 호출
#배열 생성 시 dtype을 지정할 수 있음

a = np.array([1,2,3], dtype = np.float64)               #배열생성, dtype : float64
print(a)                                                #출력시, 리스트에 소숫점'.'이 붙은걸 확인할 수 있다.
print(a.dtype)
print(type(a[0]))

#'astype' method : Numpy배열의 dtype을 변경
a = np.array([1.5,2.1,3.1,4.11])
print(a)
print(a.dtype)

a = a.astype(np.int32)                                  #a를 32비트정수타입으로 변환 후 a에 저장
print(a)                                                #a출력. 소숫점 사라지고 정수부분만 남음

#=======================================================================================================================
# + 'numpy ndarray' 클래스
# numpy 배열의 타입은 'numpy ndarray'의 클래스임
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(type(a))                                          # class : ndarray 임을 확인할 수 있음

# <ndarray.ndim>
# 배열을 구성하는 차원의 개수.
print(a.ndim)

# <ndarray.shape>
print(a)
print(a.shape)
#2열 3행
'''
[1,2,3]
[4,5,6]
'''

# <ndarray.size>
# 모든 원소의 개수
print(a)
print(a.size)                                           # 6개

# <ndarray.dtype>
# dtype
print(a)
print(a.dtype)                                          #int32 타입

# <ndarray.itemsize>
# 배열 원소 하나의 바이트 크기
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.dtype)
print(a.itemsize)                                       #int32의 itemsize : 8byte

# <ndarray.data>
# 배열 원소를 실제로 저장하고 있는 버퍼(buffer)

# buffer란 ??? : 임시 저장공간, CPU와 보조 기억장치(HDD, SSD) 사이에서 사용되는 임시 저장 공간
#이 때 버퍼를 사용하게 됩니다. 버퍼는 CPU 내부에 있는 캐시메모리 보다는 느리지만 보조 기억 장치보다 훨씬 빠른 주기억 장치(RAM)를 이용합니다.
# 보조기억장치는 주기억장치의 버퍼로 마련해둔 공간에 데이터를 열심히 보내 쌓아 둡니다.
# CPU는 처리가 빠르므로 밀려있는 다른일을 처리한 후 시간이 남을때 가끔 버퍼를 확인하여 데이터가 모두 쌓였는지 확인하고 모두 쌓였다면 가져다 한꺼번에 처리합니다.
# 그 덕분에 CPU는 100퍼센트의 효율로 연산을 할 수 있습니다.
# 이렇게 버퍼라는 것은 속도차가 큰 두 대상이 입출력을 수행할 때 효율성을 위해 사용하는 임시 저장공간이라고 할 수 있겠습니다.
# ex ) 버퍼링이 걸린다..
print(a.data)

# <배열의 연산> max(), min(), sum(), mean()
b = np.array([1,2,3,4,5,6,7,8,9])
print(b)
print(b.max())
print(b.min())
print(b.sum())
print(b.mean())

#=======================================================================================================================
# <numpy array's num of dimension & scala of dimension>
# shape속성을 사용
# shape속성은 튜플로 출력되는데, 튜플의 원소 개수가 넘파이 배열의 차원 개수이며 각 항목의 값이 각 차원의 크기이다. 차원개수만 확인할 수 있는 ndim속성도 있다.

A = np.array([[1,2,3,4],[3,4,5,6],[10,11,12,14]])
print(A)
print(type(A[0]))                               #numpy.int32

# 차원개수 확인 (.ndim)
print(A.ndim)                                   #1차원

# 첫번째 차원의 크기, 두번째 차원의 크기 (행, 열)
print(A.shape)

# <3차원 배열>
C = np.array([[[1,2,3,4], [4,5,6,7], [8,9,10,11]], [[12,13,14,15], [16,17,18,19], [20,21,22,23]]])
print(C)
print(C.ndim)
print(C.shape)                                  #(2,3,4) = 첫번째 차원의 크기 : 2, 두번째 차원의 크기 : 3, 세번째 차원의 크기 4

# <배열의 원소 접근방법>
# index를 사용해서 접근하면 됨

# ex) 14에 접근해보자!
# 14는 첫번째차원 1번째, 2번째차원의 0번째, 3번째차원에서 2번째이므로
print(C[1,0,2])
# ex) 7에 접근하기
print(C[0,1,3])

#=======================================================================================================================
# <numpy배열의 시각화 방법>
'''
배열이 출력 시 어떻게 시각화 되는 것일까?
배열이 출력될 때 다음과 같은 규칙을 따른다.

- 마지막 차원은 왼쪽에서 오른쪽 방향으로 출력된다.
- 나머지 차원은 위에서 아래로 출력된다. 원소 간 구별을 통해서 빈줄을 추가한다.
- 만약, 1차원 넘파이 배열을 출력하면 하나의 행으로 출력된다 [1,2,3,4]
- 첫번째 차원(axis = 0) 방향으로 갈수록 차원 인덱스 값은 증가함. (인덱스의 최댓값 = shape속성에서 첫번째 차원의 크기 -1 이 됨.)
- 두번째 차원(axis = 1) 방향으로 갈수록 차원 인덱스 값이 증가. 

axis = 0 왼쪽->오른쪽
axis = 1 위 -> 아래
[[1,2,3,4]
[5,6,7,8]]

- 3차원 배열도 마찬가지이다. 3차원 이상부터는 원소 간 구분을 위해 빈 줄을 추가함
[[[ 1  2  3  4]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]

원소가 많을 경우 생략되어 출력됨. 그러나 전체 배열을 전부 출력하려면 'set_printoptions(threshold = maxsize)' 호출 뒤 출력하면 된다.
ex) 
np.set_printoptions(threshold=maxsize)
print(@@)
'''

#=======================================================================================================================
# <넘파이 배열과 파이썬 리스트 성능 비교>
# 넘파이 배열과 파이썬 리스트의 사용법은 비슷하다. 하지만 넘파이 배열이 좀 더 효율적으로 메모리에 데이터를 저장하기 때문에 빠른 연산이 가능하다.

# 넘파이 연산
A = np.array([1,2,4])
B = np.array([5,3,2])
print(A+B)

# <1차원 배열 사용 시 주의점>
print(A.shape)                  # (3,) 라고 나옴
# 언뜻보면 열벡터 같지만, 1차원 배열의 경우 행벡터와 열벡터의 구분 없이 사용된다.
# 그렇기에 자기 자신에 대한 행렬곱셈이 가능하다.

print(np.dot(A,A))              # [1,2,4] , [4,2,1]

# shape 속성을 강제로 지정할 경우에는 2차원 배열이 된다.
a = np.array([1,2,3,4])
a.shape = 1,4                   # 강제로 지정하면
print(a)                        # 2차원 행벡터가 됨!!! (1,4)
print(a.shape)

a.shape = 4,1                   # 2차원 열벡터가 됨 !! (4,1), 배열의 shape속성만 바꿈
print(a)
print(a.shape)                  #(4,1)
#이렇게 열벡터의 경우 1차원 배열의 원소들이 개별 1차원 배열로 바뀌고 줄단위로 구분되어 출력됨!!

#=======================================================================================================================
#<정해진 크기 배열 생성 함수
# 배열의 데이터 개수를 알고 있을 때 사용할 수 있는 함수
# 지정한 크기(shape)와 데이터 타입(dtype)을 갖는 배열을 생성한다는 점은 동일하며, 채워지는 값은 다름
# default dtype = 'float64'



# 'zeros 함수'는 배열의 모든 원소를 0으로 지정해준 크기의 배열을 생성한다.
A = np.zeros((1,2))
print(A)                                        # 모든 원소들을 0으로 바꿈
print(A.dtype)                                  # default dtype = 'float64' 이므로 [0. 0.] 으로 나오는 것임

# 'ones 함수'는 배열의 모든 원소를 1로 지정해준 크기의 배열을 생성한다!
A = np.ones((1,2))
print(A)
print(A.dtype)

# 'empty 함수'는 초기화되지 않도록 지정한 크기의 배열을 생성, 위 두함수와 달리 초기화하지 않기 때문에 생성 속도가 빠르다.
# 주의할 점 !!!!! : 메모리 상황에 따라 배열의 초기화된 데이터가 달라지기 때문에 0으로 배열이 채워질 거라고 가정하면 안된다.
A = np.empty((3,2))
print("empty type")
print(A)
print(A.dtype)

# 'random 함수'는 0-1 사이의 무작위 값으로 채워진 지정한 크기위 배열을 생성한다.
A = np.random.random((1,2))
print(A)

# 'randint 함수'는 지정한 범위 내의 무작위 값으로 채워진 크기의 배열을 생성
A = np.random.randint(1,20,(4,5))    #1~20까지 무작위 숫자를 shape = 4,5 로 생성
print(A)

# <연속 원소 배열 생성 함수>
# 연속적인 원소를 가진 배열을 생성할 수 있는 함수
# 'range'와 사용법이 유사함 -> 'arrange'함수는 주어진 범위 내에서 지정한 간격으로 연속적인 원소를 가진 배열을 생성할 때 사용한다.
# 시작 값부터 지정한 간격으로 배열된 원소를 생성, 마지막 값은 범위에서 제외된다.
# np.arange(시작, 마지막, 간격)                //간격을 적지 않는다면 default 값은 1
# np.arange(시작,마지막)
# np.arange(마지막)

A = np.arange(0,50,5)
print(A)
B = np.arange(50)
print(B)


# np.linspace
# 지정한 범위 내에서 원하는 원소 개수로 숫자를 뽑아서 배열을 생성한다.
# 일정한 간격으로 샘플링함 !!
# np.linspace (시작값, 마지막 값, 샘플 개수)
# np.linspace (시작값, 마지막 값) default sampling 개수 = 50

A = np.linspace(0,10,10)        #0~10 샘플개수 10개
print(A)

# <shape 변환 함수>
# 'reshape 메소드' 배열의 데이터를 공유하는 shape가 다른 배열인 뷰를 생성함
# 원본 배열의 데이터를 공유하지 않는 새로운 복사본을 만들고 싶으면 추가로 'copy method'를 사용하면 됨

A = np.arange(0,16)             #1차원 0~15
print(A)
B = A.reshape(4,4)              #A를 4,4인 2차원으로 변환
print(B)
print(B.base)                   #B의 베이스가 무엇인지 확인

print(B.base is A)              #B.base와 A는 서로 동일한 객체임 = 데이터를 공유함 => array A의 데이터가 저장되어 있는 메모리 공간을 공유함
###그래서 어느 하나를 수정하면 둘이 같이 변경됨.
B[0] = -1
print(B)
print(A)
#둘다 반영된 것을 확인

#reshape을 사용해 B의 데이터를 그대로 공유하여 (2,8)로 배열을 생성 후 copy해보기
C = B.reshape(2,8).copy()
print(C)
print(C.shape)
print(C.base)                       #C = B를 copy한것이기 때문에, C.base = B 가 아님.
C[0] = -2                           #그렇기에 이렇게 변경하면 C에만 변경이 된다.
print(B)
print(C)

# <shape의 차원을 자동으로 지정하기> : shape (,) 에서 '-1' 차원을 넣으면 확정된 차원 크기로부터 나머지 차원을 추론해서 배열을 생성함
A = np.arange(0,101,0.5)
print(A)
B = A.reshape(2,-1)                  #열 :10, 행 : -1(추론)
print(B)
C = A.reshape(-1,2)
print(C)


#'revel method' 배열을 1차원 배열로 변환하여 리턴함

# 2차원 배열을 먼저 만듬
A = np.arange(0,10)
A.shape = (5,2)
print(A)

B = A.ravel()
print(B)                    # 5x2 에서 10x1 로 변함
print(B.base)

#'resize method' 뷰를 생성하지 않고 배열의 shape을 직접 바꾼다.
A = np.arange(12)
print(A)
A.resize(3,4)
print(A)


#'newaxis' : 배열의 차원을 증가시킨다. 1차원 배열을 열벡터 또는 행벡터로 바꿀 때 사용가능
A = np.array([1,2,3])
print(A)
print(A.shape)                      #shape = (3,)
B = A[:,np.newaxis]
print(B)
print(B.shape)                      #shape = (3,1)

C = A[np.newaxis,:]
print(C)
print(C.shape)                      #shape = (1,3)

#<배열 결합 함수>
# 배열을 결합하는 데 사용하는 함수
# 뷰를 리턴하는 것이 아니라 새로운 배열을 리턴
# 값을 변경해도 배열 생성 시 사용 했던 배열들이 영향을 주지 않는다.

#'vstack 함수'는 배열을 열 방향으로 결합한다.