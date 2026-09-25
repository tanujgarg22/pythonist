def mergelist_to_dict():
    lista=[1,2,3,4,5]
    listb=["a","b","c","d","e"]
    merge_dict={}
    return dict(zip(lista,listb))

def mergelist_to_dict2():
    lista=[1,2,3,4,5]
    listb=["a","b","c","d","e"]
    merge_dict={}
    for i,k in enumerate(lista):
        #enumerate strt from 0
        #range start from 1

        print(f"merge_dict[k] merge_dict[{k}] listb[i] {i}")
        merge_dict[k]=listb[i]
    return merge_dict

print(mergelist_to_dict())
print(mergelist_to_dict2())