"""
MAIN RUNNER - Complete OOP Learning Program
============================================
Run all OOP examples in sequence or select specific ones.
"""

import os
import sys
from pathlib import Path

# Get the directory containing this script
script_dir = Path(__file__).parent

# List of all OOP concept files
oop_files = [
    ("01_classes_and_objects.py", "Classes and Objects"),
    ("02_inheritance.py", "Inheritance"),
    ("03_encapsulation.py", "Encapsulation"),
    ("04_polymorphism.py", "Polymorphism"),
    ("05_abstraction.py", "Abstraction"),
    ("06_advanced_oop.py", "Advanced OOP Features"),
]


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f"  {title}".center(70))
    print("=" * 70 + "\n")


def print_menu():
    """Display main menu"""
    print_header("OOP IN PYTHON - COMPLETE LEARNING GUIDE")
    print("Select an option:")
    print()
    for i, (_, title) in enumerate(oop_files, 1):
        print(f"  {i}. {title}")
    print(f"  {len(oop_files) + 1}. Run ALL Examples")
    print(f"  0. Exit")
    print()


def run_file(filename):
    """Run a Python file and handle errors"""
    filepath = script_dir / filename
    
    if not filepath.exists():
        print(f"❌ Error: File not found - {filename}")
        return False
    
    try:
        with open(filepath, 'r') as f:
            code = f.read()
        
        # Execute the file
        exec(code)
        return True
    except Exception as e:
        print(f"❌ Error running {filename}: {e}")
        return False


def run_all():
    """Run all OOP example files"""
    print("\n" + "=" * 70)
    print("RUNNING ALL OOP EXAMPLES".center(70))
    print("=" * 70)
    
    successful = 0
    failed = 0
    
    for i, (filename, title) in enumerate(oop_files, 1):
        print(f"\n{'[' + str(i) + '/' + str(len(oop_files)) + ']'} Running: {title}")
        print("-" * 70)
        
        if run_file(filename):
            successful += 1
            print(f"✓ {title} - Completed")
        else:
            failed += 1
            print(f"✗ {title} - Failed")
        
        # Pause between files for readability
        if i < len(oop_files):
            input("\nPress Enter to continue to next example...")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY".center(70))
    print("=" * 70)
    print(f"✓ Successful: {successful}")
    print(f"✗ Failed: {failed}")
    print(f"Total: {len(oop_files)}")


def run_single(choice):
    """Run a single file"""
    if 1 <= choice <= len(oop_files):
        filename, title = oop_files[choice - 1]
        print_header(title)
        if run_file(filename):
            print(f"\n✓ {title} completed successfully!")
        else:
            print(f"\n✗ Failed to run {title}")
    else:
        print("❌ Invalid choice!")


def show_table_of_contents():
    """Show what will be learned"""
    print_header("WHAT YOU'LL LEARN")
    
    topics = {
        "Classes & Objects": [
            "Creating classes and objects",
            "Instance and class variables",
            "Constructor and methods",
            "Static and class methods",
            "Practical examples: Car, BankAccount, Student"
        ],
        "Inheritance": [
            "Single, multi-level, and multiple inheritance",
            "Parent and child classes",
            "Method overriding with super()",
            "Method Resolution Order (MRO)",
            "Practical example: Employee hierarchy"
        ],
        "Encapsulation": [
            "Public, protected, and private variables",
            "Data hiding and security",
            "Getters and setters",
            "@property decorator",
            "Data validation through encapsulation"
        ],
        "Polymorphism": [
            "Method overriding and overloading",
            "Duck typing",
            "Operator overloading",
            "Runtime polymorphism",
            "Practical example: Payment gateway system"
        ],
        "Abstraction": [
            "Abstract base classes (ABC)",
            "Abstract methods",
            "Interface design",
            "Implementation contracts",
            "Practical example: Database operations"
        ],
        "Advanced Concepts": [
            "Static and class methods",
            "Decorators and method chaining",
            "Composition vs inheritance",
            "Singleton pattern",
            "SOLID principles"
        ]
    }
    
    for topic, details in topics.items():
        print(f"\n📚 {topic}:")
        for detail in details:
            print(f"   • {detail}")


def main():
    """Main program loop"""
    show_table_of_contents()
    
    while True:
        print()
        print_menu()
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 0:
                print("\n👋 Thank you for learning OOP! Goodbye!")
                break
            elif choice == len(oop_files) + 1:
                run_all()
            else:
                run_single(choice)
            
            input("\nPress Enter to return to menu...")
            
        except ValueError:
            print("❌ Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
        sys.exit(0)
