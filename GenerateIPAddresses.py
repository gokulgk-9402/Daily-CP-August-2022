#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def genIp(self, s):
        #Code here
        def is_valid(ip):
            ip = ip.split('.')

            if len(ip) != 4:
                return False

            for part in ip:
                
                if part == "":
                    return False

                if int(part) > 255:
                    return False

                if part != "0":
                    if part[0] == "0":
                        return False

            return True

        length = len(s)
        if length > 12:
            return []

        ans = []

        for i in range(1, length - 2):
            for j in range(i+1, length - 1):
                for k in range(j + 1, length):
                    s = s[:k] + "." + s[k:]
                    s = s[:j] + "." + s[j:]
                    s = s[:i] + "." + s[i:]

                    # sprint(s)

                    if is_valid(s):
                        ans.append(s)

                    s = "".join(s.split('.'))

        return ans

res = Solution().genIp("6207291")
res.sort()
if len(res):
    for u in res:
        print(u)

else:
    print(-1)