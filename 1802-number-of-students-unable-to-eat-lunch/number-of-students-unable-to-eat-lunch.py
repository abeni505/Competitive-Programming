class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        student_count = [0, 0]  
        for student in students:
            student_count[student] += 1

        students = deque(students)
        sandwiches = deque(sandwiches)
        while sandwiches:
            if student_count[sandwiches[0]] == 0:
                break 
            if students[0] == sandwiches[0]:
                student_count[sandwiches.popleft()] -= 1
                students.popleft()
            else:
                students.append(students.popleft())
        
        return len(students)
