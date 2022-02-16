def sort_012(input_list):
    f_index=0
    e_index=len(input_list)-1
    c_index=0
    while c_index<=e_index:
        if input_list[c_index]==0:
            input_list[c_index],input_list[f_index]=input_list[f_index],input_list[c_index]
            f_index+=1
            c_index+=1
        elif input_list[c_index]==2:
            input_list[c_index],input_list[e_index]=input_list[e_index],input_list[c_index]
            e_index-=1
        else:
            c_index+=1

#Test
test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
sort_012(test_case)
print(test_case) #Should return [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
sort_012(test_case)
print(test_case) #Should return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
sort_012(test_case)
print(test_case) #Should return [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
