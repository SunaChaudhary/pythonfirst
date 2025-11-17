weekExpenses={
    'SundayExpenses':1000,
    'MondayExpenses':400,
    'TuesdayExpenses':500,
    'WednesdayExpenses':600,
    'ThusdayExpenses':200,
    'FridayExpenses':100,
    'SaturdayExpenses':800
}

total_weekExpenses=weekExpenses['SundayExpenses']+weekExpenses['MondayExpenses']+weekExpenses['TuesdayExpenses']+weekExpenses['WednesdayExpenses']+weekExpenses['ThusdayExpenses']+weekExpenses['FridayExpenses']+weekExpenses['SundayExpenses']
averageExpenses=total_weekExpenses//7 #for integer value // is used

print(f"total week expenses is {total_weekExpenses}")
print(f"Average week expenses is {averageExpenses}")