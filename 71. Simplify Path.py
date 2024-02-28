class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 1:
            return path
        left = 0
        path_stack = []

        while left < len(path) - 1:

            if path[left] == '/' and left == len(path) - 1:
                left += 1

            if path[left] == '/':
                right = left + 1
                while right in range(len(path)) and path[right] != '/':
                    right += 1

                element = path[left:right]
                if element == '/' or element == '/.':
                    pass
                elif element == '/..':
                    if len(path_stack) > 0:
                        path_stack.pop()
                else:
                    path_stack.append(element)
                left = right
            else:
                left += 1
        return ''.join(path_stack) if path_stack else '/'


solution = Solution()
assert solution.simplifyPath("/home/") == "/home"
assert solution.simplifyPath("/../") == '/'
assert solution.simplifyPath("/home//foo/") == "/home/foo"
