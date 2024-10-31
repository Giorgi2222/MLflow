## Getting Started

Follow the instructions below to set up the project on your local machine.

### Prerequisites

- Python 3.11 must be installed. You can download it from [here](https://www.python.org/downloads/).

### Creating a Virtual Environment

1. Ensure that Python is installed by running:
   ```bash
   py --version
   
2. Create Virtual Environment:
   ```bash
   py -3.11 -m venv venv

3. Activate the Virtual Environment:
   ```bash
   .\venv\Scripts\activate
4. Once the virtual environment is activated, install the necessary dependencies:
   ```bash
   pip install -r requirements.txt

### Option 1: Launch Jupyter Notebook

To launch the Jupyter notebook and run `tracking_quickstart.ipynb`, use the following command:

```bash
jupyter notebook
```

- Open the `tracking_quickstart.ipynb` file in your browser.
- Run the cells to follow along with the model training and saving process.

---

### Option 2: Convert `.ipynb` to `.py` and Run as Python Script

If you prefer, you can convert the Jupyter notebook file (`tracking_quickstart.ipynb`) to a Python script and run it directly:

1. **Convert the notebook to a Python script** using the following command:

    ```bash
    ```

    This will generate a `tracking_quickstart.py` file in the same directory.

2. **Run the Python script**:

    ```bash
    python tracking_quickstart.py
    ```

This method allows you to execute the code directly without the need for the notebook interface.

---
### Deploying the model
#### Once you save the model on MLflow tracking server and download it, you can deploy it.
   ```bash
   mlflow models serve -m ./downloaded_model -p 8000 --no-conda
```
#### You can test the deployed model by running test_deployed.py:
   ```bash
   python test_deployed.py
