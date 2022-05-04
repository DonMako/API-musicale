import unittest
from unittest import TestCase
from APIMusicale.AudioDB.getIdArtist import getIdArtist


class TestPlaylist(TestCase):

    def testGetIdArtist(self):
        id_artiste = getIdArtist("Rammstein")
        self.assertEquals(id_artiste, "112121")


if __name__ == '__main__':
    unittest.main()
