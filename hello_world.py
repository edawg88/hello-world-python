#!/usr/bin/env python3
"""
Hello World Python Script
A simple demonstration of Python basics
Author: Eric Jian
"""

def main():
    """Main function that prints Hello World message"""
    # Interactive greeting
    try:
        user_name = input("What's your name? ")
        if not user_name.strip():
            user_name = "Anonymous Programmer"
    except (EOFError, KeyboardInterrupt):
        user_name = "Eric"  # Default fallback
    
    greeting = f"Hello, World! Welcome to Python programming, {user_name}!"
    
    print("\n" + "=" * 60)
    print(f"🐍 {greeting} 🐍")
    print("=" * 60)
    
    # Demonstrate some basic Python features
    languages = ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "TypeScript"]
    print("\n🚀 Popular programming languages:")
    for i, lang in enumerate(languages, 1):
        emoji = "🐍" if lang == "Python" else "💻"
        print(f"  {i}. {emoji} {lang}")
    
    # Show Python version
    import sys
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"\n🔧 You're running Python {python_version}")
    
    # Fun fact
    import datetime
    current_year = datetime.datetime.now().year
    print(f"\n🎉 Fun fact: Python was first released in 1991")
    print(f"    That makes Python {current_year - 1991} years old!")
    
    print(f"\n✨ Happy coding, {user_name}! Keep learning and building amazing things! ✨")

if __name__ == "__main__":
    main()
