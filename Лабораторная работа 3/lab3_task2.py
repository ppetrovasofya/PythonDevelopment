def find_common_participants(participants1, participants2, a=","):
    participants1 = participants1.split(a)
    participants2 = participants2.split(a)
    common_participants = list(set(participants1).intersection(participants2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")