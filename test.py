import OpenDartReader
import pandas as pd

# OpenDartReader 객체 생성: 'your_api_key_here'에 자신의 API 키를 입력하세요.
dart = OpenDartReader('63d2d4a745644ba334f7c1c9f0d2bef987571b85')

# 조회할 기업의 종목코드 리스트: 여기에 필요한 종목코드를 추가하세요.
corp_codes = ['005930']  # 예시 코드들(Samsung Electronics, SK Hynix, NAVER)

# 결과를 저장할 빈 데이터프레임 생성
all_financials = pd.DataFrame()

# 각 기업별로 재무제표 데이터 조회 및 데이터프레임에 추가
for code in corp_codes:
    try:
        # finstate_all 메소드를 사용하여 재무제표 데이터 조회
        # corp: 종목코드, bsns_year: 사업년도, reprt_code: 보고서 코드 (11011: 사업보고서)
        # 1분기보고서: 11013
        # 반기보고서: 11012
        # 3분기보고서: 11014
        # 사업보고서: 11011
        # 여기서는 사업년도를 다양하게 설정하여 반복문을 돌려야 합니다.
        for year in range(2015, 2024):  # 예시: 1999년부터 2022년까지 데이터 조회
            financials = dart.finstate_all(corp=code, bsns_year=year, reprt_code='11013')
            if financials is not None:
                all_financials = pd.concat([all_financials, financials], ignore_index=True)
    except Exception as e:
        print(f"Error retrieving data for {code}: {e}")

# 조회된 데이터 확인
print(all_financials.head())

# 필요한 경우, 조회된 데이터를 CSV 파일로 저장
all_financials.to_csv('financial_data.csv', index=False)
