#!/usr/bin/env python3
"""
Hello World Python Script
A simple demonstration of Python basics
Author: Eric Jian
"""

def main():
    """Main function that prints Hello World message"""
    name = "Eric"
    greeting = f"Hello, World! Welcome to Python programming, {name}!"
    
    print("=" * 50)
    print(greeting)
    print("=" * 50)
    
    # Demonstrate some basic Python features
    languages = ["Python", "JavaScript", "Java", "C++", "Go"]
    print("\nSome popular programming languages:")
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")
    
    print(f"\nPython version info available via 'python3 --version'")
    print("Happy coding! 🐍")

if __name__ == "__main__":
    main()
