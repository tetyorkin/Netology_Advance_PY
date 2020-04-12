import json
import os
import unittest
from unittest.mock import patch

import app

documents = []
directories = {}


def setUpModule():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    path_directories = os.path.join(current_path, '../fixtures/directories.json')
    path_documents = os.path.join(current_path, '../fixtures/documents.json')
    with open(path_directories, 'r', encoding='utf-8') as dir:
        directories.update(json.load(dir))
    with open(path_documents, 'r', encoding='utf-8') as doc:
        documents.extend(json.load(doc))


@patch('app.directories', directories, create=True)
@patch('app.documents', documents, create=True)
class TestSecretaryProgram(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertTrue(app.check_document_existance(documents[1]['number']))
        with patch('app.input', return_value=documents[1]['number']):
            self.assertEqual(app.get_doc_owner_name(), documents[1]['name'])

    def test_get_all_doc_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)
        self.assertGreater(len(app.get_all_doc_owners_names()), 0)

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf(documents[0]['number'])
        self.assertNotIn(documents[0]['number'], directories['1'])

    def test_add_new_shelf(self):
        with patch('app.input', return_value='4'):
            self.assertIn(app.add_new_shelf()[0], directories.keys())
            # print(directories.keys())

    @patch('app.input')
    def test_move_doc_to_shelf(self, mock_input):
        mock_input.side_effect = [documents[2]['number'], '2']
        app.move_doc_to_shelf()
        self.assertIn(documents[2]['number'], directories['2'])

    def test_get_doc_shelf(self):
        doc_number = documents[0]['number']
        with patch('app.input', return_value=doc_number):
            self.assertEqual(app.get_doc_shelf(), '1')


if __name__ == '__main__':
    unittest.main()
