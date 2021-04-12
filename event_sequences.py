import os
import carla

# weather presets
# https://carla.readthedocs.io/en/0.9.3/python_api/#carlaweatherparameters

early_morning_clear = carla.WeatherParameters(
    cloudiness=10.0,
    precipitation=0.0,
    precipitation_deposits=0.0,
    sun_altitude_angle=-5.0
)

morning_clear = carla.WeatherParameters(
    cloudiness=10.0,
    precipitation=0.0,
    precipitation_deposits=0.0,
    sun_altitude_angle=5.0
)

morning_cloudy = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=0.0,
    precipitation_deposits=10.0,
    sun_altitude_angle=5.0
)


morning_light_rain = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=5.0,
    precipitation_deposits=25.0,
    sun_altitude_angle=5.0
)


morning_medium_rain = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=20.0,
    precipitation_deposits=50.0,
    sun_altitude_angle=5.0
)


morning_heavy_rain = carla.WeatherParameters(
    cloudiness=100.0,
    precipitation=100.0,
    precipitation_deposits=100.0,
    sun_altitude_angle=5.0
)


night_clear = carla.WeatherParameters(
    cloudiness=10.0,
    precipitation=0.0,
    precipitation_deposits=0.0,
    sun_altitude_angle=-90.0
)

night_cloudy = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=0.0,
    precipitation_deposits=10.0,
    sun_altitude_angle=-90.0
)


night_light_rain = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=5.0,
    precipitation_deposits=25.0,
    sun_altitude_angle=-90.0
)


night_medium_rain = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=20.0,
    precipitation_deposits=50.0,
    sun_altitude_angle=-90.0
)


night_heavy_rain = carla.WeatherParameters(
    cloudiness=100.0,
    precipitation=100.0,
    precipitation_deposits=100.0,
    sun_altitude_angle=-90.0
)


class main_sequence:
    def __init__(self):
        """
        self.seq = [
            ("w", night_cloudy),  # 0th event is to set to a morning heavy rain
            ("t", "python spawn_npc.py -n 50"),  # first event is to spawn more cars
            ("w", early_morning_clear),  # second event is to set to a rainy noon
            ("t", "python spawn_npc.py -n 20"),  # third event is to spawn fewer cars
            ("w", morning_clear),  # fourth event is to set to a cloudy noon
            ("w", morning_light_rain),  # fifth event is to set to a clear wet noon
            ("t", "python spawn_npc.py -n 50"),  # sixth event is to spawn more cars
            ("w", morning_heavy_rain),  # seventh event is to set to a clear sunset
        ]
        """
        """
        self.seq = [
            ("w", morning_light_rain),  # 0th event is to set to a morning light rain
            ("w", morning_clear),  # first event is to set to a clear morning
            ("t", "python spawn_npc.py -n 100"),  # second event is to spawn more cars
            ("w", morning_cloudy),  # third event is to set to a cloudy morning
            ("w", morning_medium_rain),  # fourth event is to set to a medium morning rain
            ("t", "python spawn_npc.py -n 50"),  # fifth event is to spawn more cars
            ("t", "python spawn_npc.py -n 20"),  # sixth event is to spawn more cars
            ("w", morning_heavy_rain),  # seventh event is to set to a heavy morning rain
        ]
        """
        """
        self.seq = [
            ("w", carla.WeatherParameters.ClearSunset),  # 0th event is to set to a morning heavy rain
            ("t", "python spawn_npc.py -n 50"),  # first event is to spawn more cars
            ("w", carla.WeatherParameters.CloudySunset),  # second event is to set to a rainy noon
            ("t", "python spawn_npc.py -n 20"),  # third event is to spawn fewer cars
            ("w", carla.WeatherParameters.MidRainSunset),  # fourth event is to set to a cloudy noon
            ("w", carla.WeatherParameters.SoftRainSunset),  # fifth event is to set to a clear wet noon
            ("t", "python spawn_npc.py -n 50"),  # sixth event is to spawn more cars
            ("w", carla.WeatherParameters.WetSunset),  # seventh event is to set to a clear sunset
        ]
        """
        """
        self.seq = [
            ("w", night_clear),  # first event is to set to a cloudy noon
            ("t", "python spawn_npc.py -n 100 --car-lights-on"),  # second event is to spawn more cars
            ("w", night_cloudy),  # first event is to set to a cloudy noon
            ("w", night_light_rain),  # third event is to set to a cloudy sunset
            ("w", night_medium_rain),  # third event is to set to a cloudy sunset
            ("w", morning_medium_rain),  # third event is to set to a cloudy sunset
            ("w", morning_heavy_rain),  # third event is to start raining
            ("w", morning_light_rain),  # third event is to start raining
        ]
        """
        """
        self.seq = [
            ("w", carla.WeatherParameters.ClearSunset),  # first event is to set to a cloudy noon
            ("t", "python spawn_npc.py -n 50"),  # second event is to spawn more cars
            ("w", night_clear),  # first event is to set to a cloudy noon
            ("w", morning_clear),  # third event is to set to a cloudy sunset
            ("w", morning_light_rain),  # third event is to set to a cloudy sunset
            ("w", carla.WeatherParameters.MidRainyNoon),  # third event is to set to a cloudy sunset
            ("w", carla.WeatherParameters.HardRainSunset),  # third event is to start raining
        ]
        """
        """
        self.seq = [
            ("w", morning_cloudy),  # first event is to set to a cloudy noon
            ("w", carla.WeatherParameters.CloudyNoon),  # first event is to set to a cloudy noon
            ("t", "python spawn_npc.py -n 50"),  # second event is to spawn more cars
            ("w", carla.WeatherParameters.CloudySunset),  # third event is to set to a cloudy sunset
            ("t", "python spawn_npc.py -n 100"),  # fourth event is to spawn more cars
            ("t", "python spawn_npc.py -n 50"),  # fifth event is to de-spawn some cars
            ("w", carla.WeatherParameters.MidRainSunset),  # third event is to start raining
        ]
        """

        self.seq = [
            ("w", morning_light_rain),  # 0th event is to set to a morning light rain
            ("w", morning_clear),  # first event is to set to a clear morning
            ("t", "python spawn_npc.py -n 100"),  # second event is to spawn more cars
            ("w", morning_cloudy),  # third event is to set to a cloudy morning
            ("w", morning_medium_rain),  # fourth event is to set to a medium morning rain
            ("t", "python spawn_npc.py -n 50"),  # fifth event is to spawn more cars
            ("t", "python spawn_npc.py -n 20"),  # sixth event is to spawn more cars
            ("w", morning_heavy_rain),  # seventh event is to set to a heavy morning rain
            ("w", morning_light_rain),  # 0th event is to set to a morning light rain
            ("w", morning_clear),  # first event is to set to a clear morning
            ("t", "python spawn_npc.py -n 100"),  # second event is to spawn more cars
            ("w", morning_cloudy),  # third event is to set to a cloudy morning
            ("w", morning_medium_rain),  # fourth event is to set to a medium morning rain
            ("t", "python spawn_npc.py -n 50"),  # fifth event is to spawn more cars
            ("t", "python spawn_npc.py -n 20"),  # sixth event is to spawn more cars
            ("w", morning_heavy_rain),  # seventh event is to set to a heavy morning rain
        ]

        """
        self.seq = [
            ("w", carla.WeatherParameters.ClearSunset),  # 0th event is to set to a morning heavy rain
            ("t", "python spawn_npc.py -n 50"),  # first event is to spawn more cars
            ("w", carla.WeatherParameters.CloudySunset),  # second event is to set to a rainy noon
            ("t", "python spawn_npc.py -n 20"),  # third event is to spawn fewer cars
            ("w", carla.WeatherParameters.MidRainSunset),  # fourth event is to set to a cloudy noon
            ("w", carla.WeatherParameters.SoftRainSunset),  # fifth event is to set to a clear wet noon
            ("t", "python spawn_npc.py -n 75"),  # sixth event is to spawn more cars
            ("w", carla.WeatherParameters.WetSunset),  # seventh event is to set to a clear sunset
        ]
        """
        """
        self.seq = [
            ("w", carla.WeatherParameters.ClearSunset),  # 0th event is to set to a morning heavy rain
            ("t", "python spawn_npc.py -n 50"),  # first event is to spawn more cars
            ("w", carla.WeatherParameters.CloudySunset),  # second event is to set to a rainy noon
            ("t", "python spawn_npc.py -n 20"),  # third event is to spawn fewer cars
            ("w", carla.WeatherParameters.MidRainSunset),  # fourth event is to set to a cloudy noon
            ("w", carla.WeatherParameters.SoftRainSunset),  # fifth event is to set to a clear wet noon
            ("t", "python spawn_npc.py -n 50"),  # sixth event is to spawn more cars
            ("w", carla.WeatherParameters.WetSunset),  # seventh event is to set to a clear sunset
        ]
        """
        """
        self.seq = [
            ("w", morning_heavy_rain),  # 0th event is to set to a morning heavy rain
            ("t", "python spawn_npc.py -n 50"),  # first event is to spawn more cars
            ("w", carla.WeatherParameters.HardRainNoon),  # second event is to set to a rainy noon
            ("t", "python spawn_npc.py -n 20"),  # third event is to spawn fewer cars
            ("w", carla.WeatherParameters.WetCloudyNoon),  # fourth event is to set to a cloudy noon
            ("w", carla.WeatherParameters.WetNoon),  # fifth event is to set to a clear wet noon
            ("t", "python spawn_npc.py -n 50"),  # sixth event is to spawn more cars
            ("w", carla.WeatherParameters.ClearSunset),  # seventh event is to set to a clear sunset
        ]
        """
        """
        self.seq = [
            ("w", morning_light_rain),  # 0th event is to set to a morning light rain
            ("w", morning_clear),  # first event is to set to a clear morning
            ("t", "python spawn_npc.py -n 100"),  # second event is to spawn more cars
            ("w", morning_cloudy),  # third event is to set to a cloudy morning
            ("w", morning_medium_rain),  # fourth event is to set to a medium morning rain
            ("t", "python spawn_npc.py -n 50"),  # fifth event is to spawn more cars
            ("t", "python spawn_npc.py -n 20"),  # sixth event is to spawn more cars
            ("w", morning_heavy_rain),  # seventh event is to set to a heavy morning rain
        ]
        """
        """
        self.seq = [
            ("w", carla.WeatherParameters.CloudyNoon),  # first event is to set to a cloudy noon
            ("t", "python spawn_npc.py -n 50"),  # second event is to spawn more cars
            ("w", carla.WeatherParameters.CloudySunset),  # third event is to set to a cloudy sunset
            ("t", "python spawn_npc.py -n 100"),  # fourth event is to spawn more cars
            ("t", "python spawn_npc.py -n 50"),  # fifth event is to de-spawn some cars
            ("w", carla.WeatherParameters.MidRainSunset),  # third event is to start raining
        ]
        """

    def __getitem__(self, item):
        return self.seq[item]

    def __len__(self):
        return len(self.seq)
