money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
budget = money_capital + salary

while budget >= spend:
    months += 1
    budget += salary - spend
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
