# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InputFichierInstallation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, install_chemin_absolu: str=None):  # noqa: E501
        """InputFichierInstallation - a model defined in Swagger

        :param install_chemin_absolu: The install_chemin_absolu of this InputFichierInstallation.  # noqa: E501
        :type install_chemin_absolu: str
        """
        self.swagger_types = {
            'install_chemin_absolu': str
        }

        self.attribute_map = {
            'install_chemin_absolu': 'install_chemin_absolu'
        }
        self._install_chemin_absolu = install_chemin_absolu

    @classmethod
    def from_dict(cls, dikt) -> 'InputFichierInstallation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InputFichierInstallation of this InputFichierInstallation.  # noqa: E501
        :rtype: InputFichierInstallation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def install_chemin_absolu(self) -> str:
        """Gets the install_chemin_absolu of this InputFichierInstallation.


        :return: The install_chemin_absolu of this InputFichierInstallation.
        :rtype: str
        """
        return self._install_chemin_absolu

    @install_chemin_absolu.setter
    def install_chemin_absolu(self, install_chemin_absolu: str):
        """Sets the install_chemin_absolu of this InputFichierInstallation.


        :param install_chemin_absolu: The install_chemin_absolu of this InputFichierInstallation.
        :type install_chemin_absolu: str
        """

        self._install_chemin_absolu = install_chemin_absolu
