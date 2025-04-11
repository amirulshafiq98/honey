![image](https://i0.wp.com/post.healthline.com/wp-content/uploads/2021/04/honey-1296x728-header.jpg?w=1155&h=1528)


# Project Background
During my internship in Thailand, I was tasked with recommending optimal storage conditions for local bee farmers to minimize bacterial growth in honey. To achieve this, I stored honey under different conditions (anaerobic/aerobic) at varying temperatures (4°C, 25°C, 37°C) for six weeks. While a lower bacterial count is generally desirable, honey contains beneficial bacteria like lactic acid bacteria (LAB), which contribute to its natural preservative properties against pathogens. This challenge inspired me to develop a data-driven approach to determine the best storage conditions for the farmers.

# Data Structure
The dataset was organized by condition (anaerobic/aerobic) and temperature, tracking bacterial counts (lactic acid bacteria, Bacillus, yeast, and mold) over the six-week period. Below is an how the data is structured in Excel:

<p align="center">
  <img src="https://github.com/user-attachments/assets/c19d9c37-ba0f-4a1f-ab66-acdfbd53106d" hspace= "10"> 
  <img src="https://github.com/user-attachments/assets/672f2489-0fd2-4107-912b-6736e9b55518" hspace= "10">
</p>

# Executive Summary
### Overview:
The best overall storage condition was 4°C under anaerobic conditions, which yielded the smallest mean bacterial count change (288.58 CFU/mL) from baseline (Day 0). This indicates minimal microbial growth across all bacteria types. For specific bacteria, the recommended conditions are:
- 4°C anaerobic (Yeast and Mould)
- 25°C anaerobic (LAB)
- 37°C aerobic (Bacillus)
  
While Two-way ANOVA results did not show statistical significance (likely due to microbial variability), the smallest average changes in bacterial counts provided a practical basis for recommendations. Temperature and condition were treated as categorical variables, as they represented fixed experimental settings.

### Code
Python libraries used in this project are:
- pandas
- matplotlib
- seaborn
- scipy
- statsmodel.api

To address zero values (indicating no detectable bacteria in culture, not necessarily absence), I replaced them with the average bacterial counts across the six weeks.

![Second](https://github.com/user-attachments/assets/3b8a8962-afaf-45a6-b7d1-4e7917905da3)
****
Initial analysis was conducted to understand data trends before further testing:

![Third](https://github.com/user-attachments/assets/c029db3c-29ff-494f-9473-c2673689a5e6)
****
This set of code tested for significant differences between storage condition combinations. No significant differences were found.

![Fourth](https://github.com/user-attachments/assets/50e994bb-aeda-4291-972c-732b8250930e)
****
I plotted bacterial counts over six weeks using matplotlib to visualize temporal changes.

![Fifth](https://github.com/user-attachments/assets/d02885a5-feee-4335-8cbf-2b15e6eb5585)
****
The lowest average change in bacterial counts guided the storage recommendations for each microbe and overall stability.

![Sixth](https://github.com/user-attachments/assets/75f882f2-392e-44ce-b1ea-836250f23ae6)
![Sisth](https://github.com/user-attachments/assets/404c3ae5-83b8-4200-b5f9-3f246ee505ea)
****

### Statistical Analysis:
<p align="center">
  <img src="https://github.com/user-attachments/assets/74a383b8-a982-428c-9b2a-dac068f6f616">
  <img src="https://github.com/user-attachments/assets/cf867963-619a-4ecb-bfef-cd7adc399705">
</p>

As noted earlier, no statistically significant differences were observed between storage conditions. The null hypothesis was retained for all temperature and condition combinations.

### Trend Visualisation:
<p align="center">
    <img src="https://github.com/user-attachments/assets/ebce5715-d68c-40ad-aaaf-592ce85a7a09" hspace="10">
    <img src="https://github.com/user-attachments/assets/9f9fc816-1e7a-49ab-839a-74dc8f853932" hspace="10">
    <img src="https://github.com/user-attachments/assets/4f7dd6a4-26b0-4ddb-b808-a527919040e6" hspace="10">
</p>

- **Yeast and Mold:** At 25°C aerobic, changes were minimal up to Day 7, but by Day 35, 25°C anaerobic showed the smallest deviation from Day 0. The highest yeast/mold count occurred at 4°C aerobic on Day 35.
- **LAB:** The largest deviation from Day 0 occurred at 37°C anaerobic on Day 21. Both 25°C conditions maintained the lowest LAB changes up to Day 28.
- **Bacillus:** 4°C storage minimized growth across all weeks. Day 28 saw peak Bacillus counts at 37°C anaerobic, while 25°C aerobic had the smallest change from Day 0 after Day 21.

# Recommendations
- **Optimal storage:** 4°C anaerobic for Heterotrigona itama honey.
- **LAB preservation:** 25°C aerobic for up to 4 weeks to prevent over-acidification.
- **Bacillus control:* 4°C aerobic to extend shelf life.

# Limitations
- **Variability:** Microbial data is inherently variable; larger sample sizes or longer storage durations could strengthen findings.
- **Extended modeling:** Predictive models (e.g., ARIMA) could forecast long-term microbial trends beyond six weeks.
- **Additional factors:** Future studies could integrate pH, water activity, and sugar content for more comprehensive recommendations.
