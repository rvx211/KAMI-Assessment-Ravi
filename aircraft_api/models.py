"""This is module for aircraft object"""
from django.db import models
from django.conf import settings

from core.models import BaseModel
from user_api.models import User

# Create your models here.
class Aircraft(BaseModel):
    """This is Aircraft model

    Args:
        BaseModel (object): Base Model object for the entire application
    """
    aircraft_id = models.IntegerField()
    aircraft_passenger = models.FloatField()
    aircraft_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_aircrafts')

    class Meta:
        """This is Meta class for Aircraft model
        """
        unique_together = ('aircraft_id', 'aircraft_user')

    @property
    def aircraft_fuel_tank(self) -> int:
        """This is the aircraft's function to get the aircraft fuel tank capacity by 
        multiply the aircraft's ID with fuel tank multiplier

        Returns:
            int: Ammount of the aircraft fuel capacity
        """
        return self.aircraft_id * settings.FUEL_TANK_MULTIPLIER

    @property
    def aircraft_basic_fuel_consumption(self) -> float:
        """This is the aircraft's function to get the aircraft basic fuel consumption by 
        multiply the aircraft's ID with basic fuel multiplier

        Returns:
            float: Ammount of the aircraft basic fuel consumption per minute
        """
        return self.aircraft_id * settings.BASIC_FUEL_MULTIPLIER

    @property
    def aircraft_additional_fuel_consumption(self) -> float:
        """This is the aircraft's function to get the aircraft additional fuel consumption 
        by multiply the aircraft's passenger amount with additional fuel multiplier

        Returns:
            float: Ammount of the aircraft additional fuel consumption per minute
        """
        return self.aircraft_passenger * settings.ADDITIONAL_FUEL_MULTIPLIER

    @property
    def aircraft_maximum_flight_time(self) -> float:
        """This is the aircraft's function to get the aircraft maximum flight time by divide 
        the aircraft fuel tank capacity with summary of the aircraft basic fuel consumption 
        and the aircraft additional fuel consumption

        Returns:
            float: Ammount of the aircraft basic fuel consumption per minute
        """
        return self.aircraft_fuel_tank / (
            self.aircraft_basic_fuel_consumption + self.aircraft_additional_fuel_consumption)
