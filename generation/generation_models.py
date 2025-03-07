from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional


class Theme(str, Enum):
    ADVENTURE = "Adventure"
    CULTURE = "Culture"
    FOOD_DRINK = "Food and drink"
    NATURE = "Nature"
    RELAXATION = "Relaxation"
    ENTERTAINMENT = "Entertainment"
    SHOPPING = "Shopping"
    SPORTS = "Sports"
    FAMILY = "Family"
    UNIQUE = "Unique"
    NIGHTLIFE = "Nightlife"


class TransportMode(str, Enum):
    TUBE = "Tube"
    WALKING = "Walking"
    BUS = "Bus"
    TAXI = "Taxi"
    TRAIN = "Train"
    FERRY = "Ferry"
    DEFAULT = "N/A"


class Activity(BaseModel):
    """An activity that could be part of an itinerary"""

    id: int = Field(
        description="Unique identifier for the activity. If one is provided you must keep the original ID"
    )
    title: str = Field(description="Brief title of the activity, max a few words.")
    description: str = Field(
        description="Brief description of the activity - maximum two sentences. It should just tell me what the activity is - it should not try and fit it into an itinerary timeline."
    )
    image_link: List[str] = Field(
        description="URLs of images representing the activity. Do not generate."
    )
    price: float = Field(
        description="Cost of the itinerary item, in GBP. If free, write 0."
    )
    theme: Theme = Field(description="Theme of the activity.")


class ActivityTitleStruct(BaseModel):
    """Activity title and id"""

    title: str = Field(description="Brief title of the activity, max a few words")
    id: int = Field(description="Unique id for the activity")


class ActivityTitles(BaseModel):
    """Generates only titles of activities that could be part of an itinerary"""

    activities: List[ActivityTitleStruct] = Field(
        description="List of titles of activities that could make for exciting activities in the given location"
    )


class ItineraryItem(BaseModel):
    """An entry for an itinerary item"""

    title: str = Field(description="Brief title of the itinerary item.")
    transport: bool = Field(
        description="Only TRUE if the itinerary item is not an actual activity of any kind but is just transport from one location to another."
    )
    start: str = Field(description="Start time of the itinerary item.")
    end: str = Field(description="End time of the itinerary item.")
    description: str = Field(
        description="Brief description of the activity - maximum two sentences."
    )
    price: float = Field(
        description="Cost of the itinerary item, in GBP. If free, write 0."
    )
    theme: Theme = Field(description="Theme of the itinerary item.")
    transportMode: str = Field(
        description="Mode of transport if it is a transport step. Only required if it is transport. MUST Be one of the following: Tube, Walking, Bus, Taxi, Train, Ferry, N/A"
    )
    requires_booking: bool = Field(
        description="Indicates if the item requires booking."
    )
    booking_url: Optional[str] = Field(
        description="URL for booking the itinerary item."
    )
    weather: Optional[str] = Field(
        description="weather conditions for the given activity. Generate ONLY if you are given conditions in context that match with the time of this activity. Must be either blank, or exactly match one of the following categories: sunny, cloudy with sun, cloudy, rainy, snowy"
    )
    temperature: Optional[int] = Field(
        description="temperature in celsius for the given activity. Generate ONLY if you are given conditions in context that match with the time of this activity. Must be either blank, or or match the number that was given in context for the given start time."
    )
    image_link: List[str] = Field(
        description="URLs of images representing the activity. Do not generate."
    )
    duration: int = Field(description="Duration of the itinerary item in minutes.")
    id: int = Field(description="Unique identifier for the itinerary item.")
    latitude: Optional[float] = Field(
        description="Latitude position of the given activity."
    )
    longitude: Optional[float] = Field(
        description="Longitude position of the given activity."
    )


class FullItinerary(BaseModel):
    itinerary: list[ItineraryItem] = Field(
        description="A full day itinerary for the given location"
    )


class SimpleItineraryItem(BaseModel):
    """An entry for a simplified itinerary item"""

    title: str = Field(description="Brief title of the itinerary item.")
    imageTag: str = Field(
        description="A search term to find a relevant image tag for the given activity or location."
    )
    start: str = Field(description="Start time of the itinerary item.")
    end: str = Field(description="End time of the itinerary item.")
    id: int = Field(description="Unique identifier for the itinerary item.")


class ActivityList(BaseModel):
    activities: list[Activity] = Field(description="List of activities.")


class ItinerarySummary(BaseModel):
    itinerary: list[SimpleItineraryItem] = Field(
        description="A full day itinerary for the given location"
    )


class Facts(BaseModel):
    facts: list[str] = Field(
        description="A list of interesting facts about the given location."
    )
