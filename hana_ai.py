import math

MARGIN = 0.40
MIN_PROFIT = 5000

def calculate_price(cost, shipping=0, fee_rate=0.10, extra=0):
    if cost < 0 or shipping < 0 or extra < 0:
        raise ValueError("비용은 0 이상이어야 합니다")
    if not 0 <= fee_rate < 0.60:
        raise ValueError("수수료율을 확인하세요")
    total = cost + shipping + extra
    minimum = max(
        total + MIN_PROFIT,
        total / (1 - fee_rate - MARGIN)
    )
    price = math.ceil((minimum - 900) / 1000) * 1000 + 900
    profit = price * (1 - fee_rate) - total
    return {
        "price": price,
        "profit": round(profit),
        "margin": round(profit / price * 100, 1)
    }

if __name__ == "__main__":
    result = calculate_price(10000, 3000, 0.10)
    print(result)
