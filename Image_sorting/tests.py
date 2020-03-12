from unittest import TestCase, main
from main import *
from data import data as example_data

class TestImageSorting(TestCase):

    def test_extension(self):
        examples = [
            'filename.png',
            'filename.jpg',
            'file.exe',
            'something.gif']
        
        results = [get_extension(filename) for filename in examples]

        self.assertEquals('.png', results[0])
        self.assertEquals('.jpg', results[1])
        self.assertEquals('.exe', results[2])
        self.assertEquals('.gif', results[3])

    def test_sorting(self):
        result = sort_pictures_dict(example_data)
        expected_result = {
            'Documents': [
                {
                    'New Folder': []
                }
            ],
            'Pictures': [
                {
                    'png': [
                        'picture1.png',
                        'picture2.png',
                        'picture4.png',
                        'picture10.png',
                    ]
                },
                {
                    'jpg': [
                        'picture3.jpg',
                        'picturenoname.jpg'
                    ]
                }
            ]
        }
        self.assertEquals(expected_result, result)


if __name__ == '__main__':
    main()