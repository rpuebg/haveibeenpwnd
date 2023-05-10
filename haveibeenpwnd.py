import requests
import hashlib

def check_email(email):
headers['hibp-api-key'] = 'TU_CLAVE_DE_API_AQUÍ'

    # Calcular el hash SHA-1 de la dirección de correo electrónico
    sha1 = hashlib.sha1(email.encode('utf-8')).hexdigest().upper()

    # Hacer una solicitud a la API de HIBP
    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/{}'.format(email)
    headers = {'User-Agent': 'Python script'}
    response = requests.get(url, headers=headers)

    # Comprobar si la dirección de correo electrónico se ha visto comprometida
    if response.status_code == 200:
        print('¡La dirección de correo electrónico {} se ha visto comprometida en las siguientes violaciones de datos:'.format(email))
        for breach in response.json():
            print('  - {} ({}): {}'.format(breach['Name'], breach['BreachDate'], breach['Description']))
    elif response.status_code == 404:
        print('La dirección de correo electrónico {} no se ha visto comprometida en ninguna violación de datos conocida.'.format(email))
    else:
        print('Error al hacer la solicitud a la API de HIBP: {}'.format(response.status_code))

def check_phone(phone):
headers['hibp-api-key'] = 'TU_CLAVE_DE_API_AQUÍ'

    # Hacer una solicitud a la API de HIBP
    url = 'https://haveibeenpwned.com/api/v3/pasteaccount/{}'.format(phone)
    headers = {'User-Agent': 'Python script'}
    response = requests.get(url, headers=headers)

    # Comprobar si el número de teléfono se ha visto comprometido
    if response.status_code == 200:
        print('¡El número de teléfono {} se ha visto comprometido en los siguientes pasteles de texto plano:'.format(phone))
        for paste in response.json():
            print('  - {} ({}): {}'.format(paste['Source'], paste['Date'], paste['Title']))
    elif response.status_code == 404:
        print('El número de teléfono {} no se ha visto comprometido en ningún pastel de texto plano conocido.'.format(phone))
    else:
        print('Error al hacer la solicitud a la API de HIBP: {}'.format(response.status_code))

def main():
    while True:
        print('Ingrese una opción:')
        print('1. Comprobar dirección de correo electrónico')
        print('2. Comprobar número de teléfono')
        print('0. Salir')

        try:
            option = int(input('>> '))
            if option == 1:
                email = input('Ingrese la dirección de correo electrónico a verificar: ')
                check_email(email)
            elif option == 2:
                phone = input('Ingrese el número de teléfono a verificar (sin espacios ni guiones): ')
                check_phone(phone)
            elif option == 0:
                break
            else:
                print('Opción inválida. Por favor ingrese una opción válida.')
        except ValueError:
            print('Por favor ingrese un número válido como opción.')

if __name__ == '__main__':
    main()
