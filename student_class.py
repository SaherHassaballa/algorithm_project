class Student:
    def __init__(self, name, grade, performance):
        self.name = name
        self.grade = grade
        self.performance = performance

    def get_features(self):
        return [self.name, self.grade, self.performance]

    @staticmethod
    def merge(left, right):
        extra_list = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].grade < right[j].grade:
                extra_list.append(left[i])
                i += 1
            else:
                extra_list.append(right[j])
                j += 1
        extra_list.extend(left[i:])
        extra_list.extend(right[j:])
        return extra_list

    @staticmethod
    def merge_sort(student_list):
        if len(student_list) <= 1:
            return student_list

        mid = len(student_list) // 2
        left = Student.merge_sort(student_list[:mid])
        right = Student.merge_sort(student_list[mid:])
        return Student.merge(left, right)
