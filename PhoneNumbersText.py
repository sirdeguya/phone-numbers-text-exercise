input_numbers = ['054-889-5564', '55-9852456', '054 889 5532']
# we want: 0548895564

def normalize(phone_number: str): 
    normalize_num = ""
    if phone_number[0] != "0":
        normalize_num = "0"
    normalize_num = normalize_num + normalize_num.join(phone_number.replace("-"," ").split(" "))
    return (normalize_num)

normalize_list = []
for nums in input_numbers :
    normalize_list.append(normalize(nums))
print(normalize_list)
