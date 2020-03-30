#@author = Jovan Karuna Cahyadi

import numpy as np
import time

class PrioQueue(object):
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])
        
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        index = 0
        for i in range(len(self.queue)):
            if(self.queue[i][0] < self.queue[index][0]): #kolom 0 adalah cost maka akan dicari cost
                index = i
        item = self.queue[index]
        del self.queue[index]
        return item

class Node:
    def __init__(self, data=None):
        self.matrix = data
        self.parent = None
        self.depth = 0

def print_path(node):
    if(node.parent == None):
        return
    print_path(node.parent)
    print("\n======================")
    print("Move "+str(node.depth)+" : ")
    print_matrix(node.matrix)


def read_file(filename):
    f = open(filename,"r+") 
    return f

def file_to_matrix(filename):
    text = read_file(filename)
    temp = text.read().split()
    matrix = np.reshape(temp,(4,4)).astype('int32')
    return matrix
    
def print_matrix(matrix):
    print("╔═══╦═══╦═══╦═══╗")
    for i in range(4):
        for j in range(4):
            print("║ ",end="")
            print(matrix[i][j], end="")
            if(matrix[i][j] < 10):
                print(" ", end="")
        print("║")
        if(i != 3):
            print("╠═══╬═══╬═══╬═══╣")
    print("╚═══╩═══╩═══╩═══╝")

def check_empty_space(matrix):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == 0):
                row = i
                column = j
    return row,column

def cost(depth,matrix,ans):
    counter = 0
    for i in range(4):
        for j in range(4):
            if((matrix[i][j] != ans[i][j]) and matrix[i][j] != 0):
                counter += 1
    return (depth+counter)

def change_zero(matrix):
    x,y = check_empty_space(matrix)
    matrix[x][y] = 16
    return matrix       

def find_X(matrix):
    matrix_temp = matrix.copy()
    x,y = check_empty_space(matrix_temp)
    sum = x+y
    return (sum % 2)

def kurang(matrix):
    counter = 0
    matrix_temp = matrix.copy()
    matrix_temp = change_zero(matrix_temp)
    matrix_temp = np.reshape(matrix_temp,(16,))
    for i in range(16):
        temp = matrix_temp[i]
        for j in range(i,16):
            if(temp > matrix_temp[j]):
                counter += 1
    return counter

def print_kurang(matrix):
    matrix_temp = matrix.copy()
    matrix_temp = change_zero(matrix_temp)
    matrix_temp = np.reshape(matrix_temp,(16,))
    for i in range(16):
        counter = 0
        temp = matrix_temp[i]
        for j in range(i,16):
            if(temp > matrix_temp[j]):
                counter += 1
        print("Fungsi Kurang("+ str(temp)+") = "+ str(counter))
    
def hasil_reachable(matrix):
    sum = find_X(matrix)
    sum += kurang(matrix)
    return sum

def solvable(matrix):
    sum = hasil_reachable(matrix)
    if(sum % 2 == 0):
        return True
    else:
        return False

def swap(matrix,row,column):
    x,y = check_empty_space(matrix)
    matrix[x][y] = matrix[row][column]
    matrix[row][column] = 0
    return matrix

def move(matrix,movement):
    matrix_temp = matrix.copy()
    x,y = check_empty_space(matrix_temp)
    if(movement == "left"):
        if(y != 0):
            y -= 1
    elif(movement == "right"):
        if(y != 3):
            y += 1
    elif(movement == "up"):
        if(x != 0):
            x -= 1
    elif(movement == "down"):
        if(x != 3):
            x += 1
    matrix_temp = swap(matrix_temp,x,y)
    return matrix_temp

def opposite_move(movement):
    if(movement == "left"):
        return "right"
    elif(movement == "right"):
        return "left"
    elif(movement == "up"):
        return "down"
    elif(movement == "down"):
        return "up"

def equal(matrix,ans):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != ans[i][j]):
                return False
    return True


#Main Algo Branch and Bound
final = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]).reshape(4,4)  
print ("Initial Matrix =")
path = "../test/"
matrix = file_to_matrix(path + "solve1.txt")
r,c = check_empty_space(matrix)
print("Empty Space at : ("+str(r)+","+str(c)+")")
print("Cost is : "+str(cost(0,matrix,final)))
print_matrix(matrix)
print_kurang(matrix)
print("Sigma Kurang(i) + X = " + str(hasil_reachable(matrix)))
movement = ("right","down", "left", "up")
print("\n--------------------------------")
if(solvable(matrix)):
    Queue = PrioQueue()
    '''PrioQueue : item[0] = cost
                   item[1] = Node
                   item[2] = movement_type
                   item[3] = langkah/step
    '''
    print("Solvable Puzzle\n")
    simpul_yang_dibangkitkan = 0
    print("Initial Matrix")
    simpul = Node(matrix)
    #push pertama
    start = time.time()
    Queue.enqueue((cost(0,simpul.matrix,final),simpul,"",0))

    Queue_temp = Queue.dequeue()
    simpul = Queue_temp[1]
    New_Matrix = simpul.matrix
    Move_balik = ""
    next_step = Queue_temp[3] + 1
    simpul_yang_dibangkitkan += 1

    while(not equal(New_Matrix, final)):
        for mov in movement:
            if(mov != Move_balik):
                after_move = move(New_Matrix,mov)
                if(not equal(after_move,New_Matrix)):
                    new_simpul = Node(after_move)
                    new_simpul.parent = simpul
                    new_simpul.depth = simpul.depth + 1
                    simpul_yang_dibangkitkan += 1
                    Queue.enqueue((cost(next_step,new_simpul.matrix,final),new_simpul,mov,next_step))      
        
        Queue_temp = Queue.dequeue()
        simpul = Queue_temp[1]
        New_Matrix = simpul.matrix
        Move= Queue_temp[2]
        Move_balik = opposite_move(Move)
        next_step = Queue_temp[3] + 1

    end = time.time()
    print_matrix(matrix)
    print_path(simpul)
    time= end - start
    print("\nTime taken = " +str(time) + " seconds")    
    print("Simpul yang dibangkitkan ada = " + str(simpul_yang_dibangkitkan))
else:
    print("Puzzle Cannot Be Solved")
