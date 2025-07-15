#!/usr/bin/env python3
"""
Quick launcher for fast Snake training
Trains 5,000 episodes rapidly without GUI
"""

from fast_trainer import FastSnakeTrainer


def main():
    print("🚀 Fast Snake Training - 5,000 Episodes")
    print("⚡ Training without GUI for maximum speed!")
    print("=" * 50)

    trainer = FastSnakeTrainer()

    # Train 5,000 episodes quickly
    trainer.fast_train(episodes=5000, report_every=500)

    print("\n🎯 Training Complete!")
    print("🎮 Now run 'python ../source.py' to see your trained agent play!")
    print("📊 Or run 'python play_autonomous.py' for guided gameplay")


if __name__ == "__main__":
    main()
