# Customer Segmentation Streamlit App

## Overview
This is a minimalist, interactive Streamlit app for customer segmentation using K-Means clustering.  
Upload your customer data (CSV or XLSX), select numeric features, choose the number of segments, and visualize your customer groups with interactive graphs.  
You can also download the segmented data for further analysis.

---

## Features
- Upload CSV or XLSX customer data
- Select numeric features for clustering
- Choose number of segments (clusters)
- Run K-Means clustering
- Visualize results with:
  - Pairplot (scatter matrix)
  - Bar chart of segment counts
  - 2D or 3D scatter plot of segments
- Download segmented data as CSV
- Minimal, clean interface with Lottie animation

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/my-python-app.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd my-python-app
   ```
3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage

To run the application, execute:
```sh
streamlit run app.py
```

---

## How It Works

1. **Upload your data:**  
   Upload a CSV or XLSX file with at least two numeric columns (e.g., Age, Income).

2. **Select features:**  
   Choose which numeric columns to use for clustering.

3. **Choose number of clusters:**  
   Select how many customer segments you want to find.

4. **Run segmentation:**  
   The app applies K-Means clustering to group similar customers.

5. **Visualize and download:**  
   View interactive graphs of your segments and download the results.

---

## Example Data Format

```csv
CustomerID,Age,Income
1,25,50000
2,32,60000
3,40,80000
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file
