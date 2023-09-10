class Solution:
    def isValid(self, s: str) -> bool:
        heap = []
        for i in range(len(s)):
            if s[i] == "{":
                heap.append("{")
                continue
            if s[i] == "[":
                heap.append("[")
                continue
            if s[i] == "(":
                heap.append("(")
                continue

            if s[i] == "}":
                if len(heap) <= 0:
                    return False
                if heap[-1] == "{":
                    heap.pop(-1)
                else:
                    heap.append("}")
                continue
            if s[i] == "]":
                if len(heap) <= 0:
                    return False
                if heap[-1] == "[":
                    heap.pop(-1)
                else:
                    heap.append("]")
                continue
            if s[i] == ")":
                if len(heap) <= 0:
                    return False
                if heap[-1] == "(":
                    heap.pop(-1)
                else:
                    heap.append(")")
                continue

        return False if len(heap) > 0 else True


sol = Solution()
# tests = ["()", "()[]{}", "(]", "]", "(])"]
tests = ["()[]{}"]
for test in tests:
    print(sol.isValid(test))
