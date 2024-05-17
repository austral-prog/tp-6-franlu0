def remove_elements(list_to_remove_elements):
    if len (list_to_remove_elements)>= 6:    
            del list_to_remove_elements[5]
            del list_to_remove_elements[4]
            del list_to_remove_elements[0]           
            
    elif len(list_to_remove_elements)==5:
           del list_to_remove_elements [4] 
           del list_to_remove_elements [0] 

    elif len(list_to_remove_elements)==0:
        list_to_add_elements=[]
    else:
        del list_to_remove_elements [0]
    return list_to_remove_elements         #Remove this line and implement

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements # Remove this line and implement

def is_empty(list_to_check):
    if list_to_check  ==  []:
        return  True
    else:
        return  False
    return "ANSWER HERE"  # Remove this line and implement

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        if list_to_compare1 [2] == list_to_compare2 [2]:
            return  True
        else:
            return  False
    else:
        return  False
def list_of_lists(list_of_lists_to_modify):
