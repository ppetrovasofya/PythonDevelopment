users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

unique_users = set(users)

basic_list = len(users)
unique_list = len(unique_users)

statistic = {"Общее количество": basic_list,
             "Уникальные посещения": unique_list}

print(statistic)
