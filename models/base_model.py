#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            dtime_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], dtime_format)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], dtime_format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # as instructed also in task 5

    def __str__(self):

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict