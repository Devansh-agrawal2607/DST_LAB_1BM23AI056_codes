import sys
num_test_cases = int(input().strip())

for _ in range(num_test_cases):
    num_elements_a, num_elements_b, max_sum = input().strip().split(' ')
    num_elements_a, num_elements_b, max_sum = [int(num_elements_a), int(num_elements_b), int(max_sum)]
    list_a = list(map(int, input().strip().split(' ')))
    list_b = list(map(int, input().strip().split(' ')))

    list_a = list_a[::-1]
    list_b = list_b[::-1]

    temp_storage = []
    total_elements = 0
    current_sum = 0

    while len(list_a) > 0:
        if current_sum + list_a[-1] <= max_sum:
            temp = list_a.pop()
            temp_storage.append(temp)
            current_sum += temp
            total_elements += 1
        else:
            break
    sum_b = 0
    while len(list_b) > 0:
        if sum_b + list_b[-1] <= max_sum:
            if current_sum + list_b[-1] <= max_sum:
                temp = list_b.pop()
                current_sum += temp
                sum_b += temp
                total_elements += 1
            else:
                temp = list_b.pop()
                current_sum = current_sum - temp_storage.pop() + temp
                sum_b += temp
        else:
            break
    print(total_elements)