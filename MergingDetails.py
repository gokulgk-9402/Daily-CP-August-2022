from typing import List
from collections import defaultdict

class Solution:
    def mergeDetails(self, details : List[List[str]]) -> List[List[str]]:
        # code here
        id_parents = list(range(len(details)))

        def get_parent(x):
            if id_parents[x] != x:
                id_parents[x] = get_parent(id_parents[x])

            return id_parents[x]

        def union(old, new):
            parent_old = get_parent(old)
            parent_new = get_parent(new)
            if parent_old != parent_new:
                id_parents[new] = parent_old

            return parent_old

        email_to_id = {}
        for i, account in enumerate(details):
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = i
                else:
                    i = union(email_to_id[email], i)

        id_to_emails = defaultdict(list)
        for email in email_to_id:
            id_group = get_parent(email_to_id[email])
            id_to_emails[id_group].append(email)

        ans = []
        for id_group in id_to_emails:
            sorted_emails = sorted(id_to_emails[id_group])
            ans.append([details[id_group][0]] + sorted_emails)

        return ans

print(Solution().mergeDetails(
[["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]))