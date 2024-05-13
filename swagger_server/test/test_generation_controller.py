# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.img import Img  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGenerationController(BaseTestCase):
    """GenerationController integration test stubs"""

    def test_generation_par_ia(self):
        """Test case for generation_par_ia

        Génère du texte à partir de texte
        """
        query_string = [('nom_fichier_parametre', 'nom_fichier_parametre_example')]
        response = self.client.open(
            '/api/v1/ia/generation/{nomCategorie}/{nomIA}/{modeleIA}'.format(nom_categorie='nom_categorie_example', nom_ia='nom_ia_example', modele_ia='modele_ia_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_resultat(self):
        """Test case for get_resultat

        Accède aux résultats d'une IA
        """
        query_string = [('nom_ia', 'nom_ia_example')]
        response = self.client.open(
            '/api/v1/ia/resultat/{nomCategorie}'.format(nom_categorie='nom_categorie_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
