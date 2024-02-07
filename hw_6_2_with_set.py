my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}

union_dict = {}

list_with_keys_in_both_dicts = list(set(my_dict_1).intersection(set(my_dict_2)))

list_with_unic_keys_in_my_dict_1 = list(set(my_dict_1).difference(set(my_dict_2)))

dict_with_unic_keys_in_my_dict_1 = {list_with_unic_keys_in_my_dict_1[i]: my_dict_1.get(list_with_unic_keys_in_my_dict_1[i])
                                    for i in range(len(list_with_unic_keys_in_my_dict_1))}

dict_with_unic_keys_in_my_dict_2 = {list(my_dict_2)[i]: my_dict_2.get(list(my_dict_2)[i]) for i in range(len(my_dict_2))
                                    if list(my_dict_2)[i] not in list_with_keys_in_both_dicts}

dict_with_keys_in_both_dicts = {list_with_keys_in_both_dicts[i]: [my_dict_1.get(list_with_keys_in_both_dicts[i]),
                                                                  my_dict_2.get(list_with_keys_in_both_dicts[i])]
                                for i in range(len(list_with_keys_in_both_dicts))}

union_dict.update(dict_with_unic_keys_in_my_dict_1)
union_dict.update(dict_with_unic_keys_in_my_dict_2)
union_dict.update(dict_with_keys_in_both_dicts)

print(f'Список із ключів, які є в обох словниках - {list_with_keys_in_both_dicts}')
print(f'Cписок із ключів, які є у першому, але немає у другому словнику - {list_with_unic_keys_in_my_dict_1}')
print(f"Cловник з пар {{ключ:значення}} для ключів, які є в першому, але немає в другому словнику - "
      f"{dict_with_unic_keys_in_my_dict_1}")
print(f"Об'єднаний словник за двома правилами - {union_dict}")
