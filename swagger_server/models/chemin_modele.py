# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CheminModele(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, chemin: str=None):  # noqa: E501
        """CheminModele - a model defined in Swagger

        :param chemin: The chemin of this CheminModele.  # noqa: E501
        :type chemin: str
        """
        self.swagger_types = {
            'chemin': str
        }

        self.attribute_map = {
            'chemin': 'chemin'
        }
        self._chemin = chemin

    @classmethod
    def from_dict(cls, dikt) -> 'CheminModele':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Chemin_modele of this CheminModele.  # noqa: E501
        :rtype: CheminModele
        """
        return util.deserialize_model(dikt, cls)

    @property
    def chemin(self) -> str:
        """Gets the chemin of this CheminModele.


        :return: The chemin of this CheminModele.
        :rtype: str
        """
        return self._chemin

    @chemin.setter
    def chemin(self, chemin: str):
        """Sets the chemin of this CheminModele.


        :param chemin: The chemin of this CheminModele.
        :type chemin: str
        """

        self._chemin = chemin
