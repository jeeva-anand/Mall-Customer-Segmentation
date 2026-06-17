# import streamlit as st
# import pandas as pd
# from src.utils import load_model

# st.title("Mall Customer Segmentation App")

# model = load_model("models/kmeans_model.pkl")

# st.write("Upload customer data or use sample dataset")

# uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write(df.head())

#     X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
#     labels = model.predict(X)

#     df['Cluster'] = labels

#     st.write("### Clustered Data")
#     st.write(df)

#     st.bar_chart(df['Cluster'].value_counts())


from src.utils import load_model
import plotly.express as px
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Mall Customer Intelligence",
    page_icon="",
    layout="wide"
)


st.title(" Mall Customer Dashboard")
st.caption(
    "Customer segmentation using K-Means Clustering"
)


st.sidebar.header("Customer Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload Customer Dataset",
    type=["csv"]
)

model = load_model("models/kmeans_model.pkl")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    X = df[
        [
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]

    df["Cluster"] = model.predict(X)

    

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Customers",
        len(df)
    )

    col2.metric(
        "Average Income",
        round(df["Annual Income (k$)"].mean(), 2)
    )

    col3.metric(
        "Average Spending Score",
        round(df["Spending Score (1-100)"].mean(), 2)
    )

    st.divider()



    fig = px.scatter(
        df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color=df["Cluster"].astype(str),
        hover_data=["CustomerID", "Age"],
        title="Customer Segments"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        cluster_counts = (
            df["Cluster"]
            .value_counts()
            .sort_index()
        )

        st.subheader("Cluster Distribution")

        st.bar_chart(cluster_counts)

    with col2:

        st.subheader("Customer Preview")

        st.dataframe(df)

    st.divider()

    st.subheader(" Business Insights")

    st.success(
        """
        • Premium customers can be targeted with loyalty programs.

        • Low-income high-spending customers respond well to promotions.

        • High-income low-spending customers represent untapped potential.

        • Segment-specific marketing can improve campaign ROI.
        """
    )

else:

    st.info(
        "Upload a Mall Customers CSV file to begin analysis."
    )

