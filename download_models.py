import gdown
import zipfile
import os

# Shared Drive link (make sure it's a ZIP file of all models)
url = "https://drive.google.com/uc?id=10V2iwfWBXNjDdw9LZmgQvy_KsAGwUnW6"
output_zip = "models.zip"

# Download the zip
gdown.download(url, output_zip, quiet=False)

# Unzip into NLPProjectModels folder
if not os.path.exists("NLPProjectModels"):
    os.makedirs("NLPProjectModels")

with zipfile.ZipFile(output_zip, 'r') as zip_ref:
    zip_ref.extractall("NLPProjectModels")

# Clean up
os.remove(output_zip)
