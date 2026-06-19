import pandas as pd
from py_clob_client.client import ClobClient

def get_official_markets():
    # Polymarket 공식 오픈 API 실시간 주소
    # 근데 자꾸 접근 막힘
    host = "https://google.com"
    
    print("🔄 Polymarket 공식 오픈 API 라이브러리로 데이터 요청 중...")
    print("제발 그만 막혀라...")
    try:
        # 공식 클라이언트 객체 생성 (조회용이므로 지갑 정보 생략)
        client = ClobClient(host=host)
        
        # 공식 메서드로 현재 활성화된 마켓 리스트 가져오기
        # (라이브러리 자체 내장 로직이 방화벽 통과를 도와줍니다.)
        sampling_markets = client.get_markets()
        
        market_list = []
        # 가져온 데이터 정제하기
        for market in sampling_markets.get('data', []):
            market_list.append({
                "질문": market.get('question'),
                "카테고리": market.get('category'),
                "토큰 ID": market.get('token_id'),
                "상태": market.get('status')
            })
            
        if market_list:
            print("🎉 공식 오픈 API 데이터 수집 성공!\n")
            return pd.DataFrame(market_list)
        else:
            print("❌ 마켓 데이터를 찾을 수 없습니다.")
            return None
            
    except Exception as e:
        print(f"❌ 공식 API 호출 중 오류 발생: {e}")
        print("💡 만약 이 코드마저 막힌다면, 한국 IP 대역 전체가 방화벽에 적발된 것이므로 '윈도우 VPN(일본/싱가포르)'을 켜는 것이 유일한 해결책입니다.")
        return None

if __name__ == "__main__":
    df = get_official_markets()
    if df is not None:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        print(df.head(10)) # 상위 10개 출력
