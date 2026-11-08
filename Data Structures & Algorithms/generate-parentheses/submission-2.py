class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(path))
                return

            # Add '(' if we have some left
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()

            # Add ')' only if it stays valid
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return result