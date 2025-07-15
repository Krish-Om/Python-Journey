# Time-Based Q-Learning Snake Trainer

## 🚀 Quick Start

### 1. Train the Agent (5 minutes)
```bash
cd learning_agent
python quick_train_5min.py
```

### 2. Watch the Trained Agent Play
```bash
python play_autonomous.py
```

## 📊 Training Performance

**Expected Results for 5-minute training:**
- **Episodes**: ~33,000 episodes
- **Training Speed**: ~6,600 episodes/minute
- **Learning**: Agent learns 1,800+ state-action pairs
- **Performance**: Achieves scores of 15-30+ points consistently

## 🎮 Game Controls

When watching the autonomous game:
- **ESC**: Quit the game
- **SPACE**: Toggle auto-restart (ON by default)
- **ENTER**: Manual restart (when auto-restart is OFF)

## 📁 Files

### Training Scripts
- `quick_train_5min.py` - Fast 5-minute training session
- `time_based_trainer.py` - Flexible time-based trainer with options
- `play_autonomous.py` - Launch autonomous gameplay

### Core Learning System
- `learning_model.py` - Q-learning implementation
- `q_table.json` - Saved learned strategies
- `training_stats.json` - Training progress and statistics

### Main Game
- `../source.py` - Snake game with autonomous Q-learning agent

## 🔧 Advanced Usage

### Custom Training Duration
```bash
python time_based_trainer.py 10  # Train for 10 minutes
```

### Interactive Training Menu
```bash
python time_based_trainer.py
```

### Estimate Training Capacity
The trainer can predict how many episodes will fit in your time budget:
- 1 minute ≈ 6,600 episodes
- 5 minutes ≈ 33,000 episodes  
- 10 minutes ≈ 66,000 episodes

## 🧠 How It Works

1. **State Representation**: Game state simplified to key features (apple direction, dangers, distance)
2. **Q-Learning**: Agent learns optimal actions for each state through trial and error
3. **Epsilon-Greedy**: Balances exploration (30%) vs exploitation (70%)
4. **Continuous Learning**: Agent continues learning even during gameplay
5. **Persistence**: All learning saved automatically to JSON files

## 📈 Performance Monitoring

The system provides real-time feedback:
- Episodes completed per minute
- Current best score
- Recent average performance
- Q-table size (learned patterns)
- Training time elapsed

## 🎯 Expected Agent Behavior

After 5-minute training, the agent should:
- Navigate efficiently toward apples
- Avoid walls and self-collision
- Score 15-30+ points consistently
- Make ~330 intelligent decisions per game
- Show clear improvement over random play

## 🚀 Next Steps

- **Longer Training**: Try 10+ minute sessions for even better performance
- **Watch Learning**: Observe how strategies improve during gameplay
- **Compare Agents**: Test different agent types in the main directory
- **Academic Use**: Perfect for AI/ML coursework demonstrations
