import numpy as np
import astropy
import json
import requests
import query_eaot



class Exoplanet():
    """Exoplanet class, defines the properites of an exoplanet and some properties of its host star.
    """
    def __init__(self):
        self.planet_radius
        self.planet_mass
        self.planet_gravity
        self.orbital_period
        self.star_distance
        self.planet_distance
        self.constellation

    def random_query_mast_database():
        """ Random query a planet from the MAST database.
        """
