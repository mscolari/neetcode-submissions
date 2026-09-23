class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        counter = len(sandwiches)
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = len(sandwiches)

            elif counter > 0:
                student = students.pop(0)
                students.append(student)
                counter -= 1
            
            else:
                break

        return len(students)