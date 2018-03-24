def rotate_matrix(input_list):
    output_list = []
    for lst in input_list:
      output_list += [[0,0,0]]
    c_1 = 2
    for lst in input_list:
        c_0 = 0 
        for i in lst:
            output_list[c_0][c_1] = i
            c_0 += 1
        c_1 -= 1
    return output_list