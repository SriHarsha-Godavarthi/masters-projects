import random

def genarateRandomList(number_of_elements,maximum_range):
    #1. generate a random list contains elements whose value should be less than 
    #   or equal to the upperbond (i.e maximum_range)
    #2. after generating each random number check wheather the number is greater than 50 
    # if the above mentioned condition is true then increment count of greaterThanFifty
    #3. after generating complete list then check if greaterThanFifty>5 then sort in Ascending Order and delete 5th element
    # otherWise sort in Descending Order and delete second element
    # return sorted list and isAscendingOrder
    greaterThanFifty=index_of_element=0
    random_numbers=[]
    isAscendingOrder=False
    while index_of_element<=number_of_elements:
        random_number=random.randint(1,maximum_range)
        random_numbers.append(random_number)
        if greaterThanFifty<=5 and random_number>50:
            greaterThanFifty+=1
        index_of_element+=1
    print("unsorted",random_numbers)
    if greaterThanFifty>5:
        #sort elements in increasing order and delete 5th element
        random_numbers.sort()
        random_numbers.pop(4)
        isAscendingOrder=True
    else:
        #sort elements in descending order and delete 2nd element
        random_numbers.sort(reverse=True)
        random_numbers.pop(1)
    
    return {"random_numbers": random_numbers,"isAscendingOrder": isAscendingOrder}

def binaryInsertion(random_numbers,new_element,isAscendingOrder):
    # we will be using binary search concept to insert new element in the given list
    start, end = 0, len(random_numbers) #start=0 , end = length of random_numbers list
    positionToInsert=((start+end)//2) # find middle position
    found=False # Assign found to False
    lengthOfList=len(random_numbers)
    while not found:
        if isAscendingOrder:
            # if the list is  sorted in ascending order check the below conditions
            if positionToInsert<0:
                #if the middlePosition is less than zero then inserting position should be between 0,1
                if new_element<random_numbers[0]:
                    positionToInsert=0
                else:
                    positionToInsert =1
                return positionToInsert
            
            elif positionToInsert>lengthOfList-1:
                #if the middlePosition is greater than last element index then inserting position is either last (or) last second element
                if new_element>random_numbers[lengthOfList-1]:
                    positionToInsert=lengthOfList
                else:
                    positionToInsert =lengthOfList-1
                return positionToInsert
            
            elif new_element==random_numbers[positionToInsert]:
                #inserting element is equal to middle elements value then return middle position
                 return positionToInsert
            elif new_element<random_numbers[positionToInsert]:
                end=positionToInsert-1
            else:
                start=positionToInsert+1
            # the condition to check correct insertion position for Ascending order are given below
            # 1. if ascending order left element should be less than inserting element
            # 2. right element of inserting element should be greater
            # 3. this condition don't work for starting and ending elements
            if new_element<random_numbers[positionToInsert] and random_numbers[positionToInsert-1]<new_element:
                found=True
        else:
            # if the list is  sorted in descending order check the below conditions
            if positionToInsert<0:
                #if the middlePosition is less than zero then inserting position should be between 0,1
                if new_element>random_numbers[0]:
                    positionToInsert=0
                else:
                    positionToInsert =1
                return positionToInsert
            
            elif positionToInsert>lengthOfList-1:
            #if the middlePosition is greater than last element index then inserting position is either last (or) last second element
                if new_element<random_numbers[lengthOfList-1]:
                    positionToInsert=lengthOfList
                else:
                    positionToInsert =lengthOfList-1
                return positionToInsert
            
            elif new_element==random_numbers[positionToInsert]:
                    #inserting element is equal to middle elements value then return middle position
                 return positionToInsert
            elif new_element<random_numbers[positionToInsert]:
                start=positionToInsert+1
            else:
                end=positionToInsert-1
            # the condition to check correct insertion position for descending order are given below
            # 1. if descending order left element should be greater than inserting element
            # 2. right element of inserting element should be lesser
            # 3. this condition don't work for starting and ending elements
            if new_element<random_numbers[positionToInsert-1] and new_element>random_numbers[positionToInsert]:
                found=True
        if not found:
            #if found is not true recalculate the middle position
            positionToInsert=((start+end)//2)
    return positionToInsert

def binarySearch(random_numbers,new_element,isAscendingOrder):
    # we will be using binary search concept to insert new element in the given list
    start, end = 0, len(random_numbers) #start=0 , end = length of random_numbers list
    positionToInsert=((start+end)//2) # find middle position
    lengthOfList=len(random_numbers)
    found=False # Assign found to False
    while not found:
        if  positionToInsert<0:
            found=True
            if new_element==random_numbers[0]:
                return 0
            else:
                return 1
        elif positionToInsert>lengthOfList-1:
            found=True
            if new_element==random_numbers[lengthOfList-1]:
                return lengthOfList
            else:
                return lengthOfList-1
        elif new_element==random_numbers[positionToInsert]:
            found=True
            return positionToInsert
        elif isAscendingOrder:
            # if the list is  sorted in ascending order check the below conditions
            if new_element<random_numbers[positionToInsert]:
                end=positionToInsert-1
            else:
                start=positionToInsert+1
        else:
            # if the list is  sorted in descending order check the below conditions
            if new_element<random_numbers[positionToInsert]:
                start=positionToInsert+1
            else:
                end=positionToInsert-1
        if not found:
            #if found is not true recalculate the middle position
            positionToInsert=((start+end)//2)
    return positionToInsert

def linearSearch(random_numbers,searchElement):   
    positionToInsert=0
    for element in random_numbers:
        if searchElement==element:
            return positionToInsert
        else:
            positionToInsert+=1
    return "element not found"