#!/usr/bin/env python3
from setuptools import setup, find_packages
import os
from pathlib import Path

# Define directory for example exercises
home = Path.home()
subjects_dir = home / ".vfy/subjects"
subjects_dir.mkdir(exist_ok=True, parents=True)

setup(
    name="vfy",
    version="1.0.0",
    description="Programming Exercises Verification Tool",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "vfy": ["*.txt", "*.json"],
    },
    entry_points={
        "console_scripts": [
            "vfy=vfy:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
    ],
)

# Copy example exercises
print("Setting up example exercises...")
os.system("mkdir -p ~/.vfy/subjects/level_1/ex00")
os.system("mkdir -p ~/.vfy/subjects/level_1/ex01")
os.system("mkdir -p ~/.vfy/subjects/level_1/ex02")
os.system("mkdir -p ~/.vfy/subjects/level_2/ex00")

print("Creating example exercises...")
with open(subjects_dir / "level_1/ex00/subject.txt", "w") as f:
    f.write("Exercise: Hello World\n------------------\n\nWrite a program that prints \"Hello World\" (without quotes) and ends with a newline.\n\nExample output:\nHello World")
with open(subjects_dir / "level_1/ex00/expected_output.txt", "w") as f:
    f.write("Hello World")
with open(subjects_dir / "level_1/ex00/template.c", "w") as f:
    f.write("#include <stdio.h>\n\nint main(void) {\n    // Your code here\n    \n    return 0;\n}")

with open(subjects_dir / "level_1/ex01/subject.txt", "w") as f:
    f.write("Exercise: Sum Two Numbers\n------------------\n\nWrite a program that adds two integers (42 and 27) and prints the result.\n\nExample output:\n69")
with open(subjects_dir / "level_1/ex01/expected_output.txt", "w") as f:
    f.write("69")
with open(subjects_dir / "level_1/ex01/template.c", "w") as f:
    f.write("#include <stdio.h>\n\nint main(void) {\n    // Add the numbers 42 and 27\n    // Print the result\n    \n    return 0;\n}")

with open(subjects_dir / "level_1/ex02/subject.txt", "w") as f:
    f.write("Exercise: Print 1 to 10\n------------------\n\nWrite a program that prints numbers from 1 to 10, each on a new line.\n\nExample output:\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
with open(subjects_dir / "level_1/ex02/expected_output.txt", "w") as f:
    f.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
with open(subjects_dir / "level_1/ex02/template.c", "w") as f:
    f.write("#include <stdio.h>\n\nint main(void) {\n    // Use a loop to print numbers 1 to 10\n    \n    return 0;\n}")

with open(subjects_dir / "level_2/ex00/subject.txt", "w") as f:
    f.write("Exercise: FizzBuzz\n------------------\n\nWrite a program that prints the numbers from 1 to 15.\nFor multiples of 3, print \"Fizz\" instead of the number.\nFor multiples of 5, print \"Buzz\" instead of the number.\nFor multiples of both 3 and 5, print \"FizzBuzz\".\n\nExample output:\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz")
with open(subjects_dir / "level_2/ex00/expected_output.txt", "w") as f:
    f.write("1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz")
with open(subjects_dir / "level_2/ex00/template.c", "w") as f:
    f.write("#include <stdio.h>\n\nint main(void) {\n    // Loop from 1 to 15\n    // If multiple of 3, print \"Fizz\"\n    // If multiple of 5, print \"Buzz\"\n    // If multiple of both, print \"FizzBuzz\"\n    // Otherwise print the number\n    \n    return 0;\n}") 