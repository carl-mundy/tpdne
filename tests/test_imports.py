import unittest


class TestImportStructure(unittest.TestCase):

    def test_can_import_package(self):
        import tpdne
    
    def test_can_import_get_base64(self):
        from tpdne import tpdne_base64
    
    def test_can_import_get_bytes(self):
        from tpdne import tpdne_bytes


if __name__ == "__main__":
    unittest.main()
