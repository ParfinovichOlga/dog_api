# dog_api
Dog api is api for retrieving and managing dogs breed data and retrieving managing real dogs data of concrete breed.
dog_api includes two main endpoints:
- api/breeds
- api/dogs

api/breeds has additional field with dogs count of current breed.

api/dogs has additional field with average dog age of this breed.

api/dogs/{id} has additional field with dogs count of its breed.


## Installation
- git clone git@github.com:ParfinovichOlga/dog_api.git
- docker-compose up

## Usage
See the api swagger documentation on localhost:8000/api/docs when docker container is run
