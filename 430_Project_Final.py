
# coding: utf-8

# In[64]:

import glob as gb
import re
import os


# In[66]:

def pairs_generator (data):
    Read_File = open(data)
    Data_Points = Read_File.read().split('\n')
    File_Number = re.findall('\d+',data)
# Reading points from text files
    number_of_data_points = Data_Points[0]
    points = []
    for dat in Data_Points[1:]:
        X_axis = int(dat.split(' ')[0])
        Y_axis = int(dat.split(' ')[1])
        points.append((X_axis, Y_axis))
    return points, number_of_data_points,File_Number[0]


# In[67]:

def Parallel_Lines_Generator(points, number_of_data_points):
    # Creating points to be traversed vertically and horizontally
    Vertical_Lines = []
    Horizontal_Lines = []
    for j in range(1,int(number_of_data_points)):
        a = j + 0.5
        Vertical_Lines.append(a)
        Horizontal_Lines.append(a)
    Set_of_Pairs = [] 
    for i in range(0,len(points)):
        for j in range(i+1, len(points)):
            Set_of_Pairs.append((points[i],points[j]))
    Solution_Set = []

    while Set_of_Pairs != None:
        if len(Set_of_Pairs) == 0:
            break
        Vertical_counter = []
        for v in Vertical_Lines:
            edge_counter = 0
            for pair in Set_of_Pairs:
                if((pair[0][0]<v) and (pair[1][0])>v):
                    edge_counter += 1
            Vertical_counter.append(edge_counter)
        Vertical_max_cut = max(Vertical_counter)
        Vertical_max_line = Vertical_Lines[Vertical_counter.index(Vertical_max_cut)]
        Horizontal_counter = []
        for h in Horizontal_Lines:
            edge_counter = 0
            for pair in Set_of_Pairs:
                if((pair[0][1]<h) and (pair[1][1])>h) or ((pair[0][1]>h) and (pair[1][1])<h):
                    edge_counter += 1
            Horizontal_counter.append(edge_counter)
        Horizontal_max_cut = max(Horizontal_counter)
        Horizontal_max_line = Horizontal_Lines[Horizontal_counter.index(Horizontal_max_cut)]
        edges_remove = []
        if Vertical_max_cut > Horizontal_max_cut:
            Solution_Set.append('v ' + str(Vertical_max_line))
            for pair in Set_of_Pairs:
                if (((pair[0][0]<Vertical_max_line) and (pair[1][0])>Vertical_max_line) or ((pair[0][0]>Vertical_max_line) and (pair[1][0])<Vertical_max_line)):
                    edges_remove.append(pair)
            Vertical_Lines.remove(Vertical_max_line)
        else:
            Solution_Set.append('h ' + str(Horizontal_max_line))
            for pair in Set_of_Pairs:
                if (((pair[0][1]<Horizontal_max_line) and (pair[1][1])>Horizontal_max_line) or ((pair[0][1]>Horizontal_max_line) and (pair[1][1])<Horizontal_max_line)):
                    edges_remove.append(pair)
            Horizontal_Lines.remove(Horizontal_max_line)
        for edge in edges_remove:
            Set_of_Pairs.remove(edge)    
    return Solution_Set


# In[68]:

def Output_File_Generator(Solution_Set, File_Number):
    Output_Name = 'output_greedy/greedy_solution'+File_Number
    d = os.path.dirname(Output_Name)
    if not os.path.exists(d):
        os.makedirs(d)
    Output_File = open(Output_Name, 'w')
    Output_File.write(str(len(Solution_Set)) + '\n')
    for s in Solution_Set:
        Output_File.write(s +'\n')
    Output_File.close()
    return


# In[69]:

def main():
    input_files = gb.glob('input/*')
    for data in input_files:
        print(data)
        points, number_of_data_points, File_Number = pairs_generator(data)
        Solution_Set = Parallel_Lines_Generator(points, number_of_data_points)
        Output_File_Generator(Solution_Set, File_Number)
        print('Output Generated')

if __name__ == "__main__": 
    main()

