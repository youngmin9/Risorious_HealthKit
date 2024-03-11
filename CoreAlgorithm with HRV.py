import numpy as np

def calculate_chronic_stress(lf):
    """
    Chronic stress 계산
    :param lf: LF 값
    :return: Chronic stress 수치
    """
    chronic_stress = 124 - 0.18 * np.log(lf)
    return chronic_stress

def calculate_acute_stress(stress_rmssd, baseline_rmssd):
    """
    Acute stress 계산
    :param stress_rmssd: 스트레스 받은 후의 RMSSD 값
    :param baseline_rmssd: 기준이 되는 RMSSD 값
    :return: Acute stress 수치
    """
    acute_stress = (stress_rmssd - baseline_rmssd) * -0.160
    return acute_stress

def calculate_attention_performance(lf_hf_ratio_before, lf_hf_ratio_after):
    """
    집중력 몰입도 계산
    :param lf_hf_ratio_before: task 전 LF/HF 비율
    :param lf_hf_ratio_after: task 후 LF/HF 비율
    :return: Attention performance 변화량
    """
    attention_performance = (lf_hf_ratio_after - lf_hf_ratio_before) * -0.23
    return attention_performance

def calculate_attention_maintenance(sex, age, rmssd):
    """
    집중력 유지 계산
    :param sex: 성별 (남자 = 1, 여자 = 0)
    :param age: 나이
    :param rmssd: RMSSD 값
    :return: 집중력 유지 지수
    """
    attention_maintenance = -3.1 + 0.05 * sex + 0.002 * age + 0.17 * rmssd
    return attention_maintenance

def calculate_vo2_max(age, resting_heart_rate):
    """
    VO2 max 계산
    :param age: 나이
    :param resting_heart_rate: 휴식 시 심박수 (1분 단위)
    :return: VO2 max
    """
    vo2_max = 15.3 * (208 - age * 0.7) / resting_heart_rate
    return vo2_max

def calculate_sleep_quality(tp, hr):
    """
    수면 quality 점수 계산
    :param tp: Total Power of HRV
    :param hr: Heart Rate
    :return: 수면 quality 점수
    """
    sleep_quality = 11.416 - 0.001 * tp - 0.069 * hr
    return sleep_quality

# 예시 사용
lf = 1000  # 예시 LF 값
stress_rmssd = 50  # 예시 스트레스 받은 후의 RMSSD
baseline_rmssd = 30  # 예시 기준 RMSSD
lf_hf_ratio_before = 2.0  # task 전 LF/HF 비율
lf_hf_ratio_after = 2.5  # task 후 LF/HF 비율
sex = 1  # 남자
age = 25  # 나이
resting_heart_rate = 60  # 휴식 시 심박수
tp = 2000  # Total Power of HRV
hr = 70  # Heart Rate

print("Chronic Stress:", calculate_chronic_stress(lf))
print("Acute Stress:", calculate_acute_stress(stress_rmssd, baseline_rmssd))
print("Attention Performance:", calculate_attention_performance(lf_hf_ratio_before, lf_hf_ratio_after))
print("Attention Maintenance:", calculate_attention_maintenance(sex, age, baseline_rmssd))
print("VO2 Max:", calculate_vo2_max(age, resting_heart_rate))
print("Sleep Quality:", calculate_sleep_quality(tp, hr))
