"""
    怎样从集合中获取最大或者最小的N个元素列表？
"""
import heapq

if __name__ == "__main__":
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))  # 最大三个数
    print(heapq.nsmallest(3, nums))  # 最小三个数
    print("=" * 50)
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(expensive)
    print("=" * 50)
    heap = nums
    print(heap)
    heapq.heapify(heap)
    print(heap)
    print("=" * 50)
    print(heapq.heappop(heap))
    print("=" * 50)

