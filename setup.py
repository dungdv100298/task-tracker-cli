from setuptools import setup

setup(
    name="tracker",
    version="1.0.0",
    description="A CLI application to manage tasks.",
    author="DaoDung",
    author_email="dungdv100298@gmail.com",
    url="https://github.com/dungdv100298/task-tracker-cli",
    py_modules=["tracker"],
    entry_points={
        "console_scripts": [
            "tracker=tracker:main",
        ],
    },
    install_requires=[
        "tabulate",
    ],
    tests_require=[
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)