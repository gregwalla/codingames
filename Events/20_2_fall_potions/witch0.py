lst = ['12', 'act', '1','2','3','4', '10', '2','y','y' ,'?']

#
bs_ = {
    'action_id': [],
    'action_type' : [],
    'delta_0': [], 
    'delta_1': [],
    'delta_2': [],
    'delta_3': [],
    'price' : [],
    'tome_index' : [],
    'tax_count': [],
    'castable' : [], 
    'repeatable': []}

def append_dict(bs : dict, lst: list)->dict:
    """append dict by inserting left elements of the list """
    for key, value in bs.items():
        if key in ['delta_'+str(i) for i in range(4)]:
            value.append(int(lst.pop(0)))
        else: 
            value.append(lst.pop(0))
        
    return bs



bs = append_dict(bs_, lst)

print(bs)

lst = ['12', 'act', '1','2','3','4', '10', '2','y','y' ,'?']

for key, value in bs.items():
    if key in ['delta_'+str(i) for i in range(4)]:
        value.append(int(lst.pop(0)))
    else: 
        value.append(lst.pop(0))

print(bs)

{'action_id': ['62', '60', '42', '54', '53', '78', '79', '80', '81', '82', '83', '84', '85'], 
 'action_type': ['BREW', 'BREW', 'BREW', 'BREW', 'BREW', 'CAST', 'CAST', 'CAST', 'CAST', 'OPPONENT_CAST', 'OPPONENT_CAST', 'OPPONENT_CAST', 'OPPONENT_CAST'], 
 'delta_0': [0, 0, -2, 0, 0, 2, -1, 0, 0, 2, -1, 0, 0], 
 'delta_1': [-2, 0, -2, -2, 0, 0, 1, -1, 0, 0, 1, -1, 0], 'delta_2': [0, -5, 0, 0, -4, 0, 0, 1, -1, 0, 0, 1, -1], 
 'delta_3': [-3, 0, 0, -2, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
 'price': ['16', '15', '6', '12', '12', '0', '0', '0', '0', '0', '0', '0', '0'], 
 'tome_index': ['0', '0', '0', '0', '0', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1'],
 'tax_count': ['0', '0', '0', '0', '0', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1'], 
 'castable': ['0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1'], 
 'repeatable': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']}

me: [3, 0, 0, 0, 0] 
her: [3, 0, 0, 0, 0]
    
import sys
import math

def parse_actions(input())-> dict: 
    
    bs = {
    'action_id': [],
    'action_type' : [],
    'delta_0': [], 
    'delta_1': [],
    'delta_2': [],
    'delta_3': [],
    'price' : [],
    'tome_index' : [],
    'tax_count': [],
    'castable' : [], 
    'repeatable': []}
    
    action_count = int(input())
    
    for i in range(action_count):
        lst = [obj for obj in input().split()]



# game loop
while True:
    bs = parse_actions(input())
    
    stock1 = [int(j) for j in input().split()]
    stock2 = [int(j) for j in input().split()]

    # Write an action using print
    print(f'{bs}, me: {stock1} her: {stock2} ', file=sys.stderr, flush=True)

    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    #if  in ['BREW', 'CAST']: 
        print(f'WAIT')
    else :
        print(f'WAIT')

        
stock = [3,0,2,0]
cost = [-1,0,2,0]
diff = [1,1,1,1]

def can_brew(lst : list , lst2 : list)->bool:
    """"check if all list elements stay positive 
    after element wise substraction """
    diff = [a_i + b_i for a_i, b_i in zip(lst, lst2)]
    test = all([a_i >= 0 for a_i in diff])
    return test 

        
            

stock = [3,0,2,0]
cost = [-1,0,2,0]
                
                
can_brew(stock, cost)

delta_0 = [3,0,2,0]
delta_1 = [3,0,2,0]
delta_2 = [3,0,2,0]
delta_3 = [3,0,2,0]

brew_costs = [[delta_0[i], delta_1[i],delta_2[i],delta_3[i]] for i in range(4)]



action_ids = brew_ids[:5]

cast_ids = brew_ids[5:9]
create list of (brew_id, [brew_cost]) for each brew_item 
    for each receipe : 
        if can_brew(stock, brew_cost) :
            brew [brew_id]

        else : 
            cast [cast_id]
            
            
bs = {'action_id': ['50', '60', '52', '54', '45', '78', '79', '80', '81', '82', '83', '84', '85'], 
 'action_type': ['BREW', 'BREW', 'BREW', 'BREW', 'BREW', 'CAST', 'CAST', 'CAST', 'CAST', 'OPPONENT_CAST', 'OPPONENT_CAST', 'OPPONENT_CAST', 'OPPONENT_CAST'], 
 'delta_0': [-2, 0, -3, 0, -2,
                2, -1, 0, 0, 2, -1, 0, 0], 
 'delta_1': [0, 0, 0, -2, 0, 
                0, 1, -1, 0, 0, 1, -1, 0], 
 'delta_2': [0, -5, 0, 0, -2, 
                0, 0, 1, -1, 0, 0, 1, -1], 
 'delta_3': [-2, 0, -2, -2, 0, 
                0, 0, 0, 1, 0, 0, 0, 1], 
 'price': ['10', '15', '11', '12', '8', '0', '0', '0', '0', '0', '0', '0', '0'], 
 'tome_index': ['0', '0', '0', '0', '0', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1'],
 'tax_count': ['0', '0', '0', '0', '0', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1'], 
 'castable': ['0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1'], 
 'repeatable': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']}
            
print(f'CAST {bs['action_id'][5]}')

bs['action_id'][0] #'50'

receipe = [bs['delta_0'][0],#-2
           bs['delta_1'][0],#0
           bs['delta_2'][0], #0
           bs['delta_3'][0]#-2
          ] 

stock = [3,0,0,0]

if bs['delta_3'][0] < 0 : 
    for i in range s['delta_3'][0]
        make_element(4)



make  = cast(2) , cast(3), cast(4), 
        rest, 
        cast(2) , cast(3), cast(4), 
        rest,
        refill
        cast(2),  
        rest,  
        cast(2),  

        brew(receipe)
        
        while stock[0] <3 :
            print(f"CAST {bs['action_id'][5]}")
            print("REST")

stock = 




def make_element(i: int, j:int, stock : list, bs: dict)-> None: 
    if stock[i]  < receipe[j]
        if can_cast[]
        print(f"CAST {bs['action_id'][6+j]})
    
        print('REST')


action = 0
              
              
def refill(stock : list , bs: dict )-> None: 
    if stock[0] <3 :
        print(f"CAST {bs['action_id'][5]}")
                  
def rest()
    print("REST")
        
    if stock[0] <3 :
        cast(0)
            rest

receipe = [1,2,1, 2]
make  = cast(2) , cast(3), cast(4), 
        rest, 
        cast(2) , cast(3), cast(4), 
        rest,
        
        refill,
        cast(2), cast(3), 
        rest,  
        cast(2),  

        
        brew(receipe)
        
        
        

def get_current_brew_item()
    return(bs['action_id'][0])
def get_current_brew_costs()
    return(bs['action_id'][0] ,
     )

    def refill(stock : list , bs: dict )-> None: 
        if stock[0] <3 :
            print(f"CAST {bs['action_id'][5]}")
        else :
            pass

    def rest(c :int):

            print(f"REST")
        else : 
            pass
    
    def make_green():
        if hasblue
            print(f"CAST {bs['action_id'][6]}

    #i in [1,2, 3]
    def transform(stock: list, i: int) -> None:
        if stock[i-1] > 0 and bd['castable'][6+i] == 1:
            print(f"CAST {bs['action_id'][6+i]}
    
    transform(stock1, 1)

            

    def make_yellow():
        if hasorange :
            print(f"CAST {bs['action_id'][7]}

    
    refill(stock1)
    rest()

    #brewed = False

    #for i in range(5): 
        #if can_brew(stock1, brew_costs[i]):
    #    print(f'BREW {bs['action_id'][i]}')
    #    brewed = True

    #if brewed :
    #for i in range(5,9):
    if bs['castable'][5] == "1" :
        print(f"CAST {bs['action_id'][5]}")

    elif bs['castable'][6] == "1" :
        print(f"CAST {bs['action_id'][6]}")
    elif i%4 == 0 : 
        print("REST")
    elif bs['castable'][7] == "1" :
        print(f"CAST {bs['action_id'][7]}")
    #elif bs['castable'][8] == "1" :
    #    print(f"CAST {bs['action_id'][8]}")
    else :
        print("REST")

    
    
    #if 
    #print(f'WAIT')
                  

                  
                  
if counter  == 2:
        transform(2, stock1, bs)
    if counter  == 3:
        transform(3, stock1, bs)
    if counter == 4:
         rest() 
        #make last element again
    if counter  == 5:
        transform(1, stock1, bs)
    if counter  == 6:
        transform(2, stock1, bs)
    if counter  == 7:
        transform(3, stock1, bs)
    if counter == 8:
         rest() 
    if counter  == 9: 
        refill()


        



    
        

