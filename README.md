# Chess AI and Recognition System

This repository combines two powerful chess-related projects:  
1. **Chess AI**: A reinforcement learning-based chess engine inspired by AlphaGo Zero, pulled from [Zeta36/chess-alpha-zero](https://github.com/Zeta36/chess-alpha-zero).  
2. **Chess Recognition**: A system to map chessboard images to Forsyth–Edwards Notation (FEN), pulled from [georg-wolflein/chesscog](https://github.com/georg-wolflein/chesscog).

---

## Chess AI: AlphaGo Zero-Inspired Engine

### Background
This Chess AI project is based on [Zeta36/chess-alpha-zero](https://github.com/Zeta36/chess-alpha-zero). It trains a chess engine from scratch using reinforcement learning and self-play, mimicking the techniques used by DeepMind's AlphaZero. The key features include:  
- **Training through Self-Play**: Simulating games to learn optimal strategies.  
- **Supervised Learning**: Pretraining with human games for a head start.  
- **UCI Compatibility**: Enabling integration with chess GUIs.

### Features
- Advanced deep reinforcement learning for strategic improvement.  
- Distributed training for scalable computation.  
- Compatible with Universal Chess Interface (UCI) chess engines.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nutsfinder/ChessCoach
   cd chess-ai-recognition
