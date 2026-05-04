import random

def generate_prices(count=10, min_price=1.0, max_price=1000.0):
    """生成指定数量的随机商品价格"""
    prices = []
    for i in range(count):
        price = round(random.uniform(min_price, max_price), 2)
        prices.append(price)
    return prices

def main():
    # 1. 生成10个随机商品价格
    prices = generate_prices(10)
    
    print("=" * 40)
    print("随机生成的10个商品价格：")
    print("=" * 40)
    for i, price in enumerate(prices, 1):
        print(f"  商品{i:2d}: ¥{price:>8.2f}")
    
    # 2. 排序（升序）
    sorted_prices = sorted(prices)
    
    print("\n" + "=" * 40)
    print("排序后的商品价格（升序）：")
    print("=" * 40)
    for i, price in enumerate(sorted_prices, 1):
        print(f"  第{i:2d}名: ¥{price:>8.2f}")
    
    # 3. 输出最便宜的3个
    cheapest_3 = sorted_prices[:3]
    
    print("\n" + "=" * 40)
    print("最便宜的3个商品价格：")
    print("=" * 40)
    for i, price in enumerate(cheapest_3, 1):
        print(f"  第{i}便宜: ¥{price:>8.2f}")
    
    print("\n" + "=" * 40)
    print(f"最低价: ¥{cheapest_3[0]:.2f}")
    print(f"最高价: ¥{sorted_prices[-1]:.2f}")
    print(f"平均价: ¥{sum(prices)/len(prices):.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
