# AI Git Commit Message Generator

## Overview

This CLI tool generates Git commit messages using an LLM. It analyzes staged changes and provides a suggested commit message so devs can focus on writing code instead of commit messages. It can also generate humorous commit messages for fun.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SubhasmitaSw/commitgen.git
   cd commitgen
   ```

2. **Create a `.env` File**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your Relax AI API key or replace with your preferred LLM API key.

## Installation

### Using Virtual Environment

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the Package**:
   ```bash
   pip install .
   ```

### Using `--user` Flag

1. **Install the Package**:
   ```bash
   pip install --user .
   ```

### Using Poetry (Optional)

If you have Poetry installed, you can also use it to manage dependencies.

1. **Install Poetry**:
   Follow the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installation).

2. **Install Dependencies**:
   ```bash
   poetry install
   ```

## Global Usage

1. **Stage Your Changes**:
   ```bash
   git add .
   ```

2. **Generate a Commit Message**:
   ```bash
   commitgen
   ```

3. **Review and Commit**:
   - Review the suggested commit message.
   - Confirm or edit the message to commit.

## Flags

- `--bonkers`: Go bonkers and generate a humorous commit message.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.