<h1 align = "center">Clustering Countries with DBSCAN 🌍</h1>

<p align = "center" >An exploratory data science project that uses the <b>DBSCAN (Density-Based Spatial Clustering of Applications with Noise)</b> algorithm to group countries based on socio-economic and development indicators. 
This project delves into the fascinating world of global economics by applying machine learning to uncover hidden patterns among nations. By analyzing a dataset of various countries, we can identify clusters of nations that share similar characteristics, providing valuable insights into global development, economic health, and more.</p>

<hr>
<h2>✨ About The Project</h2>
<p>The primary goal of this repository is to demonstrate a practical application of the DBSCAN clustering algorithm. Unlike traditional clustering methods like K-Means, DBSCAN does not require the number of clusters to be specified beforehand and can find arbitrarily shaped clusters while also identifying noise points (outliers).</p>

<b>This project walks through the entire data science pipeline:</b>
<li>Data Loading & Exploration: Importing the country dataset and performing initial exploratory data analysis (EDA).</li>
<li>Data Preprocessing: Cleaning the data and scaling the features to prepare them for the clustering algorithm.</li>
<li>Model Implementation: Applying the Scikit-learn implementation of DBSCAN to find dense regions of data points.</li>
<li>Visualization: Plotting the results on a world map to create an intuitive and easy-to-understand visualization of the country clusters.</li>
<li>Analysis & Interpretation: Drawing conclusions from the identified clusters and outliers.</li>

<h2>🛠️ Built With</h2>
<b>This project is built with Python and relies on the power of these amazing open-source libraries:</b>
<li><code>Pandas</code> For data manipulation and analysis.</li>
<li><code>NumPy</code> For fundamental numerical computations.</li>
<li><code>Scikit-learn</code> For implementing the DBSCAN algorithm and preprocessing.</li>
<li><code>Matplotlib & Seaborn</code> For creating insightful visualizations.</li>
<li><code>Jupyter Notebook</code> For interactive development and analysis.</li>

<h2>🚀 Getting Started</h2>
<p>To get a local copy up and running, follow these simple steps.</p>
<h3>Prerequisites</h3>
<p>Make sure you have Python (version 3.6 or newer) and <code>pip</code> installed on your system.</p>

<h3>Installation</h3>
<ul>Clone the repository to your local machine:</ul>

```
git clone https://github.com/RafdhiFatoni/DBSCAN-Country-Clustering.git</pre>
```

<ul>Navigate to the project directory:</ul>

```
cd DBSCAN-Country-Clustering
```

<ul>Install the required packages. It's recommended to do this in a virtual environment.</ul>

```
pip install pandas numpy scikit-learn matplotlib seaborn jupyterlab
```

<h2>Usage</h2>
<p>The core of this project is within the Jupyter Notebook <code>.ipynb</code> file.</p>
<ul>Launch Jupyter Lab or Notebook:</ul>

```
jupyter lab
```
or

```
jupyter notebook
```
<ul>Open the notebook file from the Jupyter interface.</ul>
<ul>Run the cells sequentially by pressing <code>Shift + Enter</code>. Follow the narrative and code to see the step-by-step process of clustering the countries.</ul>

<p>The notebook is structured to be self-explanatory, guiding you from data loading to the final visualization of the clusters.</p>

<h2>📊 Results and Analysis</h2>
<p>The DBSCAN algorithm successfully identified several distinct clusters of countries based on the provided features. The final output is a world map where countries are color-coded according to their cluster assignment.</p>

<img width="844" height="545" alt="DBSCAN Clustering" src="https://github.com/user-attachments/assets/461933a5-7a71-433f-92f8-02bb211c46fd" />

<p>The analysis reveals interesting groupings, such as clusters of highly developed nations, developing economies, and outlier countries that don't fit into any specific group. These results can serve as a starting point for deeper socio-economic analysis.</p>

<h2>🤝 Contributing</h2>
<p>Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are <b>greatly appreciated.</b></p>

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

<h2>📄 License</h2>
<p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>





