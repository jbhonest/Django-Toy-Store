# Django Toy Store

This is a backend application for managing and selling toy products. The project also includes a blog system and a finance app to view list of paid orders.

## Features

- Add, view, update, and delete blog posts and comments
- Add, view, update, and delete products and comments
- Create cart and add products to cart
- View list of paid orders


## Installation
1. Clone the repository:
```bash
git clone https://github.com/jbhonest/django-toy-store.git
```
2. In **toystore** folder rename sample_settings.py to local_settings.py
3. Generate a SECRET_KEY and save it in local_settings.py

4. Navigate to the project directory:

```bash
cd django-toy-store
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Apply migrations to set up the database:
```bash
python manage.py migrate
```

7. Run the development server:
```bash
python manage.py runserver
```


## API Endpoints
* Blog API root: http://127.0.0.1:8000/api/blog/
* Store API root: http://127.0.0.1:8000/api/store/
* Cart API root: http://127.0.0.1:8000/api/cart/
  * To create a cart, send a post request to: http://127.0.0.1:8000/api/cart/carts
  * To add an item to a cart, send a post request to: http://127.0.0.1:8000/api/cart/carts/{cart_id}/items
  * To view items of a cart, send a get request to: http://127.0.0.1:8000/api/cart/carts/{cart_id}/items
  * To Checkout a cart, send a post request to: http://127.0.0.1:8000/api/cart/carts/{cart_id}/checkout
* Finance API root: http://127.0.0.1:8000/api/finance/


Use tools like curl, httpie, or Postman to interact with the API.



## Django Admin
First create an admin user:
```bash
python manage.py createsuperuser
```
Then access the Django admin interface at http://127.0.0.1:8000/admin/ to manage contacts.


---
Developed by Jamal Badiee (jbhonest@yahoo.com)