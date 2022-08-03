class MyCalendar:

    def __init__(self):
        self.list = []

    def book(self, start: int, end: int) -> bool:
        # print(self.list)
        for ele in self.list:
            if ele[0] < start < ele[1]:
                return False
            
            if ele[0] < end < ele[1]:
                return False
            
            if ele[0] >= start and ele[1] <= end:
                return False
            
        self.list.append((start, end))
        return True