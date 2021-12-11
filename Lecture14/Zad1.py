def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return None
list = [1,2,3,4,5]
print(find_element_in_list(6,list))