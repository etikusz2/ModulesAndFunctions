def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'The ID of `greeting` in `great_pythons` is {id(greeting)}')
    print(f'local namespace in `greet_pythons`(1): {locals()}')

    def make_greeting(item: str) -> str:
        nonlocal greeting
        print(f'local namespace in `greet_pythons`(1): {locals()}')
        greeting = 'Hi '
        print(f'The ID of `greeting` in `great_pythons` is {id(greeting)}')
        print(f'local namespace in `greet_pythons`(2): {locals()}')
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, `greeting is {greeting}')
    print(f'The ID of `greeting` in `great_pythons` is {id(greeting)}')
    print(f'local namespace in `greet_pythons`(2): {locals()}')


names = ['John'] #, 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
