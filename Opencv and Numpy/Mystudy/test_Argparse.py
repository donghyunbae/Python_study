import argparse

#객체 하나 생성
parser = argparse.ArgumentParser(description="인자는 2개의 숫자입니다")

#define arguments
parser.add_argument('integers', metavar='N', type=int, nargs = 2, help='숫자로입력하세요')
args = parser.parse_args()

#return result
print("%d 더하기 %d 는 %d 입니다."%(args.integers[0], args.integers[1], args.integers[0] + args.integers[1]))
