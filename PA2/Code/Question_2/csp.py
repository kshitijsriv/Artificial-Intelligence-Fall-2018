import numpy as np


lecture_slots = 150
count_prof = 20
count_courses = 40
count_lecture_halls = 4
days = 5
slots = 8

####################################################################
prof = np.zeros(count_prof, dtype=int)
for i in range(count_prof):
    prof[i] = i+1
course = np.zeros(count_courses, dtype=int)
for i in range(count_courses):
    course[i] = i+1
lecture_halls = np.zeros(count_lecture_halls, dtype=int)
for i in range(count_lecture_halls):
    lecture_halls[i] = i+1
pc = []
for i in range(count_courses):
    pc.append([prof[(i%count_prof)], course[i]])
n_slots = 10


def check_constraints(a, pos):
    test1 = list([])
    test1.append([a[pos][0][0], a[pos][1], a[pos][2]])
    test2 = list([])
    test2.append([a[pos][1], a[pos][2], a[pos][3]])

    for i in range(pos-1, -1, -1):
        sche_slot_test1 = list([])
        sche_slot_test2 = list([])
        sche_slot_test1.append([a[i][0][0], a[i][1], a[i][2]])
        sche_slot_test2.append([a[i][1], a[i][2], a[i][3]])

        if test1 == sche_slot_test1 or test2 == sche_slot_test2:
            return False
    return True


number_of_backtracks_list = []
number_of_iterations_list = []
number_of_conflicts_list = []


def csp():
    k = 0
    flag = 1
    backstack = []
    schedule = []
    number_of_backtracks = 0
    number_of_iterations = 0
    number_of_conflicts = 0
    while k < lecture_slots:
        number_of_iterations += 1
        if flag == 1:
            slot_entry = list([])
            for l in range(n_slots):
                slot_entry.append([pc[np.random.randint(1, count_courses)], np.random.randint(1, 6), np.random.randint(1, 9), np.random.randint(1, count_lecture_halls+1), k])

            for j in range(n_slots):
                backstack.append(slot_entry[j])
        if backstack:
            slot_from_backstack = backstack.pop()

        if slot_from_backstack[4] == k:
            schedule.append(slot_from_backstack)

            if check_constraints(schedule, k):
                k += 1
                flag = 1
            else:
                number_of_conflicts += 1
                schedule.pop()
                flag = 0

        else:
            number_of_backtracks += 1
            k -= 1
            schedule[k] = slot_from_backstack

            if check_constraints(schedule, k):
                k += 1
                flag = 1
            else:
                schedule.pop()
                flag = 0

    schedule = np.array(schedule)
    print("FINAL SCHEDULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n", schedule)
    # print("number_of_backtracks = ", number_of_backtracks)
    # print("number_of_iterations = ", number_of_iterations)
    # print("number_of_conflicts = ", number_of_conflicts)
    # number_of_backtracks_list.append(number_of_backtracks)
    # number_of_iterations_list.append(number_of_iterations)
    # number_of_conflicts_list.append(number_of_conflicts)


if __name__ == '__main__':
    # for i in range(100):
        # print("# =============== ", i)
        csp()
        # print("=============================================================================\n\n")

    # print("TOTAL")
    # print("ITERATIONS = ", number_of_iterations_list)
    # print("BACKTRACKS = ", number_of_backtracks_list)
    # print("CONFLICTS = ", number_of_conflicts_list)
