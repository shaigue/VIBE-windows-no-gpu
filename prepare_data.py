"""
mkdir -p data
cd data
gdown https://drive.google.com/uc?id=1untXhYOLQtpNEy4GTY_0fL_H-k6cTf_r
unzip vibe_data.zip
rm vibe_data.zip
cd ..
mv data/vibe_data/sample_video.mp4 .
mkdir -p $HOME/.torch/models/
mv data/vibe_data/yolov3.weights $HOME/.torch/models/

"""
import os
import shutil
import zipfile
from pathlib import Path
import gdown

# create the data directory
data_dir = Path('data')
os.makedirs(data_dir, exist_ok=True)

# download the trained model from google drive
print('downloading data...')
url = 'https://drive.google.com/uc?id=1untXhYOLQtpNEy4GTY_0fL_H-k6cTf_r'
zip_path = data_dir / 'vibe_data.zip'
gdown.download(url, str(zip_path))

# extract the zip file and delete it
print(f'zip file to extract: {str(zip_path)}')
with zipfile.ZipFile(zip_path) as zf:
    zf.extractall(data_dir)

os.remove(zip_path)

# move the sample video to the projects main directory
print("moving sample video...")
sample_video_path = data_dir / 'vibe_data' / 'sample_video.mp4'
shutil.move(str(sample_video_path), '.')

# move yolov3 weights to the torch directory
print('moving the model weights...')
torch_models_dir = Path.home() / '.torch' / 'models'
os.makedirs(torch_models_dir, exist_ok=True)
yolov3_weights_path = data_dir / 'vibe_data' / 'yolov3.weights'
shutil.move(str(yolov3_weights_path), str(torch_models_dir))
