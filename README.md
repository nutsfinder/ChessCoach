
# Chess AI and Recognition System

This repository combines two exciting projects:  
1. **Chess AI**: A reinforcement learning-based chess engine inspired by AlphaGo Zero methods.  
2. **Chess Recognition**: A system to map chessboard images to structured formats like Forsyth–Edwards Notation (FEN).  

---

## Chess AI: AlphaGo Zero-Inspired Engine

### Background
This project leverages DeepMind's concepts to train a chess AI capable of mastering the game from scratch. Highlights include:  
- Inspired by **AlphaZero**, which mastered chess in 4 hours and outperformed Stockfish.  
- Uses reinforcement learning with supervised learning for initialization.  

### Features
- Self-play for generating training data.  
- Supervised learning for faster convergence.  
- Distributed training for scalable model development.  
- Outputs a Universal Chess Interface (UCI) compatible engine.  

### Installation
1. **Dependencies**:
   ```bash
   pip install -r requirements.txt
Run the workers:
Self-Play:
bash
Copier le code
python src/chess_zero/run.py self
Trainer:
bash
Copier le code
python src/chess_zero/run.py opt
Evaluator:
bash
Copier le code
python src/chess_zero/run.py eval
Refer to the AlphaGo Zero Implementation for additional details.

Chess Recognition: Image-to-FEN Mapping
Background
The Chess Recognition system converts chessboard images into structured FEN strings that can be used by chess engines. This involves:

Board Localization: Detecting the chessboard's corners and squares.
Occupancy Classification: Identifying empty/occupied squares.
Piece Classification: Recognizing specific pieces on the board.
FEN String Generation: Producing the FEN representation of the position.
Features
Trained on a synthetic dataset of ~5,000 chess images at varying angles and lighting.
Modular pipeline for image processing and FEN generation.
REST API integration for real-world applications.
Installation
Clone the repository:
bash
Copier le code
git clone https://github.com/YOUR_USERNAME/chess-ai-recognition.git
cd chess-ai-recognition
Install dependencies:
Using Poetry:
bash
Copier le code
poetry install
poetry shell
Using Pip:
bash
Copier le code
pip install .
Alternatively, use Docker:
bash
Copier le code
docker build -t chesscog -f cpu.Dockerfile .
docker run -it -p 8888:8888 -v $(pwd)/config:/config chesscog
Dataset & Models
Download and split the dataset:
bash
Copier le code
python -m chesscog.data_synthesis.download_dataset
python -m chesscog.data_synthesis.split_dataset
Download pretrained models:
bash
Copier le code
python -m chesscog.occupancy_classifier.download_model
python -m chesscog.piece_classifier.download_model
Inference
To analyze an image and generate the corresponding chess position:

bash
Copier le code
python -m chesscog.recognition.recognition path_to_image.png --white
Example output:

css
Copier le code
. K R . . R . .
P . P P Q . . P
. P B B . . . .
. . . . . P . .
. . b . . p . q
. p . . . . . .
p b p p . . . p
. k r . . . r .
You can view this position on Lichess for further analysis.

Fine-Tuning
The recognition model can be fine-tuned to work with custom chess sets using just two input images:

Create the dataset:
bash
Copier le code
python -m chesscog.transfer_learning.create_dataset
Train the model:
bash
Copier le code
python -m chesscog.transfer_learning.train_model
Combined Vision
By combining Chess AI and Chess Recognition, this repository provides a comprehensive toolkit for chess enthusiasts:

Quickly analyze real-world chess positions from images.
Train and deploy an advanced chess engine using self-play and reinforcement learning.
Command Line Usage
Chess AI Commands
Run Self-Play:
bash
Copier le code
python src/chess_zero/run.py self
Run Training:
bash
Copier le code
python src/chess_zero/run.py opt
Run Evaluation:
bash
Copier le code
python src/chess_zero/run.py eval
Chess Recognition Commands
Run Inference:
bash
Copier le code
python -m chesscog.recognition.recognition path_to_image.png --white
Fine-Tune Models:
bash
Copier le code
python -m chesscog.transfer_learning.train_model
Citation
If you use this repository, please cite the relevant work:

bibtex
Copier le code
@article{wolflein2021jimaging,
  author         = {W\"{o}lflein, Georg and Arandjelovi\'{c}, Ognjen},
  title          = {Determining Chess Game State from an Image},
  journal        = {Journal of Imaging},
  volume         = {7},
  year           = {2021},
  number         = {6},
  article-number = {94}
}
Contributing
We welcome contributions to both projects! Whether you want to improve the chess AI engine or enhance the recognition pipeline, feel free to:

Fork this repository.
