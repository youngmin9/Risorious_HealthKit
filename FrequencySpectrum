import Accelerate

func fft(of data: [Double]) -> [Double] {
    // FFT를 수행하기 위해 Vectors 타입을 사용합니다.
    var dataVector = vdSP_VectorRange(data, uint(0), uint(data.count))
    
    // FFT를 수행할 복소수 벡터를 생성합니다.
    var fftVector = vdSP_CreateR(dataVector.count)
    
    // FFT를 수행합니다.
    vdSP_zfft(.init(dataVector), .init(fftVector), uint(VDSP_DFT_FORWARD), uint(VDSP_DFT_CPLX_EQUISPACE), uint(VDSP_STRIDE_0), uint(VDSP_BLOCKSIZE_0))
    
    // 주파수 스펙트럼을 계산합니다.
    let frequencyVector = vdSP_CreateR(dataVector.count)
    vdSP_zcsf(.init(fftVector), .init(frequencyVector), uint(VDSP_DFT_INVERSE), uint(VDSP_DFT_CPLX_EQUISPACE), uint(VDSP_STRIDE_0), uint(VDSP_BLOCKSIZE_0))
    
    // 주파수 스펙트럼을 반환합니다.
    return frequencyVector.pointee
}

// HRV 데이터에 대한 예시 데이터(우선)
let hrvData: [Double] = [10.0, 12.0, 11.0, 9.5, 10.5, 12.0, 10.0, 11.0, 9.5, 10.5, 12.0, 10.0]

// FFT를 수행하고 주파수 스펙트럼을 얻습니다.
let frequencySpectrum = fft(of: hrvData)

// 주파수 스펙트럼을 출력합니다.
print(frequencySpectrum)
