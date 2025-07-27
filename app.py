import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import plotly.express as px


# Minimal CSS: No background, clean look
st.markdown("""
    <style>
    body {
        min-height: 100vh;
        font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
        background: none !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #22223b 0%, #4a4e69 100%);
        color: #fff;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        border: none;
        font-size: 1rem;
        box-shadow: 0 2px 8px rgba(31,38,135,0.10);
        transition: background 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #4a4e69 0%, #22223b 100%);
        box-shadow: 0 4px 16px rgba(31,38,135,0.18);
    }
    .stDataFrame, .stTable {
        background: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Lottie Animation Loader
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_ktwnwv5m.json")
if lottie:
    st_lottie(lottie, height=100, key="logo", speed=1, loop=True, quality="high")

st.title("Customer Segmentation App")


uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview Data")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("Please upload data with at least two numeric columns for clustering.")
    else:
        features = st.multiselect("Select features for segmentation", numeric_cols, default=numeric_cols[:2])
        n_clusters = st.slider("Number of segments", min_value=2, max_value=8, value=3)

        if st.button("Run Segmentation"):
            X = df[features].dropna()
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            segments = kmeans.fit_predict(X)
            df['Segment'] = -1
            df.loc[X.index, 'Segment'] = segments

            st.success("Segmentation complete!")
            st.subheader("Segmented Data")
            st.dataframe(df)

            # Pairplot
            if len(features) >= 2:
                fig = px.scatter_matrix(
                    df,
                    dimensions=features,
                    color=df['Segment'].astype(str),
                    title="Pairplot of Customer Segments",
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig, use_container_width=True)

            # Bar chart
            seg_counts = df['Segment'].value_counts().sort_index()
            fig = px.bar(
                x=seg_counts.index.astype(str),
                y=seg_counts.values,
                labels={'x': 'Segment', 'y': 'Count'},
                title="Number of Customers in Each Segment",
                color=seg_counts.index.astype(str),
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig, use_container_width=True)

            # Pie chart
            fig = px.pie(
                df, 
                names='Segment', 
                title="Customer Segment Distribution",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig, use_container_width=True)

            # 2D or 3D scatter
            if len(features) == 2:
                fig = px.scatter(
                    df, x=features[0], y=features[1], color=df['Segment'].astype(str),
                    title="Customer Segments", color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig, use_container_width=True)
            elif len(features) == 3:
                fig = px.scatter_3d(
                    df, x=features[0], y=features[1], z=features[2], color=df['Segment'].astype(str),
                    title="Customer Segments (3D)", color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig, use_container_width=True)

            st.download_button("Download Segmented Data", df.to_csv(index=False).encode(), "segmented_customers.csv")
else:
    st.info("Awaiting CSV upload.")


st.markdown("""
### What does this app do?

This app helps you **group your customers into similar categories** using a method called K-Means clustering.

**How it works:**
1. You upload your customer data as a CSV or Excel file.
2. The app shows you a preview of your data.
3. You pick which number columns (like Age, Income, etc.) you want to use for grouping.
4. You choose how many groups you want to create.
5. The app finds customers who are similar to each other and puts them in the same group.
6. You can see the results in a table and colorful charts.
7. You can also download your data with the new group labels.

**What is K-Means clustering?**  
K-Means is a way for the computer to find patterns in your data and group similar customers together, even if you don’t tell it what the groups should be.  
This is useful for things like marketing, understanding your customers, or finding patterns in your business.

**How to use this app:**
- Upload a CSV or Excel file with at least two number columns.
- Select which columns you want to use for grouping.
- Choose how many groups you want.
- Click "Run Segmentation" to see your customer groups!

""", unsafe_allow_html=True)

st.markdown("""
---
<div style="text-align:center; color:#888; font-size:0.9em;">
    Made with using Streamlit, by Solanki Pragati
</div>
""", unsafe_allow_html=True)