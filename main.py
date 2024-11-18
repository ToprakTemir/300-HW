import random
import time
import matplotlib as plt

comparison_operation_count = 0
def comparison_op(el, c):
    global comparison_operation_count
    comparison_operation_count += 1
    return el == c

loop_inc_operation_count = 0
def loop_inc_op():
    global loop_inc_operation_count
    loop_inc_operation_count += 1

assignment_operation_3_count = 0
def assignment_op_3(result):
    global assignment_operation_3_count
    assignment_operation_3_count += 1
    return result

assignment_operation_4_count = 0
def assignment_op_4(result):
    global assignment_operation_4_count
    assignment_operation_4_count += 1
    return result

def algorithm(arr, n):
    res = 1
    for i in range(n):
        if comparison_op(arr[i], 'c'):
            for j in range(n, 0, -1):
                k = i + n
                for y in range(0, n + 1, j):
                    loop_inc_op()
                    k = assignment_op_4(k - 1)
                res = assignment_op_3(res + k)

        elif arr[i] == 'm':
            z = 1
            while z < n:
                z = assignment_op_4(2 * z)
                res = assignment_op_3(res + z)

        elif arr[i] == 'p':
            w = n
            res = res - 1
            while w > 0:
                w = assignment_op_4(w // 5)
                res = assignment_op_3(res + 1)

        elif arr[i] == 'e':
            for m in range(1, i + 1):
                loop_inc_op()
                p = m
                for l in range(m, n + 1):
                    for t in range(n, 0, -1):
                        p = assignment_op_4(p + t)
                res = assignment_op_3(res + p)

    return res

def create_random_input(n):
    c_prob = 1/8
    m_prob = 1/4
    p_prob = 1/8
    e_prob = 1/2
    arr = []
    for i in range(n):
        r = random.random()
        if r < c_prob:
            arr.append('c')
        elif r < c_prob + m_prob:
            arr.append('m')
        elif r < c_prob + m_prob + p_prob:
            arr.append('p')
        else:
            arr.append('e')
    return arr

def create_best_input(n, op=4):
    if op == 1:
        return ['c'] * n # any other letter works as well
    elif op == 2:
        return ['m'] * n # p works as well
    elif op == 3:
        return ['p'] * n
    elif op == 4:
        return ['p'] * n


def create_worst_input(n, op=4):
    if op == 1:
        return ['c'] * n # any other letter works as well
    elif op == 2:
        return ['c'] * n
    elif op == 3:
        return ['e'] * n
    elif op == 4:
        return ['e'] * n


def reset_global_variables():
    global comparison_operation_count
    global loop_inc_operation_count
    global assignment_operation_3_count
    global assignment_operation_4_count
    comparison_operation_count = 0
    loop_inc_operation_count = 0
    assignment_operation_3_count = 0
    assignment_operation_4_count = 0


if __name__ == "__main__":

    input_sizes = [1, 5, 10, 20, 30, 40, 50, 60, 70, 90, 100, 120, 130, 140, 150, 160, 170]
    op = 4

    times_list = {"bests": [], "worsts": [], "averages": []}

    for i in range(len(input_sizes)):
        reset_global_variables()

        input_size = input_sizes[i]

        # create inputs
        best_arr = create_best_input(input_size, op=op)
        worst_arr = create_worst_input(input_size, op=op)
        random_arr = create_random_input(input_size)
        reset_global_variables()

        init_time = time.time_ns()
        algorithm(best_arr, input_size)
        best_time = (time.time_ns() - init_time) / 1e9
        times_list["bests"].append(best_time)
        best_op_counts = op_counts.copy()
        reset_global_variables()

        # worst time
        init_time = time.time_ns()
        algorithm(worst_arr, input_size)
        worst_time = (time.time_ns() - init_time) / 1e9
        times_list["worsts"].append(worst_time)
        worst_op_counts = op_counts.copy()
        reset_global_variables()

        # average time
        random_times = []
        N = 10
        for i in range(N):
            random_arr = create_random_input(input_size)
            init_time = time.time_ns()
            algorithm(random_arr, input_size)
            t = (time.time_ns() - init_time) / 1e9
            random_times.append(t)
        random_time = sum(random_times) / N
        times_list["averages"].append(random_time)
        random_op_counts = [int(op_counts[i] / N) for i in range(5)]
        reset_global_variables()
        # print(op_counts)

        # below lines print the time it took for each input and each case to execute
        print(f"Case: best Size: {input_size} Elapsed Time (s): {best_time}")
        print(f"Case: worst Size: {input_size} Elapsed Time (s): {worst_time}")
        print(f"Case: average Size: {input_size} Elapsed Time (s): {random_time}")

        # and these below lines print the number of operations for each input and each case
        # the operation being counted can be adjusted above
        print(f"Operation count for the best case of the {op}'th operation: {best_op_counts[op]}")
        print(f"Operation count for the worst case of the {op}'th operation: {worst_op_counts[op]}")
        print(f"Operation count for the average case of the {op}'th operation: {random_op_counts[op]}")

        for case in times_list.keys():
            with open(f"{case}_times.txt", "w") as f:
                for i in range(len(times_list[case])):
                    f.write(f"{input_sizes[i]}: {times_list[case][i]}\n")

        print()






