# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.chemin_modele import CheminModele  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModeleController(BaseTestCase):
    """ModeleController integration test stubs"""

    def test_add_modele(self):
        """Test case for add_modele

        Ajoute un nouveau Modele d'IA
        """
        body = CheminModele()
        response = self.client.open(
            '/api/v1/modele/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_modele(self):
        """Test case for del_modele

        Supprime un Modele de l'IA
        """
        query_string = [('modele_ia', 'modele_ia_example')]
        response = self.client.open(
            '/api/v1/modele/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_modele(self):
        """Test case for get_modele

        Donne les Modeles de l'IA
        """
        response = self.client.open(
            '/api/v1/modele/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
