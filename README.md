# Risorious_HealthKit


0) 제목: watchOS HRV 데이터(from HealthKit) 기반 스트레스 level 제공 앱

→Minimum Viable Feature(최소 기능): 1) 워치로 측정된 HRV 표시 + 2) 스트레스와의 상관관계 표시 +a

1) 개요:
이 어플리케이션은 심장박동변이도(HRV, Heart Rate Variability)를 측정하여 사용자의 스트레스 수준을 파악하고, 이를 바탕으로 사용자의 **특정** 루틴별 스트레스 수치를 제공하는 것을 목표로 합니다.

*여기서 심장박동(HR)과 심장박동변이도(HRV)의 구분은 다음과 같습니다. 

-----
HR(Heart Rate, 심박수)와 HRV(Heart Rate Variability, 심박변이도)는 심장 건강과 전반적인 웰빙을 평가하는 데 사용되는 두 가지 중요한 지표입니다. 각각의 단위는 다음과 같습니다:

HR (심박수): 심박수는 보통 분당 심장 박동 횟수로 측정되며, 단위는 **bpm (beats per minute, 분당 박동 수)**를 사용합니다. 예를 들어, 평균적인 성인의 심박수는 분당 60~100박 사이일 수 있습니다.

//HRV (심박변이도): 심박변이도는 연속된 심장 박동 간의 시간 간격의 변동을 측정하는 것으로, 심장의 반응성과 자율신경계의 균형 상태를 평가하는 데 사용됩니다. HRV는 보통 밀리초(ms) 단위로 표시되며, 측정 방법에 따라 여러 가지 파라미터(예: RMSSD, SDNN, LF/HF 비율 등)로 나타낼 수 있습니다. //예를 들어, RMSSD(Root Mean Square of Successive Differences)는 연속적인 심박 간의 시간 차이의 제곱근 평균을 밀리초 단위로 표시합니다.

----


2) 주요 기능:

HRV 측정: 사용자의 심박동 변화를 실시간으로 측정하고 이를 바탕으로 HRV를 계산합니다.
루틴별 스트레스 수치 제공: 측정된 HRV를 바탕으로 사용자의 스트레스 수치를 계산하여 루틴별로 제공합니다. But How?
~~스트레스 관리 권장: 사용자의 스트레스 수치와 루틴을 분석하여 스트레스 관리를 위한 개인화된 조언을 제공합니다.~~

3) 사용자 경험(UX):

사용자는 앱을 실행하고, HRV 측정을 위한 장치(스마트워치, 피트니스 트래커 등)와 연동합니다.
사용자는 자신의 일상 루틴을 입력하고, 해당 루틴 동안의 HRV 측정을 시작합니다. 
루틴이 종료되면, 앱은 측정된 HRV를 바탕으로 스트레스 수치를 계산하고 사용자에게 제공합니다.이어서 앱은 사용자의 스트레스 수치와 루틴을 분석하여 스트레스 관리를 위한 개인화된 조언을 제공합니다.

4) 기술 스택:

프론트엔드: React Native를 사용하여 iOS와 Android 모두 호환되는 앱..이 된다면 너무 좋겠죠? 
우선 Xcode로 prototyping 해볼 예정입니다. 
백엔드: Python을 사용하여 HRV 계산 알고리즘을 구현하고, Node.js와 Express.js를 사용하여 서버를 구축합니다.
데이터베이스: 사용자의 HRV 데이터와 루틴 정보를 저장하기 위해 MongoDB를 사용합니다.

5) 향후 계획:

-워치로 얻을 수 있는 건강정보, (정확히는 iOS 내의 건강-HealthKit 관련 데이터 추출 리스트) 

  확보 : 24.03~

-Minimum Viable Feature 확보: 24.02~

-Minimum Viable Feature 개선 cycle: ~ 24.06

in ProductHunt? : ~24.06(asap)

in AppStore? : 24.07


6) 생체 지표 정량화 알고리즘 추가

스트레스 정량화_

만성 스트레스: HRV 데이터를 24시간 연속 측정하여, 124 - 0.18 * ln(LF) 공식을 사용해 만점 124점 기준으로 스트레스 변화를 제시합니다.
급성 스트레스: 일 시작 10분 전과 후의 HRV 데이터를 비교하여, (Stress RMSSD - Baseline RMSSD) * -0.160 공식을 통해 스트레스 수치를 계산합니다.


집중력 정량화_

집중력 몰입도: 작업 중 HRV를 측정하고, LF/HF ratio 변화량 * -0.23 공식을 통해 집중력 변화량을 계산합니다.
집중력 유지: Coefficient Variation = -3.1 + 0.05 sex + 0.002 age + 0.17 RMSSD 공식을 사용해 집중력 유지 능력을 측정합니다.


체력 정량화_
VO2 max: VO2 max = 15.3 * (208 - 나이 * 0.7) / 심박수 공식을 사용하여 심폐지구력을 평가하고, 분류합니다.


수면 정량화_
불면증: 수면 quality 점수 = 11.416 - 0.001*TP - 0.069*HR 공식을 사용해 수면 품질을 평가합니다.
수면 패턴 개선 및 코골이: 수면 패턴의 개선을 위한 추가 연구 및 데이터 분석 계획입니다.


---

## 스트레스 수준 정량화

스트레스 수준을 정량화하기 위한 전문적인 방법 중 하나는 Heart Rate Variability (HRV) 데이터를 분석하여 시간 도메인과 주파수 도메인의 파라미터를 사용하는 것. 

HRV는 심박동 간의 간격 변동성을 측정하는 것으로, 이는 자율 신경계와 심혈관 시스템의 조절에 영향을 미치는 요소들의 반응을 반영함. 

스트레스 수준을 평가하기 위한 전형적인 HRV parameter는 아래와 같음.

1. **SDNN (Standard Deviation of NN intervals)**: 심박동 간의 연속적인 간격의 표준 편차로, 전체 심박동 간의 변동성을 나타냅니다. 높은 SDNN 값은 건강한 자율 신경계와 더 낮은 스트레스 수준

2. **RMSSD (Root Mean Square of Successive Differences)**: 연속적인 심박동 간의 차이의 제곱의 평균의 제곱근으로, 심박동 간의 고주파 변동성을 나타냅니다. 높은 RMSSD 값은 좋은 자율 신경계 활동과 더 낮은 스트레스 수준. 이 지표는 주로 심장의 빠른 변화를 반영하며, 특히 자율신경계 중 부교감신경계의 활성을 나타냅니다

3. **LF/HF 비율 (Low Frequency/High Frequency Ratio)**: 주파수 도메인에서의 HRV 파라미터로, 저주파와 고주파 영역 사이의 비율을 나타냅니다. 높은 LF/HF 비율은 스트레스 또는 심혈관 질환과 관련될 수 있습니다. LF (Low Frequency) 및 HF (High Frequency) 비율은 주파수 영역 분석에서 계산됩니다. LF는 0.04에서 0.15Hz 사이, HF는 0.15에서 0.4Hz 사이의 주파수를 포함합니다. LF는 자율신경계의 교감 및 부교감 신경 활동을 모두 반영하며, HF는 주로 부교감신경 활동을 반영합니다. LF/HF 비율은 교감/부교감신경계의 균형을 나타내는 지표로 사용됩니다.


 

이러한 지표들을 계산하기 위해서는 RR 간격 데이터가 필요하며, 주파수 영역 분석을 위해서는 Fourier 변환 또는 Lomb-Scargle 주기도와 같은 방법을 사용할 수 있습니다. 데이터 분석과 시각화를 위해서는 Python과 같은 프로그래밍 언어를 사용하여 구현할 수 있습니다.

## 추가정보

HRV 측정: 앱은 사용자가 연결한 HRV 측정 장치(스마트워치, 피트니스 트래커 등)로부터 심박동 데이터를 수집합니다. 이 데이터는 사용자의 심장박동 간격을 나타내며, 이 변동성이 HRV를 결정합니다.

HRV 분석: 수집된 심박동 데이터를 분석하여 HRV를 계산합니다. 일반적으로 HRV가 높을수록 심장의 반응성이 좋고 스트레스 수준이 낮음을 의미합니다. 반대로 HRV가 낮을수록 스트레스 수준이 높다고 판단할 수 있습니다.

루틴별 스트레스 수치 계산: 사용자가 설정한 루틴 동안의 HRV를 바탕으로 스트레스 수치를 계산합니다. 예를 들어, '회의' 루틴 동안의 HRV가 낮다면, 이 시간 동안 스트레스 수준이 높았음을 나타낼 수 있습니다.

개인화된 스트레스 수치 제공: 계산된 스트레스 수치는 사용자에게 제공됩니다. 이를 통해 사용자는 어떤 루틴이 스트레스를 유발하는지, 반대로 어떤 루틴이 스트레스를 완화하는지를 알 수 있습니다.


기술 스택 참고

<img width="700" alt="Screenshot 2024-02-27 at 10 41 53 PM" src="https://github.com/youngmin9/Risorious_HealthKit/assets/93260170/f7fd3b29-2765-477f-9ea1-b0bdf7e2fcbb">

<img width="668" alt="Screenshot 2024-02-27 at 10 42 14 PM" src="https://github.com/youngmin9/Risorious_HealthKit/assets/93260170/667ef7b5-8963-4d0b-a06b-52c40062294f">

