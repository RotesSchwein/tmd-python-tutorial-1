# -*- coding: utf-8 -*-
"""230816_실습4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LN1lnMnwLDzc_dX3WQWgkCah2SjXVCVH

##정수 리스트를 입력받아 그 중 가장 큰 수와 가장 작은 수를 반환하는 함수를 완성해보자
"""

# 'find_max_min' 함수를 정의합니다.
#이 함수는 정수 리스트를 입력받아 가장 큰 수와 가장 작은 수를 반환합니다.

def find_max_min(numbers_list):
  # 이 곳에 코드를 작성해주세요
  max_value = max(numbers_list)
  min_value = min(numbers_list)
  return max_value, min_value
  # 이 곳에 코드를 작성해주세요

# 예제로 사용할 정수 리스트
numbers = [34, 12, 56, 78, 23]
# 'find_max_min' 함수를 호출하고 결과를 출력합니다.
print(find_max_min(numbers)) # 출력: (78, 12)

