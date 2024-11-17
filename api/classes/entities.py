"""SpaceX Entity Models

This module contains objects used to translate the JSON returned from 
the SpaceX-API into Pythonic dataclass entities. 
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Core:
    core: Optional[str] = None
    flight: Optional[int] = None
    gridfins: Optional[bool] = None
    legs: Optional[bool] = None
    reused: Optional[bool] = None
    landing_attempt: Optional[bool] = None
    landing_success: Optional[bool] = None
    landing_type: Optional[str] = None
    landpad: Optional[str] = None


@dataclass
class Failure:
    time: Optional[int] = None
    altitude: Optional[int] = None
    reason: Optional[str] = None


@dataclass
class Fairings:
    reused: Optional[bool] = None
    recovery_attempt: Optional[bool] = None
    recovered: Optional[bool] = None
    ships: Optional[list[str]] = None


@dataclass
class Flickr:
    small: Optional[list[str]] = None
    original: Optional[list[str]] = None


@dataclass
class Patch:
    small: Optional[str] = None
    large: Optional[str] = None


@dataclass
class Reddit:
    campaign: Optional[str] = None
    launch: Optional[str] = None
    media: Optional[str] = None
    recovery: Optional[str] = None


@dataclass
class Links:
    patch: Optional[Patch] = None
    reddit: Optional[Reddit] = None
    flickr: Optional[Flickr] = None
    presskit: Optional[str] = None
    webcast: Optional[str] = None
    youtube_id: Optional[str] = None
    article: Optional[str] = None
    wikipedia: Optional[str] = None


@dataclass
class Launch:
    id: str
    name: str = None
    date_utc: datetime = None
    launchpad: str = None
    fairings: Optional[Fairings] = None
    links: Optional[Links] = None
    static_fire_date_utc: Optional[datetime] = None
    static_fire_date_unix: Optional[int] = None
    net: Optional[bool] = None
    window: Optional[int] = None
    rocket: Optional[str] = None
    success: Optional[bool] = None
    failures: Optional[list[Failure]] = None
    details: Optional[str] = None
    crew: Optional[list[str]] = None
    ships: Optional[list[str]] = None
    capsules: Optional[list[str]] = None
    payloads: Optional[list[str]] = None
    flight_number: Optional[int] = None
    date_unix: Optional[int] = None
    date_local: Optional[datetime] = None
    date_precision: Optional[str] = None
    upcoming: Optional[bool] = None
    cores: Optional[list[Core]] = None
    auto_update: Optional[bool] = None
    tbd: Optional[bool] = None
    launch_library_id: Optional[str] = None


@dataclass
class Images:
    large: Optional[list[str]] = None


@dataclass
class Launchpad:
    id: Optional[str]
    name: Optional[str] = None
    full_name: Optional[str] = None
    locality: Optional[str] = None
    launches: Optional[list[str]] = None
    status: Optional[str] = None
    images: Optional[list[Images]] = None
    details: Optional[str] = None
    region: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    launch_attempts: Optional[int] = None
    launch_successes: Optional[int] = None
    rockets: Optional[list[str]] = None
    timezone: Optional[str] = None
