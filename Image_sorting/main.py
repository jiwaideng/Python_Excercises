from data import data as example_data

def get_extension(file_name):
     return file_name[-4:]


def sort_pictures_dict(data):
    png_folder = []
    jpg_folder = []
    result = {}

    for key, items in data.items():
        result[key] = []

        for item in items:
            if isinstance(item, str):
                extension = get_extension(item)
                if extension == '.png':
                    png_folder.append(item)
                elif extension == '.jpg':
                    jpg_folder.append(item)
            else:
                for dict_key, dict_items in item.items():
                    result[key].append({dict_key: []})
                    for dict_item in dict_items:
                        extension = get_extension(dict_item)
                        if extension == '.png':
                            png_folder.append(dict_item)
                        elif extension == '.jpg':
                            jpg_folder.append(dict_item)

    result['Pictures'] = [
        {'png': png_folder},
        {'jpg': jpg_folder}
    ]

    return result






if __name__ == '__main__':
    sorted_data = sort_pictures_dict(example_data)
    print(sorted_data)