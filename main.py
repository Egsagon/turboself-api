import turboself

client = turboself.Client('xxx', 'xxx')

for week in client.get_reservations():
    print(f'WEEK {week.date.month}/{week.date.year}')
    
    for day in week.days:
        do_eat = '92myes' if day.eat else '91mno'
        if not day.can_eat: do_eat = '30mno'
        
        print(f'\t* {day.date.date()}: \033[{do_eat}\033[0m')
