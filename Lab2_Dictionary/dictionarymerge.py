dict1={1:"a",2:"b"}
dict2={3:"aa",4:"bb"}
dict3={5:"aaa",6:"bbb"}

def merge_dict1(a,b,c):
    merged_dict=dict1|dict2|dict3
    return merged_dict

def merge_dict2(a,b,c):
    merged=dict1.copy()
    merged.update(dict2)
    merged.update(dict3)
    return merged
    
def merge_dict3(a,b,c):
    merge_dict={}
    for key,value in dict1.items():
        merge_dict[key]=value

    for key,value in dict2.items():
        merge_dict[key]=value

    for key,value in dict3.items():
        merge_dict[key]=value

    return merge_dict

print(f"merge_dict1 return {merge_dict1(dict1,dict2,dict3)} \n merge_dict2 return {merge_dict2(dict1,dict2,dict3)} \n merge_dict3 return {merge_dict3(dict1,dict2,dict3)} \n")
