def bianary_search(lists,check):

    low=0
    high=len(lists)-1

    while low <= high:
        mid= (low+high)
        guess=lists[mid]
        #print(guess) 
        if guess==check:
            return mid
        if guess > check:
            high= mid -1
        else:
            low=mid+1
    return None

my_list= [2,4,5,7,9,11,17,18,19]

x=bianary_search(my_list,-1)
y=bianary_search(my_list,19)
print(f"search from {my_list} and the locetion is {x} ")
print(f"search from {my_list} and the locetion is {y} ")



 