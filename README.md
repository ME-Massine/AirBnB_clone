# AirBnB clone - The Console

## Description

This project is the first version of the AirBnB project, which is an AirBnB clone that includes design, layout, infrastructure and database. In this repository you will find the AirBnB console, which executes specific commands (shown below) to make specific actions.

## Code Style
[Pycodestyle](https://pypi.org/project/pycodestyle/) was taken into account and implemented for all files.

## Files and Directories
- ```models``` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- ```tests``` directory will contain all unit tests.
- ```console.py``` file is the entry point of our command interpreter.
- ```models/base_model.py``` file is the base class of all our models. It contains common elements:
    - attributes: ```id```, ```created_at``` and ```updated_at```
    - methods: ```save()``` and ```to_json()```
- ```models/engine``` directory will contain all storage classes (using the same prototype). For the moment I will have only one: ```file_storage.py```.
