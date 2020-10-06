X = [8,19,3,4,6]
y = 22


smallest_length = 9999999
sum = 0

output_subarray_list = []

curr_arr = []

for i in range(len(X)):

    if(X[i] > y):
        smallest_length = 1
        output_subarray_list.append([[X[i]]])
        for j in range(len(output_subarray_list)):
            if(output_subarray_list[j] == []):
                pass
            else:
                if(len(output_subarray_list[j][0]) > 1):
                    output_subarray_list[j] = []

    
    elif(len(curr_arr) < 1):
        sum = X[i]
        curr_arr.append(X[i])

    
    else:
        sum = sum + X[i]
        curr_arr.append(X[i])
        if(sum > y and len(curr_arr) < smallest_length):
            output_subarray_list.append([curr_arr])
            smallest_length = len(curr_arr)

            curr_arr = []


for i in output_subarray_list:
    if(i == []):
        pass
    else:
        print(i[0])
