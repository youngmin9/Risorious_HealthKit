import pandas as pd
import numpy as np
import statsmodels.api as sm

# 시계열 데이터 로드
# 예: treatment 전/후의 시계열 데이터
data = pd.read_csv('your_data.csv')

# 시계열 데이터의 시간 변수와 종속 변수 설정
time_series = sm.add_constant(data['time'])  # 시간 변수 추가
y = data['outcome_variable']  # 종속 변수 설정

# 개입 시점 설정
intervention_point = '2024-01-01'  # 예: 개입이 발생하는 시점

# 개입 시점 이전과 이후의 데이터 분할
data_before = time_series[data['time'] < intervention_point]
data_after = time_series[data['time'] >= intervention_point]
y_before = y[data['time'] < intervention_point]
y_after = y[data['time'] >= intervention_point]

# ITS 모델 구축
X_before = sm.add_constant(data_before)
X_after = sm.add_constant(data_after)
its_model = sm.OLS(y, time_series).fit()

# 모델 결과 출력
print(its_model.summary())
