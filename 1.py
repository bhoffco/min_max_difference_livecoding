array = [15,22,84,14,88,23]
minimum = ""
maximum = ""



def the_min(array):

    minimum = min(array)
    maximum = max(array)
    difference = maximum - minimum
        

    return minimum, maximum, difference
    

print(the_min(array))

    
