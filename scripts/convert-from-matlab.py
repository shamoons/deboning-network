import os
import h5py
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()

data_path = os.environ['DATA_PATH']
output_data_path = os.environ['OUTPUT_DATA_PATH']
patient_files = os.listdir(data_path)

patient_files = ['Patient_002_ALL.mat']

for patient_file in [patient_files[0]]:
    print(patient_file)
    patient_data = h5py.File(os.path.join(data_path, patient_file))
    variables = patient_data.items()

    for var in variables:
        name = var[0]
        data = var[1]
        print("Name ", name)  # Name
        if type(data) is h5py.Dataset:
            # If DataSet pull the associated Data
            # If not a dataset, you may need to access the element sub-items
            value = data.value
            # print("Value", value)  # NumPy Array / Value

            if name == 'Svar24':
                print(value.shape)
                for layer in range(value.shape[0]):
                    output_file = os.path.join(
                        output_data_path, 'output_' + str(layer) + '.png')
                    print(output_file)
                    plt.axis('off')
                    plt.imshow(value[layer], cmap='gray')
                    plt.savefig(output_file, bbox_inches='tight')

                # png.Writer.write(os.path.join(
                #     output_data_path, 'output.png'), value)
