#taking input length:
arr=[]
global_arr=[]
for i in range(int(input('Enter total values: '))):
    arr.append(int(input('Value: ')))
    global_arr.append(0)
global_arr.append(0)

def make_tree(arr):
    for i in range(0,len(arr)):
        #replace the arr[i] value with required value
        #like even or odd
            ################
        if arr[i]%2==0:
            update(1,i+1)
        else:
            update(0,i+1)
            #############
    print('Values Updated')

def update(val,index):
    global global_arr
    if index > u_limit:
        return
    else:
        global_arr[index]+=val
        index=next_item(index)
        update(val,index)
        return

def next_item(index):
    next_index=index+(index&(-index))
    if index>u_limit:
        return -1
    return next_index

def parent_item(index):
    global u_limit
    parent_index=index-(index&(-index))
    if index<=0:
        return -1
    return parent_index

def zero_to_index(index):
    suma=0
    while(True):
        next_index=parent_item(index)
        if next_index<=-1:
            return suma
        suma+=global_arr[index]
        index=next_index

def query_request(start_i,end_i=None):
    if end_i==None:
        (end_i,start_i)=(start_i,start_i-1)
    else:
        (end_i,start_i)=(end_i,start_i-1)

    val1=zero_to_index(end_i)
    val2=zero_to_index(start_i)
    return(val1-val2)

u_limit=len(arr)
make_tree(arr)

print(global_arr[1:])

var1, var2 = input().split()
(var1,var2)=(int(var1),int(var2))

print(query_request(var1,var2))
