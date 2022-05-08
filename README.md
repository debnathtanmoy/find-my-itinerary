# Find_my_itinerary

## Description
REST API's built with Django Rest Framework that allows various CRUD operations to get, post, update and delete 
travel itinearies.

## Getting Started
### Dependencies
Please check the requirements.txt file for dependencies.

To install the dependencies:

pip
```bash
pip install -r requirements.txt
```
or with conda
```bash
conda install -c conda-forge --file requirements.txt
```
### Executing program
- Clone the repository
- Go inside the directory find_my_itineary
- To use the apis, run the following command
```bash
python manage.py runserver 8080 (any other avaiable ports can also be used)
```
- Available API endpoints: 
    - http://127.0.0.1:8080/itineraries/get : Getting the list of all avaiable itinearies
    - http://127.0.0.1:8080/itineraries/post : Add a new itineary
    - http://127.0.0.1:8080/itineraries/get_by_id/<int:pk>/ : Get an itineary by id
    - http://127.0.0.1:8080/itineraries/put/<int:pk>/ : Update an itineary
    - http://127.0.0.1:8080/itineraries/delete/<int:pk>/ : Delete an itineary




