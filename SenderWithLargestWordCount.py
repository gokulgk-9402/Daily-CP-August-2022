from typing import List

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = {}
        max_count = 0
        max_sender = ""

        for i in range(len(messages)):
            if senders[i] in counter:
                counter[senders[i]] += len(messages[i].split())

            else:
                counter[senders[i]] = len(messages[i].split())

            if counter[senders[i]] > max_count:
                max_count = counter[senders[i]]
                max_sender = senders[i]

            elif counter[senders[i]] == max_count:
                max_sender = max(senders[i], max_sender)

        return max_sender

print(Solution().largestWordCount(messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]))