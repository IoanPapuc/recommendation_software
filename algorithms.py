from dataset import genres, collection



def linear_search(list, target):
    matches = []
    for item in list:
        if target == item[0:len(target)]:
            matches.append(item)
    return matches


#print("Linear search: \n", linear_search(genres, 'h'))