# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Output(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, output: str=None):  # noqa: E501
        """Output - a model defined in Swagger

        :param output: The output of this Output.  # noqa: E501
        :type output: str
        """
        self.swagger_types = {
            'output': str
        }

        self.attribute_map = {
            'output': 'output'
        }
        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'Output':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Output of this Output.  # noqa: E501
        :rtype: Output
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self) -> str:
        """Gets the output of this Output.


        :return: The output of this Output.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output: str):
        """Sets the output of this Output.


        :param output: The output of this Output.
        :type output: str
        """

        self._output = output