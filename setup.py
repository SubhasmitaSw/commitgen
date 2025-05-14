from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="commitgen",
    version="1.0.0",
    description="AI Git Commit Message Generator (Powered by Relax AI)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Subhasmita Swain",
    author_email="subhasmitaofc@gmail.com",
    url="https://github.com/SubhasmitaSw/commitgen",
    py_modules=["cli"],
    install_requires=["python-dotenv", "requests"],
    entry_points={
        "console_scripts": ["commitgen=cli:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)