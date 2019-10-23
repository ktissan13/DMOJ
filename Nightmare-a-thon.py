# Tissan Kugathas
# DMOJ
# Nightmare a thon
# August 12 2019

Q_list = []
user_input = input()

values = user_input.split()

N = int(values[0])
Q = int(values[1])

ratings = input()
N_list = ratings.split()
for integer in range(Q):
    Q_list.append(input())

for integer in Q_list:
    temp = integer.split()
    first_skip = int(temp[0])
    last_skip = int(temp[1])
    N_index = 1
    temp_list = []
    five_counter = 0
    for rating in N_list:
        if not first_skip <= N_index <= last_skip:
            temp_list.append(int(rating))
        N_index += 1
    for rating in temp_list:
        if rating == 5:
            five_counter += 1
    print("5", five_counter)
            
        
        
    
        
