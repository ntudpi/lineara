
# DPI - Lineara

## To run in localhost

Make sure that you have python 3.6 or higher

Then install Django by using `pip3 install Django==2.1.5` (virtual environment recommended)

You also need to install `Pillow` which will be use to serve the images by `pip3 install Pillow==5.4.1`

Go into the project directory where the file `manage.py` resides

Run the command `python3 manage.py runserver` and you will be able to access the website from `localhost:8000` using your browser

## How it works
Some important components in a Django project are: `app`, `project app`, `manage.py`.

### `app` & `project app`
A Django project can consists of one or many apps, with the minimum requirement of that `project app` must exist. `project app` is the app which usually has the same name with the project name. In this case, the directory `lineara` is the project app, and `my_collection` is one example of other apps.`project app` is the entry point for a site that routes requests to other `app`s as specified.

### `project app`
Project app typically has `settings.py`, `urls.py`. 

#### `settings.py`
`settings.py`, as the name suggests is where we store and declare settings for the project, for example. database setting:
``` python3
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}
```
For reference, read https://docs.djangoproject.com/en/2.1/topics/settings/.
#### `urls.py`
`urls.py` is the end point that routes requests based on the `url` to other apps' `urls.py`, or to a view function.
```python
urlpatterns = [
	path('account/', admin.site.urls),
	path('', include('my_collection.urls')),
]
```
In the example above, the `urls.py` routes request with any prefix `account/` to the `admin.site.urls`, which is also a `urls.py`. It also routes request with any prefix of empty string, which means just routes any request to `my_collection.urls`. Question that might arise is that how does it determine where to route url request of `account/admin/`? `account/admin/` suffice both the prefix of `account/` and empty string. The answer is that it will route to the longest matching `urlpatterns`. So, `account/admin/` will be routed to `admin.site.urls` since `account/` is longer than empty string. 
### other `app`
Apps that are not project app typically contains `models.py`, `forms.py`, `views.py`, `urls.py`, `admin.py`, `templates/` and some other less interesting files.

For reference, read https://docs.djangoproject.com/en/2.1/topics/http/urls/.
#### `models.py`
`models.py` is the file where we declare the database tables and the constraints.
```python
class Item(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100, null=True)
	...
```
In the snippet above, we are declaring a model of name `Item` (it will manifest as a relation table in the database). The model `Item` has fields`name`, `location`, and some others, each will manifest as a column in the table. The field `name` is type of `CharField`, with maximum length of 100, which is equivalent to `VARCHAR(100)` in `SQL`. The field location has additional constraint of `null=True`, hence it allows the field to be empty, which is not the case for field name. 

For reference, read https://docs.djangoproject.com/en/2.1/topics/db/models/.

#### `forms.py`
This file has the responsibility to serialize the models declared in the `models.py` to be represented as it's fields, subset, or other complex combination.
```
class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'
```
In this example of simple model `Item`, we just serialize it to all of it's available attribute (though we can add other additional constraints or logic).

For reference: https://docs.djangoproject.com/en/2.1/topics/forms/
#### `urls.py`
We have known how `urls.py` can route a url path to another `urls.py`. Now, we are at the `my_collection` app, where we are at the receiving side of routing from `urls.py` of the project app `lineara/`. 
``` python
urlpatterns = [
	path('', views.index, name='collection_index'),
	path('<int:item_id>/', views.detail, name='item_detail'),
	path('search/', views.search, name='search'),
	...
]
```
The first urlpattern 
In urlpattern we can have some kind of regex, as we can see in the example of `<int:item_id>/`. What it will do is that it will try to match the pattern (if it's an integer), then extract the integer and pass it as argument `item_id` to the view `detail`.
