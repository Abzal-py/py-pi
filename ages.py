ages = [_ for _ in range(0,31)]
child_counter = 0
teenager_counter = 0
adult_counter = 0
for age in ages:
    age_range = 'child' if age<13 else 'teenager' if age <18 else 'adult'
    child_counter += 1 if age_range == 'child' else 0
    teenager_counter +=1 if age_range == 'teenager' else 0
    adult_counter +=1 if age_range == 'adult' else 0    
print(f'childs: {child_counter}, teenagers: {teenager_counter}, adults: {adult_counter}')