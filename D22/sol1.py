class Solution:
    def dailyTemperatures(self, T: int) -> int:
        answer = [0] * len[T]
        stack = []

        for idx, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last]] = idx - last
            stack.append(idx)

        return answer