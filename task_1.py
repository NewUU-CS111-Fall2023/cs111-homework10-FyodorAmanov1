def merge_nodes(arr):
    merged_list = []
    sum_between_zeros = 0

    for value in arr:
        if value == 0:
            merged_list.append(sum_between_zeros)
            sum_between_zeros = 0
        else:
            sum_between_zeros += value
    
    print(merged_list)