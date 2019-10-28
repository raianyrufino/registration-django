## Required

1. Clone in the project.
```bash
$ git clone https://github.com/raianyrufino/registration_django
```

2. Enter the root directory of the project.
```bash
your / path / registration_django
```

3. Create [`virtualenv`] (https://virtualenv.pypa.io/en/latest/index.html).
3.1. You must have sudo access.
   ```bash
   # Install the virtualenv tool from pip3 (python3)
   $ [sudo] pip3 install virtualenv
   # Create a virtual env (virtual machine) 'env'
   $ virtualenv env
   # Activate your virtual machine!
   $ source env / bin / activate
   ```

4. Install all project dependencies.
   ```bash
   (env) $ pip install -r requirements.txt
   ```
5. Configure database:
```bash
   (env) $ python manage.py makemigrations
   (env) $ python manage.py migrate
```

6. Create an adm account:
```bash
   (env) $ python manage.py createsuperuser
```
Enter login name, email and password.

7. Run the project.

```bash
   (env) $ python manage.py runserver
```
