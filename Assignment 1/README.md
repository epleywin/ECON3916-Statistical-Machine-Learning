The Cost of Living Crisis: A Data-Driven Analysis

The Problem: Why the "Average" CPI Fails Students

The Consumer Price Index (CPI) is widely used as the primary measure of inflation in the United States, informing everything from Social Security adjustments to Federal Reserve policy decisions. However, the official CPI represents an average across all American consumers and may not accurately reflect the economic reality experienced by specific demographic groups—particularly college students.
Students face a fundamentally different "basket of goods" than the average American household. While the official CPI weights housing, transportation, and healthcare heavily, students allocate a disproportionate share of their budgets to tuition, rent in college towns, streaming services, and food. This analysis investigates whether the official CPI adequately captures the inflationary pressures students actually experience, and quantifies the divergence between national inflation measures and student-specific cost increases.

Methodology: Python, APIs, and Index Theory

This analysis employs rigorous data science techniques to construct a custom Student Price Index (SPI) and compare it against official inflation measures:

Data Collection:

- Utilized the Federal Reserve Economic Data (FRED) API to retrieve official CPI data and category-specific price indices
- Retrieved national CPI-U (All Urban Consumers) series
- Retrieved Boston-Cambridge-Newton metropolitan area CPI for regional comparison
- Extracted component indices for tuition, rent, streaming services, and food away from home

Index Construction:
The Student Price Index was constructed using Laspeyres index methodology, which measures the cost of a fixed basket of goods over time. The basket weights were determined based on typical student budget allocations:

- Tuition: 40% (reflecting the dominant expense for college students)
- Rent: 30% (one-bedroom apartment in college areas)
- Streaming Services: 10% (representing entertainment and digital subscriptions)
- Food Away from Home: 20% (Chipotle burritos as proxy for student dining habits)

Normalization:
All indices were normalized to a base year of 2016 = 100 to enable direct comparison across different data series with varying historical starting points. This standardization is essential for comparing inflation rates across categories that use different reference periods in their raw CPI calculations.

Technical Implementation:

- Programming Language: Python 3.x
- Key Libraries: fredapi, pandas, matplotlib
- Analysis Period: 1992-2025 (limited by data availability for streaming services)

Key Findings
1. Students Experience Significantly Different Inflation Than the General Population
My analysis reveals a dramatic divergence between student costs and national inflation, particularly in the period leading up to 2016. While the official CPI tracked relatively steady growth from the early 1990s through 2016, the Student Price Index lagged significantly behind, starting at approximately 41 points in 1992 compared to the national CPI's 57 points (when normalized to 2016 = 100).
However, this relationship inverted around 2016. From 2016 onward, student costs have accelerated faster than official CPI, with both indices converging around 2020 before student costs began pulling ahead. By 2025, both measures reach approximately 135-140 points, but the trajectory suggests students experienced a compressed inflationary period with steeper recent increases.

2. Category-Level Analysis Reveals Extreme Variability

The component analysis (Image 1) demonstrates why aggregate measures can be misleading:

Rent (green) and streaming services (red) showed explosive growth post-2016, reaching 145+ points by 2025—representing 45%+ inflation since 2016
Tuition (orange) displayed the most concerning long-term trend, climbing steadily but with the most dramatic acceleration occurring between 2016-2025, reaching 130 points
Food costs (purple) tracked closely with streaming and rent, all three converging around 135-140 by 2025
Official CPI (blue) showed the most stable, linear growth pattern, reaching approximately 150 points by 2025

3. The Normalization Problem: Why Raw Data Misleads
Image 3 illustrates the critical importance of proper data normalization. When examining raw CPI values without normalization:

Tuition CPI appears to reach 900+ points by 2025
Streaming services reach only 600 points

This creates a visual impression that tuition has inflated far more dramatically than streaming—but this is an artifact of different base years in the FRED data series. Once normalized to a common baseline (2016 = 100), the actual rate of change can be properly compared, revealing that both categories have experienced similar relative inflation rates in recent years.

4. Regional Variations: Boston vs. National Trends

The three-way comparison (Image 4) reveals important regional dynamics:

National CPI and Boston CPI track remarkably closely throughout most of the time series, starting together around 57-58 in 1992
Both indices show nearly identical trajectories through 2020, suggesting Boston's cost of living increased at the national average rate
Post-2020 divergence: After 2020, all three measures begin to separate, with the Student SPI showing the steepest acceleration
By 2025, Boston CPI reaches approximately 133 points, National CPI reaches 136 points, and Student SPI reaches 137 points
This suggests that Boston's inflation rate has been slightly below the national average, while student-specific costs have exceeded both

5. The Convergence Period (2020-2025)

A striking pattern emerges in the 2020-2025 period across all visualizations. After decades of divergent trends, all indices begin converging:

This likely reflects pandemic-era inflation affecting all categories simultaneously
The rapid increase in streaming prices and rent post-2020 brought these categories in line with long-term tuition trends
Students faced a "perfect storm" where all major expense categories inflated simultaneously

Implications

For Students: The official CPI significantly understates the inflationary pressure students face, particularly in recent years. A student's purchasing power has eroded faster than government-reported inflation suggests, potentially explaining the growing student debt crisis and increased financial stress among college populations.

For Policy Makers: Using national CPI to adjust student financial aid, scholarships, or loan limits may be insufficient. Student-specific inflation metrics should inform education policy decisions.

For Researchers: This analysis demonstrates the importance of demographic-specific price indices. Just as students experience different inflation than the general population, other groups (retirees, low-income households, rural residents) likely face divergent inflationary pressures that aggregate measures obscure.

Technologies Used: Python, FRED API, Pandas, Matplotlib, Index Theory (Laspeyres Method)
Data Sources: Federal Reserve Economic Data (FRED) - St. Louis Fed
Analysis Period: 1992-2025
