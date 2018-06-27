#pandas와 numpy 모듈을 사용하기 위해 import
import pandas as pd
import numpy as np

#read_osc 매소드를 사용해서 cctvseoul.csv 파일을 읽어 CCTV_Seoul에 저장
CCTV_Seoul = pd.read_csv('d:\\cctvstat\\cctvseoul.csv',encoding='utf-8')

#CCTV_Seoul 에서 첫 5개 데이터를 출력(테스트용)
print(CCTV_Seoul.head())

#CCTV_Seoul의 헤더를 출력하라.
print(CCTV_Seoul.columns)
print(CCTV_Seoul.columns[1],CCTV_Seoul.columns[2],CCTV_Seoul.columns[3])

#rename 매소드를 사용하면 헤더값을 변경할수 있다.
#inplace 를 참으로 하면, 실제 변수 값이 변경
#inplace 를거짓으로 하면, 실제 변수 값은 변경되지 않고, 출력만 변경.
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
print(CCTV_Seoul.head(2))

#read_excel 함수를 사용해서 excel 파일을 읽어온다.
# xlrd 모듈 관련 에러가 난다면 pip install xlrd 해서 모듈 설치
pop_Seoul = pd.read_excel('d:\\cctvstat\\popseoul.xls',encoding='utf-8')
print(pop_Seoul.head(3))

#header =2 ) 헤더의 위치를 세번째 줄로 지정
#
pop_Seoul = pd.read_excel('d:\\cctvstat\\popseoul.xls',
                                              header =2,
                                              usecols='B,D,G,J,N',
                                              encoding='utf-8')
print(pop_Seoul.head())

pop_Seoul.rename(columns={pop_Seoul.columns[0]:'구별',
                                                  pop_Seoul.columns[1]:'인구수',
                                                  pop_Seoul.columns[2]:'한국인',
                                                  pop_Seoul.columns[3]:'외국인',
                                                  pop_Seoul.columns[4]:'고령자'},
                                    inplace=True)
print(pop_Seoul.head())

#CCTV의 소계를 가지고 오름차순으로 정렬
print(CCTV_Seoul.sort_values(by='소계', ascending=True).head(5))
#CCTV의 소계를 가지고 내림차순으로 정렬
print(CCTV_Seoul.sort_values(by='소계', ascending=False).head(5))

#CCTV의 증가율을 계산하고 CCTV_Seoul에 증가율을 추가
CCTV_Seoul['최근증가율']=(CCTV_Seoul['2016년']+CCTV_Seoul['2015년']+\
                                     CCTV_Seoul['2014년']/CCTV_Seoul['2013년도 이전'] * 100)
print(CCTV_Seoul.sort_values(by='최근증가율',ascending=False).head(5))

#서울시 인구 현황
print(pop_Seoul.head())

#서울시 전체 인구 합계 통계가 나타나지 않도록 삭제.
#불필요한 데이터는 drop 메소드로 삭제
pop_Seoul.drop([0], inplace=True)
print(pop_Seoul.head())

#반복되서 나타나는 데이터는 unique를 사용해 하나로 합할수 있다.
#구별 항목이 같은 것끼리는 합해서 하나로 만든다.
print(pop_Seoul['구별'].unique())

#NaN 값의 위치를 찾아 삭제한다
print(pop_Seoul[pop_Seoul['구별'].isnull()])
pop_Seoul.drop([26], inplace=True)

pop_Seoul['외국인비율']=pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul['고령자비율']=pop_Seoul['고령자']/pop_Seoul['인구수']*100
print(pop_Seoul.head())



