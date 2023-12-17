"""This is aircraft models module"""
from rest_framework import serializers

from core.exceptions.aircraft import (
    AircraftIDEmptyException,
    AircraftIDNotInteger,
    AircraftPassengerEmptyException,
    AircraftPassengerNotInteger,
    AircraftListEmptyException)
from ..models import Aircraft

class AircraftSerializer(serializers.ModelSerializer):
    """This is the aircraft serializer

    Args:
        serializers (object): Model serializer
    """
    aircraft_total_fuel_consumption_per_minute = serializers.SerializerMethodField()
    aircraft_maximum_flight_time_in_minutes = serializers.SerializerMethodField()

    class Meta:
        """This is class meta of the aircraft serializer
        """
        model = Aircraft
        fields = [
            'aircraft_id',
            'aircraft_passenger',
            'aircraft_total_fuel_consumption_per_minute',
            'aircraft_maximum_flight_time_in_minutes']
        ref_name = "AircraftSerializer v2"

    def validate_aircraft_id(self, value: int) -> int:
        """This is the aircraft ID validation

        Args:
            value (int): Aircraft ID

        Raises:
            AircraftIDEmptyException: Aircraft ID empty exception
            AircraftIDNotInteger: Aircraft ID is not integer exception

        Returns:
            int: Validated aircraft ID
        """
        if value in (None, ""):
            raise AircraftIDEmptyException
        if isinstance(value, int) is False:
            raise AircraftIDNotInteger
        return value

    def validate_aircraft_passenger(self, value: int) -> int:
        """This is the aircraft passenger validation

        Args:
            value (int): Aircraft passenger

        Raises:
            AircraftIDEmptyException: Aircraft passenger empty exception
            AircraftIDNotInteger: Aircraft passenger is not integer exception

        Returns:
            int: Validated aircraft passenger
        """
        if value in (None, ""):
            raise AircraftPassengerEmptyException
        if isinstance(value, float) is False:
            raise AircraftPassengerNotInteger
        return value

    def create(self, validated_data: dict) -> object:
        """This is override method of aircraft serializer

        Args:
            validated_data (dict): Aircraft Serializer validated dataa

        Returns:
            object: Aircraft model
        """
        validated_data['aircraft_user'] = self.context.get('user')
        # validated_data['username'] = self.context.get('user').username
        Aircraft.objects.update_or_create(validated_data)
        return self.data

class AircraftListSerializer(serializers.Serializer):
    """This is the aircraft list serializer

    Args:
        serializers (object): Django REST Framework serializer
    """
    aircraft = AircraftSerializer(many=True)
    
    class Meta:
        ref_name = "AircraftListSerializer v1"

    def validate_aircraft(self, value: list) -> list:
        """This is validate aircraft list function

        Args:
            value (list): Aircraft list

        Raises:
            AircraftListEmptyException: Aircraft list empty exception

        Returns:
            list: Validated aircraft list
        """
        if value in (None, "", []):
            raise AircraftListEmptyException
        return value

    def create(self, validated_data: dict) -> dict:
        """This is override create function of aircraft list serializer

        Args:
            validated_data (dict): Aircraft list serializer validated data

        Returns:
            dict: New aircraft list serializer validated data
        """
        aircraft_list = []
        for aircraft in validated_data['aircraft']:
            aircraft['user'] = self.context.get('user')
            aircraft['username'] = self.context.get('user').username
            aircraft_serializer = AircraftSerializer(data=aircraft)
            aircraft_data = {}
            if aircraft_serializer.is_valid():
                aircraft_data = aircraft_serializer.create(aircraft_serializer.validated_data)
            else:
                aircraft_data = aircraft_serializer.errors
            aircraft_list.append(aircraft_data)
        validated_data['aircraft'] = aircraft_list
        return validated_data

    def update(self, instance: object, validated_data: dict):
        """This is override update function of aircraft list serializer

        Args:
            instance (object): Aircraft model
            validated_data (dict): Aircraft list validated data

        Returns:
            object: List of aircraft
        """
        validated_data['user'] = self.context.get('user')
        validated_data['username'] = self.context.get('user').username
        return super().update(instance, validated_data)
