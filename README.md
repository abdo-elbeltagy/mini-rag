# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

## Setting Up the Virtual Environment

To set up the virtual environment and install the required dependencies, follow these steps:

1. **Create a Virtual Environment**

   Run the following command to create a virtual environment named `mini-rag`:

   ```zsh
   python3 -m venv mini-rag
   ```

2. **Activate the Virtual Environment**

   - On macOS/Linux:

     ```zsh
     source mini-rag/bin/activate
     ```

   - On Windows:

     ```cmd
     mini-rag\Scripts\activate
     ```

3. **Install Dependencies**

   Once the virtual environment is activated, install the required dependencies from `requirement.txt`:

   ```zsh
   pip install -r requirement.txt
   ```

4. **Verify Installation**

   Ensure all dependencies are installed correctly by checking the installed packages:

   ```zsh
   pip list
   ```

You're now ready to run the application!

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.
