"""
chatGPT提供
滑动窗口限流服务
滑动窗口算法是一种常用的限流算法，它主要用于限制系统的请求速率。滑动窗口算法的应用场景如下：
1. API 限流：对于公共 API 接口，通常需要限制请求的速率，以保护 API 接口的性能和安全。
2. 用户请求限流：限制用户在一定时间内请求的数量，以防止恶意请求。
3. 网络流量控制：在网络流量高峰期，通过滑动窗口算法限制网络带宽使用，以保证其他请求的正常运行。
4. 电子商务系统：在电子商务系统中，需要限制用户在一定时间内购买的数量，以防止购买过多。
这些场景只是滑动窗口算法的一部分应用，实际上还有很多其他的应用场景。
"""

import time
from collections import deque

class SlidingWindowRateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.window = deque()

    def allow_request(self):
        now = time.time()
        while len(self.window) > 0 and self.window[0] <= now - self.time_window:
            self.window.popleft()
        if len(self.window) >= self.max_requests:
            return False
        self.window.append(now)
        return True


limiter = SlidingWindowRateLimiter(3, 5)

while True:
    if limiter.allow_request():
        # 处理请求
        print("doing...")
        time.sleep(1)
    else:
        # 拒绝请求
        print("waiting...")
        time.sleep(1)

