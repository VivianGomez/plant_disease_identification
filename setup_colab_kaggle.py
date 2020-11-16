import setup_colab as setup_general
import os
from google.colab import files
from IPython.display import clear_output

def setup_kaggle_token(filename: str):
    assert filename.endswith(".json"), "El archivo no es JSON"
    files.upload()
    clear_output(wait=True)
    os.system("mkdir ~/.kaggle")
    os.system(f"cp {filename} ~/.kaggle/")
    os.system(f"chmod 600 ~/.kaggle/{filename}")

def setup_gen():
    setup_general.setup_general()
    print("Workshop Enabled Successfully")

def setup_plant_disease(filename: str="kaggle.json", 
                    download_dataset=True, kaggle_version="1.5.6"):
    setup_general.setup_general()
    setup_kaggle_token(filename)
    os.system(f"pip install -q kaggle=={kaggle_version}")
    if download_dataset:
        os.system("kaggle datasets download -d abdallahalidev/plantvillage-dataset")
        from utils import general as gen
        gen.extract_file("plantvillage-dataset.zip", "data")
        print("Dataset Downloaded Successfully")
    print("Proyect Enabled Successfully")