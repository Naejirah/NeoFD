# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.input_ia import InputIA  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIAController(BaseTestCase):
    """IAController integration test stubs"""

    def test_add_ia(self):
        """Test case for add_ia

        Ajoute une nouvelle IA
        """
        body = InputIA()
        query_string = [('nom_ia', 'nom_ia_example'),
                        ('categorie', 'categorie_example'),
                        ('utilisable', false)]
        response = self.client.open(
            '/api/v1/ia',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ia(self):
        """Test case for get_ia

        Trouve une IA pour répondre à un besoin
        """
        query_string = [('categorie', 'txt2txt')]
        response = self.client.open(
            '/api/v1/ia/trouverParCategorie',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
