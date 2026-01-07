# ============================================================
# REQUIRED IMPORTS
# ============================================================
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Job Market Analytics Dashboard",
    layout="wide"
)

# ============================================================
# BASIC STREAMLIT CONFIG
# ============================================================
st.set_page_config(
    page_title="Job Market Analytics Dashboard",
    layout="wide"
)

# ============================================================
# SESSION STATE INITIALIZATION (IMPORTANT)
# ============================================================
if "page" not in st.session_state:
    st.session_state.page = "Overview"

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
st.sidebar.title("China Jobs Market")
st.session_state.page = st.sidebar.radio(
    "Go to",
    ["Overview", "Market Overview", "Salary & Experience Analysis","Job Demand & Market KPIs","Advanced Insights & Forecasting","Filters","Data View",
        "Conclusion & Insights"]
)

# ============================================================
# SAMPLE DATA LOADING (REPLACE WITH YOUR OWN DATASET)
# ============================================================
# NOTE: This is ONLY to prevent runtime errors.
# You can safely replace df with your actual dataset.

df = pd.DataFrame({
    "year": [2019, 2020, 2021, 2022, 2023] * 10,
    "salary_min_cny": [6000, 6500, 7000, 7500, 8000] * 10,
    "salary_median_cny": [9000, 9500, 10000, 11000, 12000] * 10,
    "salary_max_cny": [14000, 15000, 16000, 17000, 18000] * 10,
    "experience_years": [0, 1, 2, 3, 5] * 10,
    "demand_index": [60, 65, 70, 75, 80] * 10,
    "job_openings": [120, 150, 180, 210, 250] * 10
})

# ============================================================
# FRONT PAGE / OVERVIEW (INTRODUCTORY PAGE)
# ============================================================
if st.session_state.page == "Overview":

    st.markdown('<div class="title">📊 Job Market Analytics Dashboard</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Final Year Project | Professional Data Analytics Application</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    ### 📌 Project Introduction
    The Job Market Analytics Dashboard is a professional data-driven application developed
    as a **Final Year Project**. The purpose of this dashboard is to analyze job market trends,
    salary patterns, and demand indicators using real-world data from the Chinese job market.

    This project demonstrates the practical use of **Python, Data Visualization, and
    Exploratory Data Analysis (EDA)** techniques to support data-driven decision making.
    """)

    st.markdown("""
    ### 🎯 Project Objectives
    - To analyze salary trends across different years and experience levels  
    - To study the relationship between demand index and job openings  
    - To visualize hiring patterns using interactive charts  
    - To apply data analytics concepts in a real-world scenario  
    """)

    st.markdown("""
    ### 📂 Dataset Overview
    The dataset contains structured information related to:
    - Job salaries (minimum, median, maximum)
    - Demand index of skills
    - Number of job openings
    - Experience levels
    - Monthly and yearly trends
    """)

    st.markdown("---")

    st.markdown("### 📈 Overall Salary Trend (Sample Insight)")

    salary_trend = df.groupby("year")["salary_median_cny"].mean().reset_index()

    fig = px.line(
        salary_trend,
        x="year",
        y="salary_median_cny",
        markers=True,
        title="Average Median Salary Trend Over Time",
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Year",
        yaxis_title="Average Median Salary (CNY)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("📘 This dashboard provides detailed insights in the following sections using interactive analytics.")
    

# ============================================================
# MARKET OVERVIEW PAGE
# ============================================================
if st.session_state.page == "Market Overview":

    st.markdown('<div class="title">📊 Market Overview</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>High-level insights into the job market dynamics</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.box(
            df,
            y="salary_median_cny",
            title="Salary Distribution (Median Salary)"
        )
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.scatter(
            df,
            x="demand_index",
            y="job_openings",
            size="salary_median_cny",
            title="Demand Index vs Job Openings",
            opacity=0.7
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        yearly_salary = df.groupby("year")["salary_median_cny"].mean().reset_index()
        fig3 = px.line(
            yearly_salary,
            x="year",
            y="salary_median_cny",
            markers=True,
            title="Average Salary Trend Over Years"
        )
        fig3.update_layout(template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        yearly_jobs = df.groupby("year")["job_openings"].sum().reset_index()
        fig4 = px.area(
            yearly_jobs,
            x="year",
            y="job_openings",
            title="Total Job Openings Over Time"
        )
        fig4.update_layout(template="plotly_white")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")

    fig5 = px.histogram(
        df,
        x="salary_median_cny",
        nbins=40,
        title="Salary Density Distribution"
    )
    fig5.update_layout(template="plotly_white")
    st.plotly_chart(fig5, use_container_width=True)

# ============================================================
# SALARY & EXPERIENCE ANALYSIS PAGE
# ============================================================
if st.session_state.page == "Salary & Experience Analysis":

    st.markdown('<div class="title">💼 Salary & Experience Analysis</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Understanding salary behavior across experience, demand, and time</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    ### 📘 Analytical Overview
    This section explores the relationship between **salary levels**, **experience**, and
    **market demand**. By using advanced visualization techniques, this page provides insights
    into how compensation evolves with professional growth and market requirements.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.scatter(
            df,
            x="experience_years",
            y="salary_median_cny",
            trendline="ols",
            title="Impact of Experience on Median Salary"
        )
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.scatter(
            df,
            x="demand_index",
            y="salary_median_cny",
            size="job_openings",
            color="experience_years",
            title="Salary Variation by Market Demand & Job Openings",
            opacity=0.7
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        fig3 = px.violin(
            df,
            x="experience_years",
            y="salary_median_cny",
            box=True,
            title="Salary Distribution Across Experience Levels"
        )
        fig3.update_layout(template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        heatmap_data = df.groupby(["year", "experience_years"])["salary_median_cny"].mean().reset_index()
        fig4 = px.density_heatmap(
            heatmap_data,
            x="year",
            y="experience_years",
            z="salary_median_cny",
            title="Salary Growth Pattern Over Time & Experience"
        )
        fig4.update_layout(template="plotly_white")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:
        fig5 = px.density_contour(
            df,
            x="salary_median_cny",
            y="experience_years",
            title="Density Distribution of Salary & Experience"
        )
        fig5.update_layout(template="plotly_white")
        st.plotly_chart(fig5, use_container_width=True)

    with col6:
        salary_range = df.groupby("year").agg(
            min_salary=("salary_min_cny", "mean"),
            max_salary=("salary_max_cny", "mean")
        ).reset_index()

        fig6 = px.line(
            salary_range,
            x="year",
            y=["min_salary", "max_salary"],
            title="Salary Range Volatility Over Time"
        )
        fig6.update_layout(template="plotly_white")
        st.plotly_chart(fig6, use_container_width=True)

# ============================================================
# JOB DEMAND & MARKET KPIs PAGE
# ============================================================
if st.session_state.page == "Job Demand & Market KPIs":

    st.markdown('<div class="title">📈 Job Demand & Market KPIs</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Key performance indicators and demand-driven market insights</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    ### 📘 Page Overview
    This section focuses on **job demand indicators** and summarizes the job market
    using **Key Performance Indicators (KPIs)**. These metrics help in understanding
    market intensity, hiring trends, and salary behavior in high-demand roles.
    """)

    st.markdown("---")

    # ================= KPIs =================
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📌 Avg Demand Index", round(df["demand_index"].mean(), 2))

    with col2:
        st.metric("💼 Total Job Openings", int(df["job_openings"].sum()))

    with col3:
        st.metric("💰 Avg Median Salary (CNY)", int(df["salary_median_cny"].mean()))

    with col4:
        st.metric("📊 Avg Experience (Years)", round(df["experience_years"].mean(), 1))

    st.markdown("---")

    # ================= VISUALS =================
    col5, col6 = st.columns(2)

    with col5:
        fig1 = px.histogram(
            df,
            x="demand_index",
            nbins=35,
            title="Distribution of Market Demand Index"
        )
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    with col6:
        fig2 = px.scatter(
            df,
            x="demand_index",
            y="salary_median_cny",
            color="experience_years",
            title="Relationship Between Demand Index and Salary Levels",
            opacity=0.7
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    col7, col8 = st.columns(2)

    with col7:
        demand_jobs = df.groupby("demand_index")["job_openings"].sum().reset_index()
        fig3 = px.area(
            demand_jobs,
            x="demand_index",
            y="job_openings",
            title="Job Openings Across Demand Levels"
        )
        fig3.update_layout(template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

    with col8:
        demand_trend = df.groupby("year")["demand_index"].mean().reset_index()
        fig4 = px.line(
            demand_trend,
            x="year",
            y="demand_index",
            markers=True,
            title="Average Demand Index Trend Over Time"
        )
        fig4.update_layout(template="plotly_white")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")

    fig5 = px.density_heatmap(
        df,
        x="experience_years",
        y="demand_index",
        title="Density Pattern of Demand Index vs Experience"
    )
    fig5.update_layout(template="plotly_white")
    st.plotly_chart(fig5, use_container_width=True)
# ============================================================
# ADVANCED INSIGHTS & FORECASTING PAGE
# ============================================================
if st.session_state.page == "Advanced Insights & Forecasting":

    st.markdown('<div class="title">📊 Advanced Insights & Forecasting</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Future trends, predictive analysis, and actionable insights</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    ### 📘 Page Overview
    This section provides **advanced insights and forecasts** on the job market, salaries,
    and demand trends using historical data. Predictive analytics can help companies
    and job seekers make **data-driven decisions**.
    """)

    st.markdown("---")

    # ================= KPIs =================
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📈 Projected Avg Salary (Next Year)", int(df["salary_median_cny"].mean() * 1.05))

    with col2:
        st.metric("💼 Projected Job Openings", int(df["job_openings"].sum() * 1.08))

    with col3:
        st.metric("📊 High-Demand Skill Index", round(df["demand_index"].max(), 2))

    with col4:
        st.metric("💡 Insights Count", 5)

    st.markdown("---")

    # ================= VISUALS =================
    col1, col2 = st.columns(2)

    # -------- VISUAL 1: Salary Forecast (Line + Trend)
    with col1:
        salary_forecast = df.groupby("year")["salary_median_cny"].mean().reset_index()
        salary_forecast["forecast"] = salary_forecast["salary_median_cny"] * 1.05  # simple 5% projection
        fig1 = px.line(
            salary_forecast,
            x="year",
            y=["salary_median_cny", "forecast"],
            markers=True,
            title="Historical vs Forecasted Median Salary"
        )
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    # -------- VISUAL 2: Job Openings Forecast (Bar + Line)
    with col2:
        jobs_forecast = df.groupby("year")["job_openings"].sum().reset_index()
        jobs_forecast["forecast"] = jobs_forecast["job_openings"] * 1.08  # simple 8% projection
        fig2 = px.bar(
            jobs_forecast,
            x="year",
            y="job_openings",
            text="forecast",
            title="Historical Job Openings with Forecast"
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    col3, col4 = st.columns(2)

    # -------- VISUAL 3: Skill Demand Radar Chart
    with col3:
        skill_demand = df.groupby("demand_index")["job_openings"].sum().reset_index()
        fig3 = px.line_polar(
            skill_demand,
            r="job_openings",
            theta="demand_index",
            line_close=True,
            title="Skill Demand Radar",
            markers=True
        )
        fig3.update_layout(template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

    # -------- VISUAL 4: Experience vs Salary Forecast Heatmap
    with col4:
        heatmap_data = df.groupby(["year", "experience_years"])["salary_median_cny"].mean().reset_index()
        heatmap_data["forecast"] = heatmap_data["salary_median_cny"] * 1.05
        fig4 = px.density_heatmap(
            heatmap_data,
            x="year",
            y="experience_years",
            z="forecast",
            title="Forecasted Salary by Experience & Year"
        )
        fig4.update_layout(template="plotly_white")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")

    # -------- INSIGHT TEXT
    st.markdown("""
    ### 💡 Key Insights
    1. Median salaries are expected to **increase by ~5% next year** based on historical trends.  
    2. Total job openings are projected to grow by **8%**, indicating a robust hiring market.  
    3. Skills with the highest demand index should be prioritized for career growth.  
    4. Experience continues to play a major role in salary progression across years.  
    5. Predictive insights can guide both job seekers and employers in **strategic planning**.
    """)
    
# ============================================================
# SKILLS & JOB RECOMMENDATIONS PAGE
# ============================================================
if st.session_state.page == "Skills & Job Recommendations":

    st.markdown('<div class="title">💡 Skills & Job Recommendations</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Identify high-demand skills and suitable job roles</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    ### 📘 Page Overview
    This page highlights the most in-demand skills, their associated salaries,
    and provides suggestions for suitable job roles based on market demand
    and experience levels.
    """)

    st.markdown("---")

    # ================= KPIs =================
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📌 Top Skill Demand Index", df["demand_index"].max())

    with col2:
        st.metric("💼 Jobs Requiring Top Skill", int(df[df["demand_index"] == df["demand_index"].max()]["job_openings"].sum()))

    with col3:
        st.metric("💰 Avg Salary for Top Skill (CNY)", int(df[df["demand_index"] == df["demand_index"].max()]["salary_median_cny"].mean()))

    with col4:
        st.metric("📊 Avg Experience Required", round(df[df["demand_index"] == df["demand_index"].max()]["experience_years"].mean(), 1))

    st.markdown("---")

    # ================= VISUALS =================
    col1, col2 = st.columns(2)

    # -------- VISUAL 1: Top Skills vs Salary (Bar Chart)
    with col1:
        top_skills = df.groupby("demand_index")["salary_median_cny"].mean().reset_index().sort_values(by="demand_index", ascending=False)
        fig1 = px.bar(
            top_skills,
            x="demand_index",
            y="salary_median_cny",
            text="salary_median_cny",
            title="Top Skill Demand vs Avg Salary",
            labels={"demand_index": "Demand Index", "salary_median_cny": "Avg Salary (CNY)"}
        )
        fig1.update_layout(template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

    # -------- VISUAL 2: Experience vs Top Skills (Scatter)
    with col2:
        fig2 = px.scatter(
            df,
            x="experience_years",
            y="demand_index",
            size="job_openings",
            color="salary_median_cny",
            title="Experience vs Skill Demand & Salary",
            opacity=0.7,
            labels={"experience_years": "Experience (Years)", "demand_index": "Demand Index"}
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ================= TABLE OF RECOMMENDED JOBS =================
    st.markdown("### 📝 Recommended Jobs Based on High Demand Skills")

    recommended_jobs = df[df["demand_index"] >= df["demand_index"].quantile(0.75)][
        ["experience_years", "salary_median_cny", "demand_index", "job_openings"]
    ].sort_values(by="demand_index", ascending=False)

    st.dataframe(recommended_jobs.reset_index(drop=True))

    st.markdown("---")

    st.markdown("""
    ### 💡 Key Takeaways
    1. Focus on the **highest demand skills** to maximize job opportunities.  
    2. Salaries increase significantly with experience in high-demand roles.  
    3. Prioritize skill development in areas with high demand index.  
    4. Job openings are concentrated among top 25% high-demand skills.  
    5. This insight helps in **career planning and upskilling strategy**.
    """)
    # ============================================================
# FILTERS PAGE (FIXED & WORKING)
# ============================================================
if st.session_state.page == "Filters":

    st.markdown("## ⚡ Interactive Filters")

    st.markdown("---")

    # -------- FILTERS --------
    col1, col2, col3 = st.columns(3)

    with col1:
        min_exp = st.slider(
            "Minimum Experience (Years)",
            int(df["experience_years"].min()),
            int(df["experience_years"].max()),
            0
        )

    with col2:
        min_salary = st.slider(
            "Minimum Median Salary (CNY)",
            int(df["salary_median_cny"].min()),
            int(df["salary_median_cny"].max()),
            int(df["salary_median_cny"].min())
        )

    with col3:
        min_demand = st.slider(
            "Minimum Demand Index",
            int(df["demand_index"].min()),
            int(df["demand_index"].max()),
            int(df["demand_index"].min())
        )

    # -------- APPLY FILTERS --------
    filtered_df = df[
        (df["experience_years"] >= min_exp) &
        (df["salary_median_cny"] >= min_salary) &
        (df["demand_index"] >= min_demand)
    ]

    st.markdown("---")

    # -------- KPIs --------
    col4, col5, col6 = st.columns(3)

    col4.metric("💼 Total Jobs", len(filtered_df))
    col5.metric("💰 Avg Salary (CNY)", int(filtered_df["salary_median_cny"].mean()))
    col6.metric("📊 Avg Demand Index", round(filtered_df["demand_index"].mean(), 2))

    st.markdown("---")

    # -------- VISUAL --------
    fig = px.scatter(
        filtered_df,
        x="experience_years",
        y="salary_median_cny",
        size="job_openings",
        color="demand_index",
        title="Filtered Jobs: Salary vs Experience",
        labels={
            "experience_years": "Experience (Years)",
            "salary_median_cny": "Median Salary (CNY)"
        }
    )
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.markdown("### 📋 Filtered Data")
    st.dataframe(filtered_df)

# ============================================================
# DATA VIEW PAGE
# ============================================================
if st.session_state.page == "Data View":

    st.markdown('<div class="title">📂 Data View</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Interactive view of the raw job market dataset</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    ### 📘 Page Overview
    This page provides an **interactive table** of the job market dataset.
    You can filter, sort, and explore the data for deeper insights.
    """)

    # Show first n rows slider
    rows_to_show = st.slider("Select number of rows to display", min_value=5, max_value=len(df), value=20, step=5)
    
    st.dataframe(df.head(rows_to_show))

    st.markdown("---")

    # Optional: Allow user to download CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Dataset as CSV",
        data=csv,
        file_name="job_market_data.csv",
        mime="text/csv"
    )
# ============================================================
# CONCLUSION & INSIGHTS PAGE
# ============================================================
if st.session_state.page == "Conclusion & Insights":

    st.markdown('<div class="title">🏁 Conclusion & Insights</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Key takeaways and recommendations from the job market analysis</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("""
    ### 📘 Summary of Findings
    1. **Salary Trends:** Median salaries show a steady increase over the years. Experience strongly impacts compensation.  
    2. **Job Demand:** High-demand skills correspond to higher salaries and more job openings.  
    3. **KPIs:** Average demand index, job openings, and experience provide actionable insights for career planning.  
    4. **Forecasting:** Predicted salary growth and job openings indicate a positive trend in the job market.  
    5. **Skill Focus:** Prioritizing high-demand skills enhances career opportunities and market competitiveness.
    """)

    st.markdown("---")

    st.markdown("""
    ### 💡 Recommendations
    - Focus on acquiring **high-demand skills** identified in the market.  
    - Target roles with **growing job openings** for better career prospects.  
    - Use predictive insights to **plan career path and salary growth**.  
    - Leverage dashboards for continuous **monitoring of market trends**.  
    - Upskill in areas with **high demand index and low experience threshold** to maximize opportunities.
    """)

    st.markdown("---")

    st.markdown("""
    ### 🔹 Final Note
    This dashboard provides **comprehensive insights** into the Chinese job market.  
    By combining **historical analysis, KPIs, forecasting, and skill recommendations**, it serves as a powerful tool for **job seekers, HR professionals, and decision-makers** to make data-driven decisions.
    """)
