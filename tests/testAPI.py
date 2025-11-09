import unittest
from unittest import TestCase
from APIMusicale.AudioDB import AudioDB


class TestAPI(TestCase):

    def testGetIdArtist(self):
        id_artiste = AudioDB.getIdArtist("Rammstein")
        self.assertEquals(id_artiste, "112121")


if __name__ == '__main__':
    unittest.main()
