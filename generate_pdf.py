import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Define the target directory from your config setup
OUTPUT_DIR = os.path.join("data", "pdfs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 10 Detailed Chapter Outlines with Structured Content
chapters = [
    {
        "filename": "Chapter_01_Introduction_to_Python.pdf",
        "title": "Chapter 1: Introduction to Python",
        "content": """Python is a high-level, interpreted, interactive, and object-oriented scripting language. 
        Created by Guido van Rossum in the late 1980s, Python's design philosophy emphasizes code readability with the use of significant indentation.
        
        Key Features of Python:
        1. Easy to Learn and Read: Python has straightforward, English-like syntax that makes it easy for beginners to grasp.
        2. Interpreted Language: Code is executed line by line, making debugging straightforward and interactive programming possible.
        3. Dynamically Typed: You do not need to explicitly declare variable data types prior to assignment; Python determines types automatically at runtime.
        4. Portable and Cross-Platform: Python scripts run seamlessly across Windows, macOS, Linux, and Unix environments.
        5. Extensive Standard Libraries and Packages: Support for third-party tools via pip expands its capabilities into data science, web development, and AI."""
    },
    {
        "filename": "Chapter_02_Variables_and_Data_Types.pdf",
        "title": "Chapter 2: Variables & Data Types",
        "content": """Variables are containers for storing data values. In Python, a variable is created the moment you first assign a value to it using the assignment operator (=).
        
        Standard Built-in Data Types in Python:
        - Numeric Types: int (whole numbers like 42), float (decimal numbers like 3.14).
        - Text Sequence Type: str (strings enclosed in single or double quotes, e.g., 'Hello Python').
        - Boolean Type: bool (represents truth values True or False).
        - Type Conversion: You can explicitly convert between types using built-in constructors like int(), float(), and str().
        
        Example variable assignments:
        x = 10          # Integer
        pi = 3.14159    # Float
        name = "AI Bot" # String
        is_active = True# Boolean"""
    },
    {
        "filename": "Chapter_03_Operators_and_Expressions.pdf",
        "title": "Chapter 3: Operators & Expressions",
        "content": """Operators are special symbols used to carry out arithmetic and logical computations on variables and values.
        
        Categories of Python Operators:
        1. Arithmetic Operators: Used for mathematical calculations including addition (+), subtraction (-), multiplication (*), division (/), floor division (//), exponentiation (**), and modulus (%).
        2. Comparison Operators: Used to compare values, returning a boolean result. Examples include equal to (==), not equal to (!=), greater than (>), and less than or equal to (<=).
        3. Logical Operators: Combine conditional statements using and, or, and not.
        4. Assignment Operators: Modify variable values using shorthand notations like +=, -=, and *=."""
    },
    {
        "filename": "Chapter_04_Conditional_Statements.pdf",
        "title": "Chapter 4: Conditional Statements",
        "content": """Conditional statements control the execution flow of a program based on whether specific boolean expressions evaluate to True or False.
        
        Primary Control Structures:
        - if statement: Executes a block of code only if the condition is true.
        - elif (Else If) clause: Evaluates subsequent expressions if preceding conditions fail.
        - else statement: Catches all remaining cases when prior conditions evaluate to false.
        
        Syntax structure relies entirely on proper colon usage and consistent code block indentation."""
    },
    {
        "filename": "Chapter_05_Loops_and_Iteration.pdf",
        "title": "Chapter 5: Loops & Iteration",
        "content": """Loops are programming structures designed to repeat a block of code multiple times until a terminating condition is met.
        
        Types of Loops:
        1. for loop: Used for iterating over a sequence such as a list, tuple, dictionary, set, or string range.
        2. while loop: Repeatedly executes a statement block as long as a designated test expression remains true.
        
        Control Keywords within Loops:
        - break: Immediately exits the enclosing loop.
        - continue: Skips the current iteration and advances directly to the next loop cycle."""
    },
    {
        "filename": "Chapter_06_Functions_and_Scope.pdf",
        "title": "Chapter 6: Functions & Scope",
        "content": """A function is a reusable, self-contained block of code organized to perform a specific related action, defined using the def keyword.
        
        Key Concepts:
        - Parameters and Arguments: Inputs passed into functions for processing.
        - Return Values: Outputs sent back using the return statement.
        - Variable Scope: Defines where a variable is accessible within your program.
          * Local Scope: Variables created inside a function body.
          * Global Scope: Variables declared outside any function body, accessible globally."""
    },
    {
        "filename": "Chapter_07_Lists_and_Tuples.pdf",
        "title": "Chapter 7: Lists & Tuples",
        "content": """Python provides compound data structures to store collections of items within a single variable.
        
        1. Lists: 
           - Defined using square brackets [].
           - Mutable (elements can be modified, appended, or removed after creation).
           - Supports indexing, slicing, and methods like append(), pop(), and sort().
        
        2. Tuples:
           - Defined using parentheses ().
           - Immutable (cannot be changed, added to, or altered once instantiated).
           - Faster performance than lists due to fixed memory allocation."""
    },
    {
        "filename": "Chapter_08_Dictionaries_and_Sets.pdf",
        "title": "Chapter 8: Dictionaries & Sets",
        "content": """Advanced collections allow efficient data lookup, key-value association, and mathematical set operations.
        
        1. Dictionaries:
           - Store data in key-value pairs using curly braces {}.
           - Keys must be unique and hashable; values can be of any data type.
           - Provides fast lookups using keys via methods like keys(), values(), and items().
        
        2. Sets:
           - Unordered collections of unique elements.
           - Automatically eliminates duplicate values.
           - Supports mathematical operations like union, intersection, and difference."""
    },
    {
        "filename": "Chapter_09_Strings_and_File_Handling.pdf",
        "title": "Chapter 9: Strings & File Handling",
        "content": """String manipulation and external file persistence are core foundational tasks in Python application development.
        
        1. String Operations:
           - Strings support slicing, concatenation, formatting via f-strings, and utility methods like split(), join(), and replace().
        
        2. File Handling:
           - Built-in open() function manages reading and writing external files.
           - File Modes: 'r' for reading, 'w' for writing, and 'a' for appending data.
           - Context managers (with statements) ensure files are cleanly and automatically closed after execution."""
    },
    {
        "filename": "Chapter_10_Exception_Handling_and_OOP.pdf",
        "title": "Chapter 10: Exception Handling & OOP",
        "content": """Robust applications require error handling and structured modular design paradigms.
        
        1. Exception Handling:
           - Uses try, except, else, and finally blocks to catch runtime errors gracefully without crashing applications.
           - Prevents issues like ZeroDivisionError or FileNotFoundError from disrupting user flows.
        
        2. Object-Oriented Programming (OOP):
           - Centered around classes and objects.
           - Core principles include encapsulation, inheritance, polymorphism, and abstraction.
           - The __init__() constructor method initializes object attributes upon instantiation."""
    }
]

def build_pdf(file_path, title, text_content):
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor='#1e3a8a',
        spaceAfter=14
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        textColor='#334155',
        spaceAfter=10
    )
    
    story = []
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 10))
    
    for paragraph in text_content.strip().split("\n\n"):
        clean_p = paragraph.strip().replace("\n", " ")
        story.append(Paragraph(clean_p, body_style))
        story.append(Spacer(1, 6))
        
    doc.build(story)

if __name__ == "__main__":
    print("Generating 10 Python Study Assistant PDFs...")
    for ch in chapters:
        path = os.path.join(OUTPUT_DIR, ch["filename"])
        build_pdf(path, ch["title"], ch["content"])
        print(f"Created: {ch['filename']}")
    print("All 10 PDFs successfully created inside data/pdfs/!")