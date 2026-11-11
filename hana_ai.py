import math
import os
import urllib.parse
import urllib.request
import json

MARGIN = 0.40
MIN_PROFIT = 5000


def calculate_price(cost, shipping=0, fee_rate=0.10, extra=0):
    if cost < 0 or shipping < 0 or extra < 0:
        raise ValueError('비용은 0 이상이어야 합니다')
    if not 0 <= fee_rate < 0.60:
        raise ValueError('수수료율을 확인하세요')
    total = cost + shipping + extra
    minimum = max(total + MIN_PROFIT, total / (1 - fee_rate - MARGIN))
    price = math.ceil((minimum - 900) / 1000) * 1000 + 900
    profit = price * (1 - fee_rate) - total
    return {'price': price, 'profit': round(profit), 'margin': round(profit / price * 100, 1)}


def check_api_key():
    key = os.environ.get('DOMEGGOOK_API_KEY', '')
    if not key:
        raise RuntimeError('DOMEGGOOK_API_KEY가 설정되지 않았습니다')
    print('도매꾹 API 키 환경변수 확인 완료')
    return key


if __name__ == '__main__':
    check_api_key()
    print('가격 계산:', calculate_price(10000, 3000, 0.10))
    print('도매꾹 실제 상품 조회는 아직 연결되지 않았습니다')
