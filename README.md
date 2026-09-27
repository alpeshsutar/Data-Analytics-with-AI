# Student Performance Analytics

## Overview
This project performs exploratory data analysis (EDA) on the **Students Performance in Exams** dataset from Kaggle. The dataset contains 1,000 student records and 8 original columns covering gender, race/ethnicity, parental education, lunch type, test preparation, and math, reading, and writing scores.

Source: Kaggle — https://www.kaggle.com/spscientist/students-performance-in-exams

## Objectives
- Inspect and clean the dataset.
- Check missing values and duplicate records.
- Calculate total and average scores.
- Create performance categories.
- Compare performance across gender, lunch type, parental education, and test preparation.
- Visualize distributions and relationships between subjects.
- Generate a cleaned dataset and chart outputs.

## Project Structure
```text
Student_Performance_Analytics/
├── data/
│   └── StudentsPerformance.csv
├── outputs/
│   ├── cleaned_student_performance.csv
│   └── generated charts
├── main.py
├── requirements.txt
├── README.md
└── PROJECT_REPORT.md
```

## Dataset
The Kaggle dataset has 1,000 rows and 8 columns:
- gender
- race/ethnicity
- parental level of education
- lunch
- test preparation course
- math score
- reading score
- writing score

## Setup
1. Download `StudentsPerformance.csv` from Kaggle.
2. Put it inside the `data` folder.
3. Open the project in VS Code.
4. Create and activate a virtual environment if desired.
5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run:

```bash
python main.py
```

## Outputs
The program creates:
- `cleaned_student_performance.csv`
- average-score distribution
- gender comparison
- test-preparation comparison
- parental-education comparison
- score-distribution box plot
- reading vs writing scatter plot
- correlation heatmap

## Important interpretation note
This is an observational educational dataset. Relationships in the data should be interpreted as associations, not proof that one factor causes another. The `lunch` variable should not automatically be treated as a direct measure of household income.

## License / Dataset attribution
Kaggle currently lists the dataset's license as **Unknown**, so verify the current Kaggle data-card terms before redistributing the CSV itself. The project code is provided separately for educational use.
