# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.output import Output  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCategorieController(BaseTestCase):
    """CategorieController integration test stubs"""

    def test_add_categorie(self):
        """Test case for add_categorie

        Ajoute une nouvelle catégorie pour les IA
        """
        response = self.client.open(
            '/api/v1/categorie/{nomCategorie}'.format(nom_categorie='nom_categorie_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_categorie(self):
        """Test case for get_categorie

        Donne les catégories existantes
        """
        response = self.client.open(
            '/api/v1/categorie',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
