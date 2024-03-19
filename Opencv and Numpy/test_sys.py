import sys

print("The name of the script being processed is : '{}' ".format(sys.argv[0]))
print("The number of arguments of the script is : '{}'".format(len(sys.argv)))
print("The arguments of the script are : '{}'".format(str(sys.argv)))

'''
if len(sys.argv) != 3:
    print("인자는 2개의 숫자입니다.")
    print("Usage:python test_sys.py number1 number2")
    print("python test_sys.py")

    sys.exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
sum = num1 + num2
print("%d 더하기 %d는 %d 입니다."%(num1, num2, sum))
'''

#코드를 만들고, 커맨더창에서 python test_sys.py 라는 명령어로 이 파일을 실행할 때, 인자값들을 전달받을 수 있다.
#sys.argv[0] = 파일명
#sys.argv[1] = 1번째 인자
#sys.argv[2] = 2번째 인자
#     .
#     .
#     .