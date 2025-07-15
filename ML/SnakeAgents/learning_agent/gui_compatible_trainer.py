#!/usr/bin/env python3
"""
GUI-Compatible Fast Trainer for Snake Q-Learning
Trains using the exact same game logic and state representation as source.py
"""

import sys
import os
import time
import json
from collections import defaultdict

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the actual game logic
from source import Game
import pygame


class HeadlessGameTrainer:
    """Fast training using actual Game class but without GUI rendering"""

    def __init__(self):
        # Initialize pygame but don't create visible window
        pygame.init()
        pygame.display.set_mode((1, 1), pygame.NOFRAME)  # Minimal hidden window

        self.episodes_trained = 0
        self.scores = []

    def train_episode(self):
        """Train one episode using the real game logic"""
        # Create game instance
        game = Game()
        game_over = False
        steps = 0
        max_steps = 500

        try:
            while not game_over and steps < max_steps:
                # Use the actual learning_model function
                from learning_agent.learning_model import learning_model

                learning_model(game)

                # Run one game step without rendering
                try:
                    # Disable rendering temporarily
                    old_flip = pygame.display.flip
                    pygame.display.flip = lambda: None  # Disable screen updates

                    game.play()  # This runs the actual game logic

                    # Restore rendering
                    pygame.display.flip = old_flip

                except Exception as e:
                    # Game over occurred
                    game_over = True
                    final_score = game.snake.length - 1
                    return final_score

                steps += 1

            # If we reach max steps without game over
            if steps >= max_steps:
                return game.snake.length - 1

        except Exception as e:
            return game.snake.length - 1

    def fast_train(self, episodes=1000):
        """Train for specified number of episodes"""
        print(f"🚀 Starting GUI-Compatible Training for {episodes} episodes")
        print("🎯 Using exact same game logic as source.py")
        print("=" * 60)

        start_time = time.time()

        for episode in range(episodes):
            score = self.train_episode()
            self.scores.append(score)
            self.episodes_trained += 1

            # Progress reporting
            if (episode + 1) % 100 == 0:
                avg_score = sum(self.scores[-100:]) / min(100, len(self.scores))
                elapsed = time.time() - start_time
                eps_per_sec = (episode + 1) / elapsed

                print(f"📊 Episode {episode + 1}")
                print(f"   Last Score: {score}")
                print(f"   Avg (last 100): {avg_score:.2f}")
                print(f"   Speed: {eps_per_sec:.1f} eps/sec")
                print(f"   Elapsed: {elapsed/60:.1f} min")
                print("-" * 40)

        total_time = time.time() - start_time
        final_avg = sum(self.scores[-100:]) / min(100, len(self.scores))

        print(f"\n✅ Training completed!")
        print(f"⏱️  Total time: {total_time/60:.2f} minutes")
        print(f"🎯 Final average score: {final_avg:.2f}")
        print(f"📈 Best score: {max(self.scores)}")
        print(f"🏃‍♂️ Training speed: {episodes/total_time:.1f} episodes/second")


def main():
    """Main training function"""
    trainer = HeadlessGameTrainer()

    print("🐍 GUI-Compatible Snake Q-Learning Trainer")
    print("🎯 This trainer uses the exact same game logic as source.py")
    print("=" * 60)

    # Start with 2000 episodes of focused training
    trainer.fast_train(2000)

    print("\n🎮 Training complete! The agent is now ready for GUI gameplay.")
    print("🎯 Run 'python ../source.py' to see the trained agent play!")


if __name__ == "__main__":
    main()
