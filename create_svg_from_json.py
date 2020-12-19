import os, json, csv

json_folder_name = 'json_file'
json_file_name = 'table.json'

csv_file_name = 'table.csv'
csv_folder_name = 'csv'

root_Path = os.path.dirname(__file__)

json_directory_path = os.path.join(root_Path, json_folder_name)
json_file_path = os.path.join(json_directory_path, json_file_name)
csv_directory_path = os.path.join(root_Path, csv_folder_name)
csv_file_path = os.path.join(csv_directory_path, csv_file_name)

if not os.path.exists(csv_directory_path):
    os.makedirs(csv_directory_path)

json_file = open(json_file_path)
json_file_content = json_file.read()
json_file.close()

json_object = json.loads(json_file_content)

selected_color = json_object["002"]


with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,
                        delimiter=';',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)

    header = ['intensity']
    # write header
    for i in range(0, len(list(json_object.keys()))):
        current_color_key = list(json_object.keys())[i]
        header.append(current_color_key)
    writer.writerow(header)

    # write rest
    amount_of_intensities = len(json_object["002"]) # we use the ones of "002" because they're the same everywhere
    for i in range(1, amount_of_intensities): # we start at 1, because we want to skip e.g. ['nm', '002'] for each element

        current_intensity = [json_object["002"][i][0]]
        row = current_intensity

        for j in range(0, len(list(json_object.keys()))):
            current_color_key = list(json_object.keys())[j]
            try:
                current_wavelength = json_object[current_color_key][i][1]
            except:
                current_wavelength = 0

            row.append(current_wavelength)
        
        writer.writerow(row)
