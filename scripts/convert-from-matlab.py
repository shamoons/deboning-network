import os
import h5py
import asyncio
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()

data_path = os.environ['DATA_PATH']
output_data_path = os.environ['OUTPUT_DATA_PATH']
patient_files = os.listdir(data_path)


async def save_file(filename, image_data):
    plt.imshow(image_data, cmap='gray')
    await plt.savefig(filename, pad_inches=0, bbox_inches='tight')

for patient_file in patient_files:
    patient_parts = patient_file.split('.')
    patient_parts = patient_parts[0].split('_')
    patient_id = patient_parts[1]
    if int(patient_id) < 21:
        continue
    print('Doing patient', patient_id)

    patient_data = h5py.File(os.path.join(data_path, patient_file))
    variables = patient_data.items()

    for var in variables:
        name = var[0]
        data = var[1]
        # print("Name ", name)  # Name
        if type(data) is h5py.Dataset:
            # If DataSet pull the associated Data
            # If not a dataset, you may need to access the element sub-items
            value = data.value
            # print("Value", value)  # NumPy Array / Value
            plt.axis('off')
            if name == 'Svar25':
                for layer in range(value.shape[0]):
                    output_file = os.path.join(
                        output_data_path, patient_id + '_FLAIR_debone_' + str(layer) + '.png')
                    save_file(filename=output_file, image_data=value[layer])

            if name == 'Svar24':
                for layer in range(value.shape[0]):
                    output_file = os.path.join(
                        output_data_path, patient_id + '_FLAIR_bone_' + str(layer) + '.png')
                    save_file(filename=output_file, image_data=value[layer])
