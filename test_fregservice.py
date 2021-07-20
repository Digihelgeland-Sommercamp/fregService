import json
import unittest
import fregservice as fs
import os

class TestFregservice(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.person_number_json = '03839199405.json'
        self.person = fs.Person(file_name=self.person_number_json)
    
    def test_read_file_name(self):
        with open(self.get_file_path(self.person_number_json)) as test_file:
            test_dict = json.load(test_file)
        
        target_dict = self.person._read_person_from_file(local_file_path="/FREG_manual/", file_name="03839199405.json", file_position_in_directory=None)

        self.assertDictEqual(target_dict, test_dict, "Wrong read of file through filename")

    def test_read_file_position(self):
        with open(self.get_file_path(self.person_number_json)) as test_file:
            test_dict = json.load(test_file)

        target_dict = self.person._read_person_from_file(local_file_path="/FREG_manual/", file_name=None, file_position_in_directory=0)

        self.assertDictEqual(target_dict, test_dict, "Wrong read of file through pos in directory")
        

    def test_id(self):
        test_data = {
            "foedselsEllerDNummer": "03839199405",
            "identifikatortype": "foedselsnummer"
        }
        self.assertDictEqual(self.person.identifikasjonsnummer, test_data, "Personid is not correct")

    
    def get_file_path(self, file):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir+"/FREG_manual/", file)
        return file_path
        

if __name__ == '__main__':
    unittest.main()