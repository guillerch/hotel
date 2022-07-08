# Hotel manager

Este es un modelo para la prueba de tuGerente, a continuación se explica los pasos de instalacion del mismo.

- Se crearon los siguientes endpoints:
- Users: nos permite crear a los clientes en sistema y editar su información. (http://localhost:8000/customers/)
- Rooms: nos permite crear los tipos de habitaciones de un hotel. (http://localhost:8000/rooms/)
- Reservation: nos permite gestionar las reservas que realizan los clientes y el tipo de habitación que solicitan. (http://localhost:8000/reservations/)
- Payments: nos permite guardar los datos del pago que realiza el cliente y el monto a pagar. (http://localhost:8000/payments/)

## Instalacion

Crea un entorno virtual e instala los requerimientos

```bash
$ virtualenv -p $(which python3) <nombre_de_entorno>
$ source <nombre_de_entorno>/bin/activate
$ pip install -r requirements.txt

# Ejecutamos las migraciones
$ python manage.py migrate
```
Crea un super usuario para acceder al panel de administrador

```bash
$ python3 manage.py createsuperuser

# Iniciamos el servidor
$ python3 manage.py runserver 0.0.0.0:8000
```
