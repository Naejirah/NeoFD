# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.output import Output  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIAController(BaseTestCase):
    """IAController integration test stubs"""

    def test_add_output(self):
        """Test case for add_output

        Ajoute une nouvelle IA
        """
        body = Output()
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

    def test_find_outputs_by_status(self):
        """Test case for find_outputs_by_status

        Trouve une IA pour répondre à un besoin
        """
        query_string = [('categorie', 'txt2Output;Output2Output')]
        response = self.client.open(
            '/api/v1/ia/trouverParCategorie',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
