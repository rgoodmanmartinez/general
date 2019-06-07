def calcualte_valley_area(li):
    min_side = min(li[0],li[-1])
    area = min_side * (len(li) - 2)
    inner_list = li[1:-1]

    for val in inner_list:
        area = area - min(min_side,min(val,min_side))
    return area

def calculate_area(li):
    start_position = 0
    total_area = 0
    start_valley = 0
    end_valley = 0
    uphill = 0
    
    if(len(li) <= 1):
        return 0

    for i in range(1,len(li),1):
        if(li[i] <= li[i-1]):
            start_valley = i-1
            break

    for i in range(start_valley + 1,len(li),1):
        if(i == len(li)-1): # end of list
            end_valley = len(li)
        if(li[i] > li[i-1]): # start moving uphill
            uphill = 1
        if(uphill and li[i] <= li[i-1]): # reached the end of the valley
            end_valley = i 
            break

    if(end_valley != len(li)):
        total_area = calcualte_valley_area(li[start_valley:end_valley]) + calculate_area(li[end_valley-1:len(li)])
    else:
        total_area = total_area + calcualte_valley_area(li[start_valley:end_valley])
    
    return total_area

print('[2,1,1,1,2,1,1,3]: ',calculate_area([2,1,1,1,2,1,1,3]))
print('[1,2,3,3,1,2]: ',calculate_area([1,2,3,3,1,2]))
print('[1,2,3,3,2,1]: ',calculate_area([1,2,3,3,2,1]))
print('[6,5,4,4,4,4,1,2,3,0,2]: ',calculate_area([6,5,4,4,4,4,1,2,3,0,2]))

