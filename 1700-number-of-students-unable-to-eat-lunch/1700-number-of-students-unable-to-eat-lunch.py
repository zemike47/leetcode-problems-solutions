from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu = deque(students)
        sandw = deque(sandwiches)

        rotation = 0

        while True:
            if stu[0] == sandw[0]:
                stu.popleft()
                sandw.popleft()
                rotation = 0
            else:
                stu.append(stu.popleft())
                
                rotation += 1
            
            if rotation == len(stu):
                break
        
        return len(stu)




