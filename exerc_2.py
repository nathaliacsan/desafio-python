import requests

request = requests

api = request.get('https://jsonplaceholder.typicode.com/users')
data = api.json()

# Uma função para exibir somente os nomes dos registros em ordem alfabética;


def show_names():

    new_list = []
    names = map(lambda name: name['name'], data)

    for name in names:
        new_list.append(name)

    ordered_list = sorted(new_list)
    for name in ordered_list:
        print(name)


show_names()

print('**********************')

# Uma função para exibir os nomes das cidades dos registros;


def show_cities():

    full_anddress = map(lambda address: address['address'], data)

    for address in full_anddress:
        print(address['city'])


show_cities()

print('**********************')

# Uma função para exibir o username e o e-mail com domínio .biz


def show_username_email():

    users = map(lambda user: user, data)

    for user in users:
        if 'biz' in user['email']:
            username = user['username']
            email = user['email']
            print(f'{username} - {email}')


show_username_email()
