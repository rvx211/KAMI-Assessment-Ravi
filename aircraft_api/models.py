"""This is module for aircraft object"""
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

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
        verbose_name = _('user')
        verbose_name_plural = _('users')

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
    def aircraft_total_fuel_consumption_per_minute(self) -> float:
        """This is summary of the aircraft total consumption per minute

        Returns:
            float: Aircraft total consumption per minute
        """
        return self.aircraft_basic_fuel_consumption + self.aircraft_additional_fuel_consumption

    @property
    def aircraft_maximum_flight_time_in_minutes(self) -> float:
        """This is the aircraft's function to get the aircraft maximum flight time in minutes

        Returns:
            float: Ammount of the aircraft basic fuel consumption per minute
        """
        return self.aircraft_fuel_tank / self.aircraft_total_fuel_consumption_per_minute
