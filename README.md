# turboself-api
API for the TurboSelf web application.

Is able to fetch user reservations, remaining credits and account data.


## Installation

- Install beautifulSoup (`pip install beautifulsoup`)

- Clone and the repository and run:

```sh
git clone https://github.com/Egsagon/turboself-api
cd turboself-api/
python3 main.py
```

## Usage

There is an example usage in the `main.py` file which show how to print resservations per week:
```py
import turboself

client = turboself.Client('username', 'password')

for week in client.get_reservations():
    print(f'WEEK {week.date.month}/{week.date.year}')
    
    for day in week.days:
        do_eat = '92myes' if day.eat else '91mno'
        if not day.can_eat: do_eat = '30mno'
        
        print(f'\t* {day.date.date()}: \033[{do_eat}\033[0m')
```

![demo](https://github.com/Egsagon/turboself-api/blob/master/demo.png)