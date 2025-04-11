
# Project Background
This is a project I did during my internship in Thailand where I was tasked to recommend storage conditions to local bee farmers to minimise bacterial growth. To do this, I stored the honey in different condions (anaerobic/aerobic) and at different temperatures (4, 25, 37°C) for 6 weeks. While a lower bacterial count is generally seen as a positive, in the context of honey, there are some good bacteria like lactic acid (LAB) which is what gives honey its natural preservative to pathogens. This challenge was what inspired me to write this code to determine which storage condition was the best to recommend to the local bee farmers.

# Data Structure
The dataset was sorted by condition and temperature based on the different bacteria (lactic acid bacteria, bacillus, yeast and mould) across the 6 weeks. Below is an example of how the anaerobic table was saved in Excel.

![Excel](https://github.com/user-attachments/assets/c19d9c37-ba0f-4a1f-ab66-acdfbd53106d)

# Executive Summary
### Overview:
The best condition to recommend was at 4°C in an anaerobic condition which gave the lowest mean bacterial count change of 288.58 CFU/mL. This means that the changes for all bacteria was the smallest in the recommended storage condition from Day 0. For each individual bacteria, the recommended storage conditions are as follows:
- 4°C anaerobic (Yeast and Mould)
- 25°C anaerobic (LAB)
- 37°C aerobic (Bacillus)
While the recommendations were not statistically significant based on Two-way ANOVA results (likely due to variability in microbial counts), using the smallest average changes in bacterial counts provided a practical alternative for decision-making. Both temperature and condition were treated as categorical variables, as they represent fixed experimental settings rather than continuous measurements. Thus, the best environment to keep honey that is produced from Heterotrigona itama is at 4°C in an anaerobic condition.

### Code
Python libraries used in this project are:
- pandas
- matplotlib
- seaborn
- scipy
- statsmodel.api

Since I knew my data had zero values due to there being no presence of bateria in the culture, that does not mean that there is not bacteria present. To solve this problem, I used the average values across the 6 weeks to replace the zero values in the dataset.

![First](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

The next part is to do descriptive statistics to understand our data better before doing any analysis

![Second](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

After doing descriptive statistics, I then conducted a Two-way ANOVA with a Tukey's Pairwise Test to determine if there are any significant differences between the various combinations of environments that the honey was stored. 

![Third](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

As no significant differences were found, I plotted the bacterial count across the 6 weeks using matplotlib to visualise the changes over time.

![Fourth](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

Lastly, I used the lowest average change over time to recommend the best storage conditions for each microbe and for general stability.

![Fifth](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

### Trend Visualisation:

<p align="center">
    <img src="https://github.com/user-attachments/assets/ebce5715-d68c-40ad-aaaf-592ce85a7a09" hspace="10">
    <img src="https://github.com/user-attachments/assets/9f9fc816-1e7a-49ab-839a-74dc8f853932" hspace="10">
    <img src="https://github.com/user-attachments/assets/4f7dd6a4-26b0-4ddb-b808-a527919040e6" hspace="10">
</p>

- For yeast and mould, at 25°C in Aerobic conditions up to Day 7, the changes were the least siginifcant. However, at Day 35, 25°C in Anaerobic condition had the smallest change from Day 0 values. 4°C Aerobic on Day 35 gave the highest yeast and mould count.
- For LAB, the biggest change from Day 0 was on Day 21 stored at 37°C anaerobic. Both 25°C honey had the lowest changes from Day 0 values up to Day 28 and produced the smallest change in LAB count (since lower LAB isn’t always better contextually)
- For bacillus, 4°C honey had the lowest changes across the 6 weeks on average. Day 28 saw the highest bacillus count where the honey was kept at 37°C anaerobic. From Day 21 onwards, 25°C aerobic honey had the smallest change from Day 0 bacterial counts. 

# Recommendations
- The best environment to keep Heterotrigona itama honey is at 4°C in an anerobic condition
- If LAB counts are to be maintained to prevent over-acidification of honey, 25°C at aerobic conditions would be best up to 4 weeks in storage.
- Minimisation of bacillus was the most effective at 4°C in aerobic conditions which would extend shelf life of the honey.

# Limitations
- Microbial data is inherently variable; future studies could incorporate a larger sample size or longer storage duration to validate trends.
- Predictive modeling (e.g., ARIMA forecasting) could be used to estimate long-term microbial changes beyond the 6-week period.
- Additional factors like pH, water activity, and sugar content could be integrated for a more holistic storage recommendation.
