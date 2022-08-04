class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        stk = []
        for ele in lst:
            if ele == "" or ele == ".":
                continue
            if ele == "..":
                if len(stk):
                    stk.pop(-1)
            else:
                stk.append(ele)
        return("/" + "/".join(stk))