# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.


cost = int(input('Введите издержки фирмы '))
profit = int(input('Введите выручку фирмы '))
benefit = profit - cost
if benefit > 0:
    efficiency = profit/benefit
    print(f"Издержки фирмы меньше чем выручка на {benefit} позиций")
    print(f"Рентабельность выручки составляет {efficiency:.0f} позиций")
    employees = int(input('Введите количество сотрудников компании для расчета премий '))
    print(f"Премия составит {benefit/employees:.2f} позиций на каждого сотрудника")

elif cost == profit:
    print('Компания работает в 0')
else:
    print(f"Выручка фирмы меньше издержек на {(-1)*benefit} позиций")