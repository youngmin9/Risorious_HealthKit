#numpy scipy matplotlib

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def calculate_lf_hf(rr_intervals):
    # RR 간격을 신호 샘플로 변환 (단위: 초)
    rr_intervals = np.array(rr_intervals) / 1000.0  # ms to seconds
    rr_times = np.cumsum(rr_intervals)  # RR 간격으로부터 시간 벡터 생성
    rr_signal = 1.0 / rr_intervals  # 심박수 신호 생성

    # 신호의 평균 주파수 성분을 제거 (DC 제거)
    rr_signal_detrended = signal.detrend(rr_signal)

    # Lomb-Scargle 주기도 계산
    frequency, power = signal.lombscargle(rr_times, rr_signal_detrended, np.arange(0.01, 0.5, 0.001), normalize=True)

    # LF 및 HF 파워 계산
    lf_mask = (frequency >= 0.04) & (frequency <= 0.15)
    hf_mask = (frequency >= 0.15) & (frequency <= 0.4)
    
    lf_power = np.trapz(power[lf_mask], frequency[lf_mask])
    hf_power = np.trapz(power[hf_mask], frequency[hf_mask])

    # LF/HF 비율 계산
    lf_hf_ratio = lf_power / hf_power
    
    return lf_hf_ratio, frequency, power

# 예시 RR 간격 데이터 (ms)
rr_intervals = [800, 810, 780, 790, 820, 800, 830, 810]

lf_hf_ratio, frequency, power = calculate_lf_hf(rr_intervals)

print(f"LF/HF Ratio: {lf_hf_ratio}")

# 주파수 대 파워 스펙트럼 그래프
plt.figure(figsize=(10, 6))
plt.plot(frequency, power, label='Power Spectrum')
plt.axvline(0.04, color='r', linestyle='--', label='LF start')
plt.axvline(0.15, color='g', linestyle='--', label='HF start')
plt.axvline(0.4, color='b', linestyle='--', label='HF end')
plt.legend()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Power Spectrum of RR intervals')
plt.show()


#LF/HF ratio를 계산하기 위해 HRV (Heart Rate Variability) raw data에서 신호 처리를 수행하는 Python 코드를 구현하려면, 주로 Fast Fourier Transform (FFT) 또는 Lomb-Scargle 주기도를 사용하여 시간 영역 데이터를 주파수 영역으로 변환해야 합니다. 이 예제에서는 numpy와 scipy 라이브러리를 사용하여 FFT를 적용하고 LF (0.04-0.15 Hz) 및 HF (0.15-0.4 Hz) 범위의 파워를 계산한 다음 LF/HF 비율을 구하는 방법을 보여줍니다.
