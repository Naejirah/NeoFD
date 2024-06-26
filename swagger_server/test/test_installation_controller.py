# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.input_fichier_generation import InputFichierGeneration  # noqa: E501
from swagger_server.models.input_fichier_installation import InputFichierInstallation  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInstallationController(BaseTestCase):
    """InstallationController integration test stubs"""

    def test_add_fichier_installation(self):
        """Test case for add_fichier_installation

        Ajoute un nouveau Modele d'IA
        """
        body = InputFichierInstallation()
        query_string = [('plateforme', 'plateforme_example')]
        response = self.client.open(
            '/api/v1/ia/fichier_installation/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ajout_fichier_lancement(self):
        """Test case for ajout_fichier_lancement

        Ajoute un fichier de generation
        """
        body = InputFichierGeneration()
        response = self.client.open(
            '/api/v1/ia/fichier_generation/{nomCategorie}/{nomIA}'.format(nom_categorie='nom_categorie_example', nom_ia='nom_ia_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fichier_generation(self):
        """Test case for get_fichier_generation

        Retourne les fichiers de Generation
        """
        response = self.client.open(
            '/api/v1/ia/fichier_generation/{nomCategorie}/{nomIA}'.format(nom_categorie='nom_categorie_example', nom_ia='nom_ia_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fichier_installation(self):
        """Test case for get_fichier_installation

        Retourne les fichiers d'installation d'une IA
        """
        response = self.client.open(
            '/api/v1/ia/fichier_installation/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_lancement_fichier_installation(self):
        """Test case for lancement_fichier_installation

        Lancement d'une installation d'une IA
        """
        response = self.client.open(
            '/api/v1/ia/fichier_installation/{nomIA}/{plateforme}'.format(nom_ia='nom_ia_example', plateforme='plateforme_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suppr_fichier_installation(self):
        """Test case for suppr_fichier_installation

        Supprime un fichier d'installation
        """
        response = self.client.open(
            '/api/v1/ia/fichier_installation/{nomIA}/{plateforme}'.format(nom_ia='nom_ia_example', plateforme='plateforme_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suppr_fichier_lancement(self):
        """Test case for suppr_fichier_lancement

        Supprime un fichier de Generation
        """
        response = self.client.open(
            '/api/v1/ia/fichier_generation/{nomCategorie}/{nomIA}'.format(nom_categorie='nom_categorie_example', nom_ia='nom_ia_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
