# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.img import Img  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInstallationController(BaseTestCase):
    """InstallationController integration test stubs"""

    def test_ajout_fichier_installation(self):
        """Test case for ajout_fichier_installation

        Ajoute un nouveau Modele d'IA
        """
        body = Img()
        query_string = [('plateforme', 'plateforme_example'),
                        ('fichiers', 'fichiers_example')]
        data = dict(base64='base64_example')
        response = self.client.open(
            '/api/v1/ia/fichier_installation/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ajout_fichier_lancement(self):
        """Test case for ajout_fichier_lancement

        Ajoute un fichier d'installation
        """
        body = Img()
        query_string = [('plateforme', 'plateforme_example'),
                        ('fichier', 'fichier_example')]
        data = dict(base64='base64_example')
        response = self.client.open(
            '/api/v1/ia/fichier_generation/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fichier_installation(self):
        """Test case for get_fichier_installation

        Retourne les fichiers d'installation d'une IA
        """
        query_string = [('plateforme', 'plateforme_example')]
        response = self.client.open(
            '/api/v1/ia/fichier_installation/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fichier_lancement(self):
        """Test case for get_fichier_lancement

        Retourne les fichiers de Generation
        """
        query_string = [('plateforme', 'plateforme_example')]
        response = self.client.open(
            '/api/v1/ia/fichier_generation/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='GET',
            query_string=query_string)
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
            '/api/v1/ia/fichier_generation/{nomIA}'.format(nom_ia='nom_ia_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
