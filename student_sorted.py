def selection_sort(student_grad):
    length = len(student_grad)
    if length != 1:
        for i in range(length):
            min = i
            for j in range(i+1 , length): # becuase the last element is sorted 
                if student_grad[j] < student_grad[min]:
                    min = j
            temp = student_grad[i]
            student_grad[i] = student_grad[min]
            student_grad[min] = temp
        print(f'the sorted grades: {student_grad}')
        return
    else:
        print(f'it has an one element: {student_grad}')
        return # use should use return to can use this fun again if not the program will stay in the end of the fun return mean end fun

def insertion_sort(student_grad):
    if len(student_grad)  > 1 :
        for i in range(1,len(student_grad)):
            key = student_grad[i]
            hole = i
            while(hole > 0 and student_grad[hole-1] >key ):
                temp = student_grad[hole-1]
                student_grad[hole-1] = student_grad[hole]
                student_grad[hole] = temp
                hole-=1
        print(f'the sorted grades: {student_grad}')
        return
    else:
        print(f'it has an one element: {student_grad}')
        return


def merge_sort(student_grad):
    if len(student_grad) <= 1:
            return student_grad

    mid = len(student_grad) // 2
    left = merge_sort(student_grad[:mid])
    right = merge_sort(student_grad[mid:])
    return merge(right, left )


def merge(right, left):
    extra_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            extra_list.append(left[i])
            i += 1
        else:
            extra_list.append(right[j])
            j += 1

    extra_list.extend(left[i:])
    extra_list.extend(right[j:])
    return extra_list





# list_of_name = []
# list_of_grade = []
# list_of_perf = []



# issubmited = False

# while True :
#     while not issubmited:
#         # student_name = input("enter your name of student: ").strip()
#         # print('\n')
#         # list_of_name.append(student_name)

#         student_grade = float(input("enter your grad of students: ").strip())
#         print('\n')
#         list_of_grade.append(student_grade)

#         # student_perf = input("enter your perf of students: ").strip()
#         # print('\n')
#         # print(f'your informations :{student_name} , {student_grade} , {student_perf} \n')
#         # list_of_name.append(student_perf)

#         # isright = input('if your information are true enter 1 else 0: ').strip()
#         # print('\n')

#         # if isright == "1":
#         #     pass
#         # else:
#         #     if list_of_name :
#         #         list_of_name.pop()
#         #     if list_of_grade :
#         #         list_of_grade.pop()
#         #     if list_of_perf :
#         #         list_of_perf.pop()
        
#         anthor_data = input('if there anthor student enter 1 else 0: ').strip()
#         print('\n')
#         if anthor_data == "1":
#             continue
#         else:
#             break
    
#     # Now we will ask the person if he want to sorted grades or exit
#     program_state = input("if you want to sort the grade and see it enter 1 or 2 for using insertion sort or 3 for using merg sort else enter 0: ").strip()
#     if program_state == "1" :
#         print('\n')
#         print(f"the unsorted grades: {list_of_grade}\n")
#         selection_sort(list_of_grade)
#         go_ahead =  input('if there anthor data enter 1 else 0: ').strip()
#         print('\n')
#         if go_ahead == "1":
#             continue
#         else:
#             break
#     elif program_state == "2" :
#         print('\n')
#         print(f"the unsorted grades: {list_of_grade}\n")
#         insertion_sort(list_of_grade)
#         go_ahead =  input('if there anthor data enter 1 else 0: ').strip()
#         print('\n')
#         if go_ahead == "1":
#             continue
#         else:
#             break
#     elif program_state == "3" :
#         print('\n')
#         print(f"the unsorted grades: {list_of_grade}\n")
#         merg_sort(list_of_grade , 0 , len(list_of_grade))
#         go_ahead =  input('if there anthor data enter 1 else 0: ').strip()
#         print('\n')
#         if go_ahead == "1":
#             continue
#         else:
#             break