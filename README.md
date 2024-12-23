# Autism_Prediction
 "Autism prediction ML model leveraging classification algorithms to identify autism spectrum disorder traits from behavioral data."
<img src="https://github.com/rpjinu/Autism_Prediction/blob/main/autism_prediction_image.png" width=800>

# Autism Prediction using Machine Learning

This project aims to predict Autism Spectrum Disorder (ASD) traits from behavioral data using advanced classification algorithms. By providing a reliable tool for early identification, this project can aid in timely intervention and support for individuals and their families.

## Project Description

Autism Spectrum Disorder (ASD) is a complex developmental condition affecting communication, behavior, and social interaction. Early detection is crucial for improving the quality of life for individuals with ASD. This project utilizes machine learning techniques to analyze behavioral datasets and classify whether an individual exhibits traits of autism.

## Key Features

*   Uses supervised learning algorithms for classification.
*   Handles behavioral and demographic data.
*   Incorporates data preprocessing and feature engineering for improved accuracy.
*   Visualizes data trends and feature importance.
*   Interactive web interface using Streamlit.

## Workflow

1.  **Data Collection:**
    *   Behavioral data collected from surveys and assessments.
    *   Features include responses to screening questions, demographic details, and behavioral patterns.

2.  **Data Preprocessing:**
    *   Handling missing values and outliers.
    *   Encoding categorical variables.
    *   Normalizing numerical features for consistency.

3.  **Exploratory Data Analysis (EDA):**
    *   Visualizing feature distributions.
    *   Identifying correlations and trends.
    *   Analyzing class imbalances.

4.  **Model Training:**
    *   Testing multiple classification models (e.g., Logistic Regression, Random Forest, Support Vector Machines).
    *   Implementing hyperparameter tuning for optimal performance.

5.  **Evaluation:**
    *   Using metrics like accuracy, precision, recall, and F1-score.
    *   Cross-validation to ensure robustness.

6.  **Prediction:**
    *   Deploying the best-performing model to predict autism traits on new data.

7.  **Deployment:**
    *   Creating and deploying an API using Streamlit for an interactive web interface.

## Technologies Used

*   **Programming Language:** Python
*   **Libraries:**
    *   Pandas
    *   NumPy
    *   Scikit-learn
    *   Matplotlib
    *   Seaborn
    *   Streamlit
*   **Machine Learning Algorithms:**
    *   Logistic Regression
    *   Random Forest
    *   SVM
    *   Other relevant algorithms
*   **Deployment:** Streamlit

## Installation (Optional - For running locally)

1.  Clone the repository:

    ```bash
    git clone [https://github.com/rpjinu/YOUR_REPOSITORY.git](https://github.com/rpjinu/YOUR_REPOSITORY.git)
    ```

2.  Navigate to the project directory:

    ```bash
    cd Autism-Prediction
    ```

3.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

4.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage (For running the Streamlit app locally)

1.  Navigate to the project directory (if not already there) and activate the virtual environment.

2.  Run the Streamlit app:

    ```bash
    streamlit run app.py # Replace app.py with your main Streamlit file if different
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[Choose a license](https://choosealicense.com/) (e.g., MIT License)
