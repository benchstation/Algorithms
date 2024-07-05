# Setup Instructions

<details>

<summary style="font-size: 18px; font-weight: bold">Python</summary>

To run the Python scripts, I recommend creating a **virtual environment**. A virtual environment provides isolation, allowing you to manage project-specific dependencies independently of the global Python installation. All required dependencies are listed in `requirements.txt`.

1. **Create a Virtual Environment**

    ```bash
    python -m venv .venv
    ```

2. **Activate the Virtual Environment**
    - On Windows

        ```bash
        .venv\Scripts\activate
        ```
    - On macOS and Linux

        ```bash
        source .venv/bin/activate
        ```

3. **Configure VS Code to Use the Virtual Environment**

    - Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
    - Type Python: Select Interpreter.
    - Choose the interpreter from the `.venv` folder.

4. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the project**:
    ```bash
    python [script_name].py
    ```

</details>