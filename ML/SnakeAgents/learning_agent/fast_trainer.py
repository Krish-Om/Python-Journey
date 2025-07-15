#!/usr/bin/env python3
"""
Fast Q-Learning trainer for Snake game - No GUI mode for rapid learning
Trains agent quickly without graphics, then uses learned model for gameplay
"""

import sys
import os
import time
import random
import json
from collections import defaultdict

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Q-Learning parameters optimized for fast training
LEARNING_RATE = 0.15  # Slightly higher for faster learning
DISCOUNT_FACTOR = 0.95
EPSILON = 0.3  # Exploration rate
SIZE = 40  # Grid size from the game

# Training configuration
GRID_WIDTH = 25  # Game grid width (1000 / 40)
GRID_HEIGHT = 20  # Game grid height (800 / 40)


class FastSnakeTrainer:
    """Fast Snake game simulation for Q-learning training without GUI"""

    def __init__(self):
        self.reset_game()

        # Q-table and training stats
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.training_stats = {
            "total_episodes": 0,
            "total_steps": 0,
            "scores_history": [],
            "episode_lengths": [],
            "best_score": 0,
            "last_100_avg": 0.0,
            "q_table_size": 0,
            "training_start_time": time.time(),
        }

        # Load existing data
        self.load_q_table()
        self.load_training_stats()

    def reset_game(self):
        """Reset game state for new episode"""
        # Snake starts in center
        self.snake_x = [GRID_WIDTH // 2]
        self.snake_y = [GRID_HEIGHT // 2]
        self.snake_direction = "right"
        self.snake_length = 1

        # Random apple position
        self.place_apple()

        self.game_over = False
        self.score = 0
        self.steps = 0

    def place_apple(self):
        """Place apple at random valid position"""
        while True:
            self.apple_x = random.randint(0, GRID_WIDTH - 1)
            self.apple_y = random.randint(0, GRID_HEIGHT - 1)

            # Ensure apple doesn't spawn on snake
            if (self.apple_x, self.apple_y) not in zip(self.snake_x, self.snake_y):
                break

    def get_state(self):
        """Get current game state for Q-learning"""
        head_x, head_y = self.snake_x[0], self.snake_y[0]

        # Direction to apple
        apple_dx = 0 if self.apple_x == head_x else (1 if self.apple_x > head_x else -1)
        apple_dy = 0 if self.apple_y == head_y else (1 if self.apple_y > head_y else -1)

        # Danger detection (wall and self-collision)
        danger_left = self.is_collision(head_x - 1, head_y)
        danger_right = self.is_collision(head_x + 1, head_y)
        danger_up = self.is_collision(head_x, head_y - 1)
        danger_down = self.is_collision(head_x, head_y + 1)

        # Current direction
        dir_left = self.snake_direction == "left"
        dir_right = self.snake_direction == "right"
        dir_up = self.snake_direction == "up"
        dir_down = self.snake_direction == "down"

        # Distance to apple (normalized)
        distance = abs(head_x - self.apple_x) + abs(head_y - self.apple_y)
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

    def is_collision(self, x, y):
        """Check if position would cause collision"""
        # Wall collision
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            return True

        # Self collision
        for i in range(len(self.snake_x)):
            if x == self.snake_x[i] and y == self.snake_y[i]:
                return True

        return False

    def step(self, action):
        """Execute one game step with given action"""
        if self.game_over:
            return -10, self.score

        # Update direction based on action
        old_direction = self.snake_direction
        if action == "left" and self.snake_direction != "right":
            self.snake_direction = "left"
        elif action == "right" and self.snake_direction != "left":
            self.snake_direction = "right"
        elif action == "up" and self.snake_direction != "down":
            self.snake_direction = "up"
        elif action == "down" and self.snake_direction != "up":
            self.snake_direction = "down"

        # Move snake
        head_x, head_y = self.snake_x[0], self.snake_y[0]

        # Initialize new head position
        new_head_x, new_head_y = head_x, head_y

        if self.snake_direction == "left":
            new_head_x, new_head_y = head_x - 1, head_y
        elif self.snake_direction == "right":
            new_head_x, new_head_y = head_x + 1, head_y
        elif self.snake_direction == "up":
            new_head_x, new_head_y = head_x, head_y - 1
        elif self.snake_direction == "down":
            new_head_x, new_head_y = head_x, head_y + 1

        # Check collision
        if self.is_collision(new_head_x, new_head_y):
            self.game_over = True
            return -100, self.score  # Large negative reward for death

        # Add new head
        self.snake_x.insert(0, new_head_x)
        self.snake_y.insert(0, new_head_y)

        reward = -1  # Small negative reward for each step (encourages efficiency)

        # Check if ate apple
        if new_head_x == self.apple_x and new_head_y == self.apple_y:
            self.score += 1
            self.snake_length += 1
            reward = 100  # Large positive reward for eating apple
            self.place_apple()
        else:
            # Remove tail if didn't eat apple
            self.snake_x.pop()
            self.snake_y.pop()

        # Reward for moving toward apple
        old_distance = abs(head_x - self.apple_x) + abs(head_y - self.apple_y)
        new_distance = abs(new_head_x - self.apple_x) + abs(new_head_y - self.apple_y)

        if new_distance < old_distance:
            reward += 1  # Small reward for getting closer to apple
        elif new_distance > old_distance:
            reward -= 1  # Small penalty for moving away

        self.steps += 1

        # End game if too many steps without progress
        if self.steps > 500:
            self.game_over = True
            reward -= 50

        return reward, self.score

    def choose_action(self, state, epsilon=0.3):
        """Choose action using epsilon-greedy strategy"""
        if random.random() < epsilon:
            # Exploration: random action
            return random.choice(["up", "down", "left", "right"])
        else:
            # Exploitation: best known action
            actions = ["up", "down", "left", "right"]
            q_values = [self.q_table[str(state)][action] for action in actions]
            max_q = max(q_values)

            # Handle ties randomly
            best_actions = [
                actions[i] for i in range(len(actions)) if q_values[i] == max_q
            ]
            return random.choice(best_actions)

    def update_q_table(self, state, action, reward, next_state):
        """Update Q-table using Q-learning formula"""
        state_str = str(state)
        next_state_str = str(next_state)

        # Current Q-value
        current_q = self.q_table[state_str][action]

        # Maximum Q-value for next state
        next_actions = ["up", "down", "left", "right"]
        next_q_values = [self.q_table[next_state_str][a] for a in next_actions]
        max_next_q = max(next_q_values) if next_q_values else 0

        # Q-learning update
        new_q = current_q + LEARNING_RATE * (
            reward + DISCOUNT_FACTOR * max_next_q - current_q
        )
        self.q_table[state_str][action] = new_q

    def train_episode(self):
        """Train one complete episode"""
        self.reset_game()
        episode_reward = 0

        while not self.game_over and self.steps < 500:
            # Get current state
            current_state = self.get_state()

            # Choose action
            action = self.choose_action(current_state, EPSILON)

            # Execute action
            reward, score = self.step(action)
            episode_reward += reward

            # Get new state
            new_state = self.get_state()

            # Update Q-table
            self.update_q_table(current_state, action, reward, new_state)

        # Update training statistics
        self.training_stats["total_episodes"] += 1
        self.training_stats["total_steps"] += self.steps
        self.training_stats["scores_history"].append(self.score)
        self.training_stats["episode_lengths"].append(self.steps)

        if self.score > self.training_stats["best_score"]:
            self.training_stats["best_score"] = self.score

        # Calculate last 100 average
        if len(self.training_stats["scores_history"]) >= 100:
            self.training_stats["last_100_avg"] = (
                sum(self.training_stats["scores_history"][-100:]) / 100
            )

        self.training_stats["q_table_size"] = sum(
            len(actions) for actions in self.q_table.values()
        )

        return self.score, episode_reward

    def fast_train(self, episodes=5000, report_every=500):
        """Fast training without GUI"""
        print(f"🚀 Starting FAST training for {episodes} episodes (NO GUI)")
        print("⚡ This will be much faster than GUI mode!")
        print("=" * 60)

        start_time = time.time()
        start_episode = self.training_stats["total_episodes"]

        for episode in range(episodes):
            score, reward = self.train_episode()

            # Progress report
            if (episode + 1) % report_every == 0:
                elapsed = time.time() - start_time
                episodes_per_sec = (episode + 1) / elapsed

                print(f"📊 Episode {start_episode + episode + 1}")
                print(f"   Score: {score} | Reward: {reward:.1f}")
                print(f"   Best Score: {self.training_stats['best_score']}")
                print(f"   Avg Last 100: {self.training_stats['last_100_avg']:.2f}")
                print(f"   Q-table Size: {self.training_stats['q_table_size']}")
                print(f"   Speed: {episodes_per_sec:.1f} episodes/sec")
                print(f"   Elapsed: {elapsed/60:.1f} min")
                print("-" * 40)

        total_time = time.time() - start_time
        print(f"\n✅ Fast training completed!")
        print(f"⏱️  Total time: {total_time/60:.2f} minutes")
        print(f"🏃‍♂️ Average speed: {episodes/total_time:.1f} episodes/second")
        print(f"🎯 Final best score: {self.training_stats['best_score']}")
        print(f"📈 Final avg (last 100): {self.training_stats['last_100_avg']:.2f}")

        # Save progress
        self.save_q_table()
        self.save_training_stats()

        return self.training_stats

    def load_q_table(self):
        """Load Q-table from file"""
        q_table_file = os.path.join(os.path.dirname(__file__), "q_table.json")
        if os.path.exists(q_table_file):
            try:
                with open(q_table_file, "r") as f:
                    loaded_data = json.load(f)
                    self.q_table = defaultdict(lambda: defaultdict(float))
                    for state_str, actions in loaded_data.items():
                        for action, value in actions.items():
                            self.q_table[state_str][action] = value
                print(f"✅ Loaded Q-table with {len(loaded_data)} states")
            except Exception as e:
                print(f"⚠️  Error loading Q-table: {e}")

    def save_q_table(self):
        """Save Q-table to file"""
        q_table_file = os.path.join(os.path.dirname(__file__), "q_table.json")
        # Convert defaultdict to regular dict for JSON serialization
        q_table_dict = {state: dict(actions) for state, actions in self.q_table.items()}

        with open(q_table_file, "w") as f:
            json.dump(q_table_dict, f, indent=2)

    def load_training_stats(self):
        """Load training statistics"""
        stats_file = os.path.join(os.path.dirname(__file__), "training_stats.json")
        if os.path.exists(stats_file):
            try:
                with open(stats_file, "r") as f:
                    loaded_stats = json.load(f)
                    self.training_stats.update(loaded_stats)
                print(
                    f"✅ Loaded training stats - {self.training_stats['total_episodes']} episodes completed"
                )
            except Exception as e:
                print(f"⚠️  Error loading training stats: {e}")

    def save_training_stats(self):
        """Save training statistics"""
        stats_file = os.path.join(os.path.dirname(__file__), "training_stats.json")
        with open(stats_file, "w") as f:
            json.dump(self.training_stats, f, indent=2)


def main():
    """Main training function"""
    trainer = FastSnakeTrainer()

    print("🐍 Fast Snake Q-Learning Trainer")
    print("=" * 50)

    while True:
        print("\n🎯 Training Options:")
        print("1. Quick train (1,000 episodes)")
        print("2. Medium train (5,000 episodes)")
        print("3. Long train (10,000 episodes)")
        print("4. Custom episodes")
        print("5. View current stats")
        print("6. Exit")

        choice = input("\nChoose option (1-6): ").strip()

        if choice == "1":
            trainer.fast_train(1000, 200)
        elif choice == "2":
            trainer.fast_train(5000, 500)
        elif choice == "3":
            trainer.fast_train(10000, 1000)
        elif choice == "4":
            try:
                episodes = int(input("Enter number of episodes: "))
                report_every = max(episodes // 10, 100)
                trainer.fast_train(episodes, report_every)
            except ValueError:
                print("❌ Invalid number")
        elif choice == "5":
            stats = trainer.training_stats
            print(f"\n📊 Current Training Statistics:")
            print(f"Total Episodes: {stats['total_episodes']}")
            print(f"Best Score: {stats['best_score']}")
            print(f"Average (last 100): {stats['last_100_avg']:.2f}")
            print(f"Q-table Size: {stats['q_table_size']}")
        elif choice == "6":
            print("👋 Happy gaming!")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
