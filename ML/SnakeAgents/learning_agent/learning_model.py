import random
import json
import os
import time
from collections import defaultdict

# Q-Learning parameters
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.95
EPSILON = 0.3  # Exploration rate - increased for more exploration and faster episodes
SIZE = 40  # Grid size from the game

# File to save/load Q-table and training stats
Q_TABLE_FILE = os.path.join(os.path.dirname(__file__), "q_table.json")
TRAINING_STATS_FILE = os.path.join(os.path.dirname(__file__), "training_stats.json")

# Global Q-table - we'll use a simple dictionary
q_table = defaultdict(lambda: defaultdict(float))

# Training Statistics
training_stats = {
    "total_episodes": 0,  # Number of complete games played
    "total_steps": 0,  # Total actions taken across all episodes
    "scores_history": [],  # List of scores for each episode
    "episode_lengths": [],  # Number of steps per episode
    "exploration_count": 0,  # Number of exploration actions
    "exploitation_count": 0,  # Number of exploitation actions
    "q_table_size": 0,  # Number of state-action pairs in Q-table
    "learning_start_time": None,  # When training started
    "last_100_avg_score": 0.0,  # Average score of last 100 episodes
    "best_score": 0,  # Best score achieved
    "current_episode_steps": 0,  # Steps in current episode
    "current_episode_score": 0,  # Score in current episode
}


def load_q_table():
    """Load Q-table from file if it exists"""
    global q_table
    if os.path.exists(Q_TABLE_FILE):
        try:
            print("🔄 Loading Q-table...")
            with open(Q_TABLE_FILE, "r") as f:
                loaded_data = json.load(f)
                q_table = defaultdict(lambda: defaultdict(float))
                for state_str, actions in loaded_data.items():
                    # Convert string representation back to tuple if it looks like a tuple
                    if state_str.startswith("(") and state_str.endswith(")"):
                        try:
                            # Safely evaluate tuple string
                            state = eval(state_str)
                        except:
                            state = state_str  # Fallback to string if eval fails
                    else:
                        state = state_str
                    q_table[state] = defaultdict(float, actions)
            print(f"✅ Q-table loaded with {len(q_table)} entries!")
        except Exception as e:
            print(f"❌ Error loading Q-table: {e}")
            q_table = defaultdict(lambda: defaultdict(float))
    else:
        print("📁 No existing Q-table found, starting fresh")
        q_table = defaultdict(lambda: defaultdict(float))


def save_q_table():
    """Save Q-table to file"""
    try:
        # Convert defaultdict to regular dict for JSON serialization
        # Convert tuple keys to strings since JSON doesn't support tuple keys
        regular_dict = {}
        for state, actions in q_table.items():
            # Convert tuple state to string representation
            state_str = str(state) if isinstance(state, tuple) else state
            regular_dict[state_str] = dict(actions)

        print(f"🔄 Saving Q-table with {len(regular_dict)} states...")
        with open(Q_TABLE_FILE, "w") as f:
            json.dump(regular_dict, f)
        print("✅ Q-table saved successfully!")
    except Exception as e:
        print(f"❌ Error saving Q-table: {e}")


def load_training_stats():
    """Load training statistics from file if it exists"""
    global training_stats
    if os.path.exists(TRAINING_STATS_FILE):
        try:
            with open(TRAINING_STATS_FILE, "r") as f:
                loaded_stats = json.load(f)
                training_stats.update(loaded_stats)
            print(
                f"Training stats loaded! Episodes: {training_stats['total_episodes']}, Best Score: {training_stats['best_score']}"
            )
        except:
            print("Error loading training stats, starting fresh")

    # Set start time if not already set
    if training_stats["learning_start_time"] is None:
        training_stats["learning_start_time"] = time.time()


def save_training_stats():
    """Save training statistics to file"""
    try:
        print(
            f"🔄 Saving training stats (Episode {training_stats['total_episodes']})..."
        )
        with open(TRAINING_STATS_FILE, "w") as f:
            json.dump(training_stats, f, indent=2)
        print("✅ Training stats saved successfully!")
    except Exception as e:
        print(f"❌ Error saving training stats: {e}")


def update_q_table_size():
    """Update the Q-table size statistic"""
    training_stats["q_table_size"] = sum(len(actions) for actions in q_table.values())


def calculate_avg_last_100():
    """Calculate average score of last 100 episodes"""
    if len(training_stats["scores_history"]) >= 100:
        training_stats["last_100_avg_score"] = (
            sum(training_stats["scores_history"][-100:]) / 100
        )
    elif len(training_stats["scores_history"]) > 0:
        training_stats["last_100_avg_score"] = sum(
            training_stats["scores_history"]
        ) / len(training_stats["scores_history"])


def print_training_progress():
    """Print current training progress"""
    episodes = training_stats["total_episodes"]
    if episodes > 0 and episodes % 10 == 0:  # Print every 10 episodes
        avg_score = training_stats["last_100_avg_score"]
        best_score = training_stats["best_score"]
        q_size = training_stats["q_table_size"]
        exploration_rate = (
            training_stats["exploration_count"]
            / max(1, training_stats["total_steps"])
            * 100
        )

        print(f"\n=== Training Progress ===")
        print(f"Episodes: {episodes}")
        print(f"Total Steps: {training_stats['total_steps']}")
        print(f"Best Score: {best_score}")
        print(f"Avg Score (last 100): {avg_score:.2f}")
        print(f"Q-table Size: {q_size} state-action pairs")
        print(f"Exploration Rate: {exploration_rate:.1f}%")

        if training_stats["learning_start_time"]:
            training_time = (time.time() - training_stats["learning_start_time"]) / 60
            print(f"Training Time: {training_time:.1f} minutes")
        print("========================\n")


def get_simple_state(game):
    """
    Create a simplified state representation compatible with fast trainer.
    Uses the same format as fast_trainer.py for Q-table compatibility.
    """
    head_x, head_y = game.snake.x[0], game.snake.y[0]
    apple_x, apple_y = game.apple.x, game.apple.y

    # Convert pixel coordinates to grid coordinates (same as fast trainer)
    head_grid_x = head_x // SIZE
    head_grid_y = head_y // SIZE
    apple_grid_x = apple_x // SIZE
    apple_grid_y = apple_y // SIZE

    # Direction to apple (same as fast trainer)
    apple_dx = (
        0 if apple_grid_x == head_grid_x else (1 if apple_grid_x > head_grid_x else -1)
    )
    apple_dy = (
        0 if apple_grid_y == head_grid_y else (1 if apple_grid_y > head_grid_y else -1)
    )

    # Danger detection (wall and self-collision) - same as fast trainer
    danger_left = game._is_potential_move_colliding(head_x - SIZE, head_y)
    danger_right = game._is_potential_move_colliding(head_x + SIZE, head_y)
    danger_up = game._is_potential_move_colliding(head_x, head_y - SIZE)
    danger_down = game._is_potential_move_colliding(head_x, head_y + SIZE)

    # Current direction (same as fast trainer)
    dir_left = game.snake.direction == "left"
    dir_right = game.snake.direction == "right"
    dir_up = game.snake.direction == "up"
    dir_down = game.snake.direction == "down"

    # Distance to apple (normalized, same as fast trainer)
    distance = abs(head_grid_x - apple_grid_x) + abs(head_grid_y - apple_grid_y)
    distance_normalized = min(distance / 10.0, 1.0)

    state = (
        apple_dx,
        apple_dy,  # Apple direction
        danger_left,
        danger_right,
        danger_up,
        danger_down,  # Danger detection
        dir_left,
        dir_right,
        dir_up,
        dir_down,  # Current direction
        distance_normalized,  # Distance to apple
    )

    return state


def get_reward(game, old_score, new_score, collision_occurred):
    """Calculate reward based on game events"""
    if collision_occurred:
        return -100  # Heavy penalty for dying

    if new_score > old_score:
        return 50  # Reward for eating apple

    # Small penalty for each move to encourage efficiency
    return -1


def choose_action(state, valid_actions):
    """Choose action using epsilon-greedy strategy"""
    global training_stats
    state_str = str(state)  # Convert tuple to string for Q-table key

    if random.random() < EPSILON:
        # Explore: choose random valid action
        training_stats["exploration_count"] += 1
        return random.choice(valid_actions)
    else:
        # Exploit: choose best known action
        training_stats["exploitation_count"] += 1
        best_action = None
        best_value = float("-inf")

        for action in valid_actions:
            q_value = q_table[state_str][action]
            if q_value > best_value:
                best_value = q_value
                best_action = action

        return best_action if best_action else random.choice(valid_actions)


def update_q_table(old_state, action, reward, new_state, valid_new_actions):
    """Update Q-table using Q-learning formula"""
    old_state_str = str(old_state)  # Convert tuple to string
    new_state_str = str(new_state)  # Convert tuple to string

    # Find max Q-value for next state
    max_next_q = 0
    if valid_new_actions:
        max_next_q = max(q_table[new_state_str][a] for a in valid_new_actions)

    # Q-learning formula: Q(s,a) = Q(s,a) + α[r + γ*max(Q(s',a')) - Q(s,a)]
    old_q_value = q_table[old_state_str][action]
    new_q_value = old_q_value + LEARNING_RATE * (
        reward + DISCOUNT_FACTOR * max_next_q - old_q_value
    )
    q_table[old_state_str][action] = new_q_value


# Global variables to maintain state between calls
last_state = None
last_action = None
last_score = 0
game_count = 0


def learning_model(game):
    """
    Simple Q-Learning agent for Snake game.

    This implements a basic Q-learning algorithm that:
    1. Simplifies the game state to avoid curse of dimensionality
    2. Uses exploration/exploitation to balance learning and performance
    3. Learns from rewards (eating apples) and penalties (collisions)
    4. Saves/loads learned knowledge to/from file
    5. Tracks comprehensive training statistics
    """
    global last_state, last_action, last_score, game_count

    # Load Q-table and training stats on first run
    if game_count == 0:
        print("🚀 Initializing Q-Learning Agent...")
        load_q_table()
        load_training_stats()
        game_count += 1
        print(f"📊 Starting Episode {training_stats['total_episodes'] + 1}")

    # Update training statistics
    training_stats["total_steps"] += 1
    training_stats["current_episode_steps"] += 1

    # Check for maximum episode length to prevent infinite episodes
    MAX_EPISODE_STEPS = 200  # Reduced for faster training cycles
    if training_stats["current_episode_steps"] > MAX_EPISODE_STEPS:
        print(
            f"⏰ Episode reached maximum length ({MAX_EPISODE_STEPS} steps), forcing game over..."
        )
        handle_game_over()
        reset_learning_state()
        return "down"  # Return a safe default action

    # Get current state and score
    current_state = get_simple_state(game)
    current_score = game.snake.length - 1
    training_stats["current_episode_score"] = current_score

    # Get valid actions (no immediate U-turns)
    current_direction = game.snake.direction
    all_actions = ["left", "right", "up", "down"]
    opposite = {"left": "right", "right": "left", "up": "down", "down": "up"}

    valid_actions = []
    for action in all_actions:
        if action != opposite.get(current_direction):  # Avoid U-turns
            next_x, next_y = game._get_potential_head(action)
            if not game._is_potential_move_colliding(next_x, next_y):
                valid_actions.append(action)

    # If no valid actions, try all actions (emergency)
    if not valid_actions:
        valid_actions = [a for a in all_actions if a != opposite.get(current_direction)]

    # If we have previous state and action, update Q-table
    if last_state is not None and last_action is not None:
        reward = get_reward(game, last_score, current_score, False)
        update_q_table(last_state, last_action, reward, current_state, valid_actions)

    # Choose next action
    if valid_actions:
        action = choose_action(current_state, valid_actions)

        # Execute action
        if action == "left":
            game.snake.move_left()
        elif action == "right":
            game.snake.move_right()
        elif action == "up":
            game.snake.move_up()
        elif action == "down":
            game.snake.move_down()

        # Store current state and action for next iteration
        last_state = current_state
        last_action = action
        last_score = current_score

    # Save Q-table periodically (every 50 calls)
    if game_count % 50 == 0:
        save_q_table()


def reset_learning_state():
    """Reset learning state when game restarts"""
    global last_state, last_action, last_score
    print("🔄 Resetting learning state for new episode")
    last_state = None
    last_action = None
    last_score = 0
    # Reset episode-specific stats
    training_stats["current_episode_steps"] = 0
    training_stats["current_episode_score"] = 0


def handle_game_over():
    """Handle game over event for learning and record episode statistics"""
    global last_state, last_action, last_score

    print(f"🎮 Game Over! Episode {training_stats['total_episodes'] + 1} completed")

    if last_state is not None and last_action is not None:
        # Give heavy penalty for collision
        reward = -100
        update_q_table(last_state, last_action, reward, "", [])

    # Record episode statistics
    final_score = training_stats["current_episode_score"]
    episode_length = training_stats["current_episode_steps"]

    training_stats["total_episodes"] += 1
    training_stats["scores_history"].append(final_score)
    training_stats["episode_lengths"].append(episode_length)

    # Update best score
    if final_score > training_stats["best_score"]:
        training_stats["best_score"] = final_score
        print(f"🎉 New best score: {final_score}!")

    # Calculate running averages
    calculate_avg_last_100()
    update_q_table_size()

    # Print progress and save
    print_training_progress()

    reset_learning_state()
    print("💾 Saving progress...")
    save_q_table()
    save_training_stats()
    print("✅ Progress saved!")


def get_training_summary():
    """Get a comprehensive summary of training progress"""
    if training_stats["total_episodes"] == 0:
        return "No training data available yet."

    summary = f"""
🧠 Q-Learning Training Summary 🧠
================================================
📊 Episodes Completed: {training_stats["total_episodes"]}
🎯 Total Actions Taken: {training_stats["total_steps"]}
🏆 Best Score Achieved: {training_stats["best_score"]}
📈 Average Score (Last 100): {training_stats["last_100_avg_score"]:.2f}

🔍 Exploration vs Exploitation:
   - Exploration Actions: {training_stats["exploration_count"]} ({training_stats["exploration_count"]/max(1,training_stats["total_steps"])*100:.1f}%)
   - Exploitation Actions: {training_stats["exploitation_count"]} ({training_stats["exploitation_count"]/max(1,training_stats["total_steps"])*100:.1f}%)

🧠 Learning Progress:
   - Q-Table Size: {training_stats["q_table_size"]} state-action pairs
   - Average Episode Length: {sum(training_stats["episode_lengths"])/len(training_stats["episode_lengths"]):.1f} steps
"""

    if training_stats["learning_start_time"]:
        training_time = (time.time() - training_stats["learning_start_time"]) / 60
        summary += f"   - Total Training Time: {training_time:.1f} minutes\n"

    # Recent performance (last 10 episodes)
    if len(training_stats["scores_history"]) >= 10:
        recent_scores = training_stats["scores_history"][-10:]
        recent_avg = sum(recent_scores) / len(recent_scores)
        summary += f"\n📊 Recent Performance (Last 10 Episodes):\n"
        summary += f"   - Scores: {recent_scores}\n"
        summary += f"   - Average: {recent_avg:.1f}\n"

    summary += "================================================"
    return summary


def save_training_report():
    """Save a detailed training report to file"""
    report_content = get_training_summary()

    # Also include detailed statistics
    report_content += f"\n\nDetailed Statistics:\n"
    report_content += f"All Scores: {training_stats['scores_history']}\n"
    report_content += f"Episode Lengths: {training_stats['episode_lengths']}\n"

    try:
        with open("training_report.txt", "w") as f:
            f.write(report_content)
        print("📝 Training report saved to 'training_report.txt'")
    except:
        print("❌ Error saving training report")


# ============================================================================
# AUTOMATIC TRAINING FUNCTIONS
# ============================================================================


def run_automatic_training(
    episodes=10000,
    save_interval=250,
    report_interval=500,
    early_stopping=True,
    target_score=20,
    gui_mode=False,
):
    """
    Run automatic training without GUI for faster learning

    Args:
        episodes: Number of episodes to train
        save_interval: Save progress every N episodes
        report_interval: Print progress every N episodes
        early_stopping: Stop if performance plateaus
        target_score: Stop if average score reaches this value
        gui_mode: Whether to show GUI during training
    """
    print(f"🚀 Starting automatic training for {episodes} episodes")
    print(f"📊 Progress will be saved every {save_interval} episodes")
    print(f"📈 Reports every {report_interval} episodes")

    if not gui_mode:
        print("🏃‍♂️ Running in fast mode (no GUI)")

    # Load existing progress
    load_q_table()
    load_training_stats()

    start_episode = training_stats["total_episodes"]
    start_time = time.time()

    consecutive_no_improvement = 0
    best_recent_avg = 0

    for episode in range(episodes):
        current_episode = start_episode + episode + 1

        if gui_mode:
            # Train with GUI (slower but visual)
            score = train_single_episode_fast()  # Use fast for now
        else:
            # Train without GUI (faster)
            score = train_single_episode_fast()

        # Check for improvement (early stopping)
        if early_stopping and len(training_stats["scores_history"]) >= 100:
            recent_avg = sum(training_stats["scores_history"][-100:]) / 100

            if recent_avg > best_recent_avg:
                best_recent_avg = recent_avg
                consecutive_no_improvement = 0
            else:
                consecutive_no_improvement += 1

            # Stop if no improvement for 500 episodes
            if consecutive_no_improvement >= 500:
                print(f"🛑 Early stopping: No improvement for 500 episodes")
                break

            # Stop if target score reached
            if recent_avg >= target_score:
                print(
                    f"🎯 Target score {target_score} reached! Average: {recent_avg:.2f}"
                )
                break

        # Save progress
        if (episode + 1) % save_interval == 0:
            save_q_table()
            save_training_stats()

        # Print progress report
        if (episode + 1) % report_interval == 0:
            elapsed_time = time.time() - start_time
            print_training_progress_detailed(episode + 1, elapsed_time)

    # Final save and report
    save_q_table()
    save_training_stats()
    total_time = time.time() - start_time

    print(f"\n✅ Automatic training completed!")
    print(f"🕐 Total time: {total_time/60:.1f} minutes")
    print(f"📊 Episodes trained: {episodes}")
    print(get_training_summary())


def train_single_episode_fast():
    """Train a single episode without GUI for speed - simplified version"""

    # Simple Q-learning training loop without complex game simulation
    # This focuses on Q-table updates rather than full game simulation

    game = SimpleGameState()
    score = 0
    steps = 0
    max_steps = 200

    # Initialize episode
    reset_learning_state()

    while not game.game_over and steps < max_steps:
        # Get current state
        current_state = game.get_state()

        # Choose action using epsilon-greedy
        action = choose_action_epsilon_greedy(current_state)

        # Execute action and get reward
        reward, new_score = game.step(action)
        score = new_score

        # Get new state
        new_state = game.get_state()

        # Update Q-table
        valid_actions = ["up", "down", "left", "right"]
        update_q_table(current_state, action, reward, new_state, valid_actions)

        steps += 1

    # Handle episode completion
    training_stats["current_episode_score"] = score
    handle_game_over()

    return score


class SimpleGameState:
    """Simplified game state for fast training"""

    def __init__(self):
        self.grid_size = 10
        self.snake_pos = (5, 5)  # Head position
        self.apple_pos = (7, 7)
        self.score = 0
        self.game_over = False
        self.direction = "right"

    def get_state(self):
        """Get simplified state representation"""
        head_x, head_y = self.snake_pos
        apple_x, apple_y = self.apple_pos

        # Calculate relative apple direction
        apple_dir_x = 0 if apple_x == head_x else (1 if apple_x > head_x else -1)
        apple_dir_y = 0 if apple_y == head_y else (1 if apple_y > head_y else -1)

        # Calculate distance to apple (bucketed)
        distance = abs(apple_x - head_x) + abs(apple_y - head_y)
        if distance <= 2:
            dist_bucket = "very_close"
        elif distance <= 4:
            dist_bucket = "close"
        elif distance <= 7:
            dist_bucket = "medium"
        else:
            dist_bucket = "far"

        # Check dangers
        dangers = self.get_dangers()

        return (
            apple_dir_x,
            apple_dir_y,
            dist_bucket,
            self.direction,
            dangers["up"],
            dangers["down"],
            dangers["left"],
            dangers["right"],
        )

    def get_dangers(self):
        """Check for dangers in each direction"""
        head_x, head_y = self.snake_pos

        dangers = {}
        directions = {
            "up": (head_x, head_y - 1),
            "down": (head_x, head_y + 1),
            "left": (head_x - 1, head_y),
            "right": (head_x + 1, head_y),
        }

        for direction, (new_x, new_y) in directions.items():
            # Check wall collision
            if (
                new_x < 0
                or new_x >= self.grid_size
                or new_y < 0
                or new_y >= self.grid_size
            ):
                dangers[direction] = True
            else:
                dangers[direction] = False

        return dangers

    def step(self, action):
        """Execute action and return reward"""
        head_x, head_y = self.snake_pos

        # Update direction and position
        self.direction = action

        if action == "up":
            new_pos = (head_x, head_y - 1)
        elif action == "down":
            new_pos = (head_x, head_y + 1)
        elif action == "left":
            new_pos = (head_x - 1, head_y)
        elif action == "right":
            new_pos = (head_x + 1, head_y)
        else:
            new_pos = self.snake_pos

        # Check for wall collision
        new_x, new_y = new_pos
        if new_x < 0 or new_x >= self.grid_size or new_y < 0 or new_y >= self.grid_size:
            self.game_over = True
            return -100, self.score  # Collision penalty

        # Update position
        self.snake_pos = new_pos

        # Check if apple eaten
        if self.snake_pos == self.apple_pos:
            self.score += 1
            self.place_new_apple()
            return 50, self.score  # Apple reward

        # Calculate reward based on distance to apple
        old_distance = abs(self.apple_pos[0] - head_x) + abs(self.apple_pos[1] - head_y)
        new_distance = abs(self.apple_pos[0] - new_x) + abs(self.apple_pos[1] - new_y)

        if new_distance < old_distance:
            return 1, self.score  # Moving closer to apple
        else:
            return -1, self.score  # Moving away or staying same distance

    def place_new_apple(self):
        """Place apple in new random location"""
        import random

        while True:
            new_apple = (
                random.randint(0, self.grid_size - 1),
                random.randint(0, self.grid_size - 1),
            )
            if new_apple != self.snake_pos:
                self.apple_pos = new_apple
                break


def choose_action_epsilon_greedy(state):
    """Choose action using epsilon-greedy policy"""
    actions = ["up", "down", "left", "right"]

    if random.random() < EPSILON:
        # Exploration: choose random action
        training_stats["exploration_count"] += 1
        return random.choice(actions)
    else:
        # Exploitation: choose best known action
        training_stats["exploitation_count"] += 1
        best_action = max(actions, key=lambda a: q_table[state][a])
        return best_action


def train_fast(episodes=500):
    """Quick training function - 500 episodes without GUI"""
    print("🏃‍♂️ Starting fast training session...")
    run_automatic_training(episodes=episodes, gui_mode=False, save_interval=50)


def train_comprehensive(episodes=5000):
    """Comprehensive training session - 5000 episodes"""
    print("🧠 Starting comprehensive training session...")
    run_automatic_training(
        episodes=episodes, gui_mode=False, save_interval=250, report_interval=500
    )


def resume_training(additional_episodes=1000):
    """Resume training from last saved state"""
    load_q_table()
    load_training_stats()

    current_episodes = training_stats["total_episodes"]
    print(f"📥 Resuming training from episode {current_episodes}")

    run_automatic_training(episodes=additional_episodes, gui_mode=False)


def evaluate_performance(test_episodes=100):
    """Evaluate the trained agent's performance"""
    print(f"🧪 Evaluating agent performance over {test_episodes} episodes...")

    load_q_table()

    # Temporarily disable exploration for evaluation
    global EPSILON
    original_epsilon = EPSILON
    EPSILON = 0.0  # Pure exploitation

    scores = []
    for episode in range(test_episodes):
        score = train_single_episode_fast()
        scores.append(score)

        if (episode + 1) % 20 == 0:
            avg_so_far = sum(scores) / len(scores)
            print(
                f"📊 Episode {episode + 1}/{test_episodes}: Average = {avg_so_far:.2f}"
            )

    # Restore original epsilon
    EPSILON = original_epsilon

    # Calculate statistics
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    print(f"\n🎯 Performance Evaluation Results:")
    print(f"   Average Score: {avg_score:.2f}")
    print(f"   Best Score: {max_score}")
    print(f"   Worst Score: {min_score}")
    print(f"   Score Range: {min_score} - {max_score}")

    return {"average": avg_score, "max": max_score, "min": min_score, "scores": scores}


def generate_report():
    """Generate a comprehensive training report"""
    print("📝 Generating comprehensive training report...")

    # Save detailed report
    save_training_report()

    # Print summary
    print(get_training_summary())

    # Performance evaluation if trained
    if training_stats["total_episodes"] > 0:
        evaluate_performance(50)


def print_training_progress_detailed(episodes_completed, elapsed_time):
    """Print detailed training progress"""
    if len(training_stats["scores_history"]) == 0:
        return

    recent_scores = (
        training_stats["scores_history"][-50:]
        if len(training_stats["scores_history"]) >= 50
        else training_stats["scores_history"]
    )
    avg_recent = sum(recent_scores) / len(recent_scores)

    print(f"\n📊 Training Progress Report")
    print(f"   Episodes Completed: {episodes_completed}")
    print(f"   Time Elapsed: {elapsed_time/60:.1f} minutes")
    print(f"   Average Score (last {len(recent_scores)}): {avg_recent:.2f}")
    print(f"   Best Score Ever: {training_stats['best_score']}")
    print(f"   Q-Table Size: {len(q_table)} states")

    if len(training_stats["scores_history"]) >= 10:
        last_10 = training_stats["scores_history"][-10:]
        print(f"   Last 10 Scores: {last_10}")


class HeadlessGame:
    """Simplified game class for fast training without GUI"""

    def __init__(self):
        self.grid_size = SIZE
        self.snake = [(SIZE // 2, SIZE // 2)]  # Initialize with starting position
        self.apple_pos = (SIZE // 4, SIZE // 4)  # Initialize apple position
        self.score = 0
        self.game_over = False

    def run_episode(self):
        """Run a single episode and return the score"""
        self.reset_game()
        steps = 0
        max_steps = 1000  # Prevent infinite loops

        while not self.game_over and steps < max_steps:
            # Get current game state
            game_state = self.get_game_state()

            # Let learning agent make decision
            direction = self.get_learning_action(game_state)

            # Execute move
            self.move_snake(direction)

            # Check for collisions and apple eating
            self.check_collisions()
            self.check_apple_eaten()

            steps += 1

        # Handle episode end
        final_score = self.score
        handle_game_over()
        return final_score

    def reset_game(self):
        """Reset game state for new episode"""
        self.score = 0
        self.game_over = False
        self.snake = [(self.grid_size // 2, self.grid_size // 2)]  # Start in center
        self.place_apple()
        reset_learning_state()

    def place_apple(self):
        """Place apple in random location"""
        while True:
            x = random.randint(1, self.grid_size - 2)
            y = random.randint(1, self.grid_size - 2)
            if (x, y) not in self.snake:
                self.apple_pos = (x, y)
                break

    def get_game_state(self):
        """Get current game state for learning agent"""
        head = self.snake[0]
        return {
            "snake_head": head,
            "snake_body": self.snake,
            "apple_pos": self.apple_pos,
            "score": self.score,
        }

    def get_learning_action(self, game_state):
        """Get action from learning agent"""
        # Simulate the learning_model function call
        head_x, head_y = game_state["snake_head"]
        apple_x, apple_y = game_state["apple_pos"]

        # Create mock game object for learning_model
        # The learning_model expects specific properties, so we need to mock them properly
        mock_snake = type(
            "MockSnake",
            (),
            {
                "x": head_x * 20,  # Convert to pixel coordinates
                "y": head_y * 20,
                "body": [(x * 20, y * 20) for x, y in game_state["snake_body"]],
                "length": len(game_state["snake_body"]),  # Add length property
                "direction": "down",  # Default direction
            },
        )()

        mock_apple = type("MockApple", (), {"x": apple_x * 20, "y": apple_y * 20})()

        mock_game = type(
            "MockGame",
            (),
            {
                "snake": mock_snake,
                "apple": mock_apple,
                "score": game_state["score"],
                # Add methods that learning_model might call
                "_get_potential_head": lambda action: self._get_potential_head_pos(
                    action
                ),
                "_is_potential_move_colliding": lambda x, y: self._is_colliding(x, y),
            },
        )()

        # Get direction from learning model
        return learning_model(mock_game)

    def _get_potential_head_pos(self, action):
        """Get potential head position for given action"""
        head_x, head_y = self.snake[0]

        if action == "UP" or action == "up":
            return (head_x, head_y - 1)
        elif action == "DOWN" or action == "down":
            return (head_x, head_y + 1)
        elif action == "LEFT" or action == "left":
            return (head_x - 1, head_y)
        elif action == "RIGHT" or action == "right":
            return (head_x + 1, head_y)
        else:
            return self.snake[0]  # Current position if invalid action

    def _is_colliding(self, x, y):
        """Check if position would cause collision"""
        # Wall collision
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
            return True

        # Self collision (but not with current head)
        if (x, y) in self.snake[1:]:
            return True

        return False

    def move_snake(self, direction):
        """Move snake in given direction"""
        head_x, head_y = self.snake[0]

        if direction == "UP":
            new_head = (head_x, head_y - 1)
        elif direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        else:
            return  # Invalid direction

        self.snake.insert(0, new_head)

        # Check if apple was eaten
        if new_head != self.apple_pos:
            self.snake.pop()  # Remove tail if no apple eaten

    def check_collisions(self):
        """Check for wall and self collisions"""
        head_x, head_y = self.snake[0]

        # Wall collision
        if (
            head_x < 0
            or head_x >= self.grid_size
            or head_y < 0
            or head_y >= self.grid_size
        ):
            self.game_over = True
            return

        # Self collision
        if self.snake[0] in self.snake[1:]:
            self.game_over = True

    def check_apple_eaten(self):
        """Check if apple was eaten and place new one"""
        if self.snake[0] == self.apple_pos:
            self.score += 1
            self.place_apple()


# Convenience functions for easy access
def quick_train():
    """Quick training - 500 episodes"""
    train_fast(500)


def full_train():
    """Full training - 2000 episodes"""
    train_comprehensive(2000)


def test_agent():
    """Test the trained agent"""
    return evaluate_performance(100)
