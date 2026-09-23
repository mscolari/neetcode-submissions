class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        count = {}
        for student in students:
            if student not in count:
                count[student] = 0
            count[student] += 1
        
        total_count = len(students)
        for s in sandwiches:
            if s not in count or count[s] == 0:
                break

            if count[s] > 0:
                count[s] -= 1
                total_count -= 1
            else:
                break

        return total_count