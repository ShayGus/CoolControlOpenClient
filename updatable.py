from abc import ABC, abstractmethod
from dataclasses import dataclass
import re
from typing_extensions import Required
from marshmallow import Schema, fields, post_load, ValidationError


###
# {'data': {'ambientTemperature': 29,
#           'deviceId': '61bb087a212f1c7c42b9e76a',
#           'fan': 3,
#           'filter': False,
#           'internalId': '283B960300D4:31303336',
#           'operationMode': 0,
#           'operationStatus': 2,
#           'serviceUnits': [],
#           'setpoint': 25,
#           'site': '61f8e091a8a31c1966b33a29',
#           'swing': 6,
#           'temperatureScale': 1,
#           'unitId': '61f8e56960bf483d1e5b0743'},
#  'name': 'UPDATE_UNIT'}
###


class UnitUpdate(Schema):
    ambient_temperature = fields.Integer(required=False, data_key = "ambientTemperature")
    unit_id = fields.Str(required=True, data_key = "unitId")
    fan = fields.Integer(reuired=True)
    filter = fields.Bool()
    operation_mode = fields.Integer(reuired=True, data_key="operationMode")
    operation_status = fields.Integer(reuired=True, data_key="operationStatus")
    setpoint = fields.Integer(reuired=True)
    swing = fields.Integer(reuired=True)
    temperature_scale = fields.Integer(reuired=True, data_key="temperatureScale")


class Updatable(ABC):
    @abstractmethod
    def notify(self, message):
        pass

    @abstractmethod
    def get_updatable_id(self) -> str:
        pass
