#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Game Penjumlahan Anak-Anak dengan GUI
Author: Yohanes 2026
"""

import tkinter as tk
from tkinter import messagebox, font
import random
import time
import json
import os

class GamePenjumlahan:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Penjumlahan Anak-Anak")
        self.root.geometry("800x600")
        self.root.configure(bg='#FFE4B5')  # Warna peach cerah
        
        # Game variables
        self.score = 0
        self.time_left = 60
        self.current_level = "Mudah"
        self.soal_count = 0
        self.max_soal = 10
        self.timer_running = False
        self.current_answer = 0
        self.high_scores = {}
        
        # Level configurations
        self.level_config = {
            "Mudah": {"min": 1, "max": 10, "soal": 10, "time": 60},
            "Sedang": {"min": 1, "max": 50, "soal": 15, "time": 90},
            "Sulit": {"min": 1, "max": 100, "soal": 20, "time": 120}
        }
        
        # Load high scores
        self.load_high_scores()
        
        # Setup GUI
        self.setup_gui()
        
        # Show start screen
        self.show_start_screen()
        
    def setup_gui(self):
        """Setup all GUI components"""
        # Title
        title_font = font.Font(family="Arial", size=24, weight="bold")
        self.title_label = tk.Label(
            self.root, 
            text="🎮 Game Penjumlahan 🎮", 
            font=title_font,
            bg='#FFE4B5',
            fg='#FF6347'
        )
        self.title_label.pack(pady=20)
        
        # Score display
        score_font = font.Font(family="Arial", size=16)
        self.score_label = tk.Label(
            self.root,
            text=f"Skor: {self.score}/100",
            font=score_font,
            bg='#FFE4B5',
            fg='#228B22'
        )
        self.score_label.pack(pady=5)
        
        # Timer display
        self.timer_label = tk.Label(
            self.root,
            text=f"Waktu: {self.time_left} detik",
            font=score_font,
            bg='#FFE4B5',
            fg='#FF4500'
        )
        self.timer_label.pack(pady=5)
        
        # Question display
        question_font = font.Font(family="Arial", size=20, weight="bold")
        self.question_label = tk.Label(
            self.root,
            text="",
            font=question_font,
            bg='#FFFFFF',
            fg='#000080',
            width=20,
            height=2,
            relief=tk.RAISED,
            bd=3
        )
        self.question_label.pack(pady=20)
        
        # Answer input
        self.answer_entry = tk.Entry(
            self.root,
            font=font.Font(family="Arial", size=18),
            width=10,
            justify='center'
        )
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # Submit button
        self.submit_button = tk.Button(
            self.root,
            text="Jawab!",
            font=font.Font(family="Arial", size=14, weight="bold"),
            bg='#32CD32',
            fg='white',
            width=10,
            height=2,
            command=self.check_answer
        )
        self.submit_button.pack(pady=10)
        
        # Feedback label
        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=font.Font(family="Arial", size=14),
            bg='#FFE4B5',
            fg='#000000'
        )
        self.feedback_label.pack(pady=10)
        
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg='#FFE4B5')
        control_frame.pack(pady=20)
        
        # Level buttons
        button_font = font.Font(family="Arial", size=12)
        tk.Button(
            control_frame,
            text="Mudah",
            font=button_font,
            bg='#87CEEB',
            width=8,
            command=lambda: self.start_game("Mudah")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame,
            text="Sedang",
            font=button_font,
            bg='#FFD700',
            width=8,
            command=lambda: self.start_game("Sedang")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            control_frame,
            text="Sulit",
            font=button_font,
            bg='#FF6347',
            width=8,
            command=lambda: self.start_game("Sulit")
        ).pack(side=tk.LEFT, padx=5)
        
        # Pause/Resume button
        self.pause_button = tk.Button(
            control_frame,
            text="Pause",
            font=button_font,
            bg='#FFA500',
            width=8,
            command=self.toggle_pause
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        # High score button
        tk.Button(
            control_frame,
            text="High Score",
            font=button_font,
            bg='#9370DB',
            width=10,
            command=self.show_high_scores
        ).pack(side=tk.LEFT, padx=5)
        
    def show_start_screen(self):
        """Show start screen with instructions"""
        self.question_label.config(text="Pilih Level untuk Mulai!")
        self.feedback_label.config(text="Jawab soal penjumlahan secepat mungkin! 🎯")
        self.submit_button.config(state='disabled')
        self.answer_entry.config(state='disabled')
        
    def start_game(self, level):
        """Start new game with selected level"""
        self.current_level = level
        config = self.level_config[level]
        self.score = 0
        self.soal_count = 0
        self.max_soal = config["soal"]
        self.time_left = config["time"]
        self.timer_running = True
        
        # Update displays
        self.update_score_display()
        self.update_timer_display()
        
        # Enable controls
        self.submit_button.config(state='normal')
        self.answer_entry.config(state='normal')
        self.pause_button.config(state='normal')
        
        # Generate first question
        self.generate_question()
        
        # Start timer
        self.update_timer()
        
        # Focus on answer entry
        self.answer_entry.focus()
        
    def generate_question(self):
        """Generate random addition question based on level"""
        config = self.level_config[self.current_level]
        a = random.randint(config["min"], config["max"])
        b = random.randint(config["min"], config["max"])
        self.current_answer = a + b
        
        self.question_label.config(text=f"{a} + {b} = ?")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        
    def check_answer(self):
        """Check user's answer and update score"""
        if not self.timer_running or self.soal_count >= self.max_soal:
            return
            
        try:
            user_answer = int(self.answer_entry.get())
            self.soal_count += 1
            
            if user_answer == self.current_answer:
                self.score += 5
                self.feedback_label.config(text="✅ Benar! Hebat! 🎉", fg='#32CD32')
                self.animate_feedback(True)
            else:
                self.score = max(0, self.score - 2)
                self.feedback_label.config(text=f"❌ Salah! Jawabannya {self.current_answer}", fg='#FF0000')
                self.animate_feedback(False)
                
            self.update_score_display()
            
            # Check if game should end
            if self.soal_count >= self.max_soal:
                self.end_game()
            else:
                # Generate next question after delay
                self.root.after(1500, self.generate_question)
                
        except ValueError:
            self.feedback_label.config(text="⚠️ Masukkan angka!", fg='#FFA500')
            
    def update_timer(self):
        """Update countdown timer"""
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.update_timer_display()
            
            # Check if time is up
            if self.time_left <= 0:
                self.end_game()
            else:
                # Add bonus time points
                if self.time_left % 10 == 0 and self.time_left > 0:
                    self.score = min(100, self.score + 1)
                    self.update_score_display()
                    
                # Continue timer
                self.root.after(1000, self.update_timer)
                
    def update_score_display(self):
        """Update score display"""
        self.score_label.config(text=f"Skor: {self.score}/100")
        
    def update_timer_display(self):
        """Update timer display"""
        color = '#FF4500' if self.time_left <= 10 else '#FF4500'
        self.timer_label.config(text=f"Waktu: {self.time_left} detik", fg=color)
        
    def toggle_pause(self):
        """Toggle pause/resume game"""
        if self.timer_running:
            self.timer_running = False
            self.pause_button.config(text="Resume", bg='#32CD32')
            self.submit_button.config(state='disabled')
            self.answer_entry.config(state='disabled')
            self.feedback_label.config(text="⏸️ Game Dijeda", fg='#FFA500')
        else:
            self.timer_running = True
            self.pause_button.config(text="Pause", bg='#FFA500')
            self.submit_button.config(state='normal')
            self.answer_entry.config(state='normal')
            self.feedback_label.config(text="")
            self.answer_entry.focus()
            self.update_timer()
            
    def animate_feedback(self, is_correct):
        """Animate feedback for correct/incorrect answer"""
        original_bg = self.question_label.cget('bg')
        color = '#90EE90' if is_correct else '#FFB6C1'
        
        self.question_label.config(bg=color)
        self.root.after(500, lambda: self.question_label.config(bg='#FFFFFF'))
        
    def end_game(self):
        """End game and show results"""
        self.timer_running = False
        self.submit_button.config(state='disabled')
        self.answer_entry.config(state='disabled')
        self.pause_button.config(state='disabled')
        
        # Save high score
        self.save_high_score()
        
        # Show game over message
        grade = self.get_grade(self.score)
        message = f"""
🎮 GAME SELESAI! 🎮

Skor Akhir: {self.score}/100
Grade: {grade}
Soal Dijawab: {self.soal_count}/{self.max_soal}

{"🏆 LUAR BIASA!" if self.score >= 90 else "👍 Bagus!" if self.score >= 70 else "💪 Terus berlatih!"}
        """
        
        messagebox.showinfo("Game Selesai!", message)
        
        # Reset for new game
        self.show_start_screen()
        
    def get_grade(self, score):
        """Get grade based on score"""
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "E"
            
    def save_high_score(self):
        """Save high score to file"""
        try:
            if self.current_level not in self.high_scores:
                self.high_scores[self.current_level] = []
                
            self.high_scores[self.current_level].append({
                "score": self.score,
                "date": time.strftime("%Y-%m-%d %H:%M:%S"),
                "grade": self.get_grade(self.score)
            })
            
            # Keep only top 10 scores per level
            self.high_scores[self.current_level].sort(
                key=lambda x: x["score"], reverse=True
            )
            self.high_scores[self.current_level] = self.high_scores[self.current_level][:10]
            
            with open('game_penjumlahan.json', 'w') as f:
                json.dump(self.high_scores, f, indent=2)
                
        except Exception as e:
            print(f"Error saving high score: {e}")
            
    def load_high_scores(self):
        """Load high scores from file"""
        try:
            if os.path.exists('game_penjumlahan.json'):
                with open('game_penjumlahan.json', 'r') as f:
                    self.high_scores = json.load(f)
        except Exception as e:
            print(f"Error loading high scores: {e}")
            self.high_scores = {}
            
    def show_high_scores(self):
        """Show high scores dialog"""
        message = "🏆 HIGH SCORE 🏆\n\n"
        
        for level in ["Mudah", "Sedang", "Sulit"]:
            message += f"--- {level} ---\n"
            if level in self.high_scores and self.high_scores[level]:
                for i, score_data in enumerate(self.high_scores[level][:5], 1):
                    message += f"{i}. {score_data['score']} - {score_data['grade']} - {score_data['date'][:10]}\n"
            else:
                message += "Belum ada skor\n"
            message += "\n"
            
        messagebox.showinfo("High Scores", message)
        
    def run(self):
        """Run the game"""
        self.root.mainloop()

# Run the game
if __name__ == "__main__":
    game = GamePenjumlahan()
    game.run()
