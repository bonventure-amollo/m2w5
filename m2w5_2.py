import pandas as pd
import matplotlib.pyplot as plt
import datetime

covid_dataset= "df_covid19_countries.csv"
df = pd.read_csv(covid_dataset)
df['quarter'] = pd.PeriodIndex(df.date, freq='Q')
df_summarized = df.groupby(['quarter']).mean()
df_summarized['total_cases'] = round(df_summarized['total_cases']/1000,2)
df_summarized['new_cases'] = round(df_summarized['new_cases']/1000,2)
df_summarized['total_deaths'] = round(df_summarized['total_deaths']/1000,2)
df_summarized['new_deaths'] = round(df_summarized['total_deaths']/1000,2)
df_summarized['vaccination_ratio'] = round(df_summarized['vaccination_ratio'],2)
df_summarized['total_vaccinations'] = round(df_summarized['total_vaccinations']/1000,2)
df_summarized['prevalence'] = round(df_summarized['prevalence'],2)
df_summarized['incidence'] = round(df_summarized['incidence'],2)
df_summarized['population'] = round(df_summarized['population']/1000000,2)
df_summarized.to_csv("covid_global_data.csv")
df_global = pd.read_csv('covid_global_data.csv')
reportingperiod = df_global['quarter'].tolist()
totalcases = df_global['total_cases'].tolist()
deathcases = df_global['total_deaths'].tolist()
newcases = df_global['new_cases'].tolist()
vaccinationratio = df_global['vaccination_ratio'].tolist()
totalvaccinations = df_global['total_vaccinations'].tolist()

#Total Cases
plt.rcParams["figure.figsize"] = [8.50, 5.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
plt.plot(reportingperiod, totalcases,   label = 'Total Cases', marker='.', linewidth=1, color='b', linestyle='solid',  markersize=12, markerfacecolor='white')
plt.xlabel('Reporting Period')
plt.ylabel('COVID-19 Cases (x1000)')
plt.legend(loc='upper left')
plt.xticks(reportingperiod)
plt.title('QUARTERLY GLOBAL MEAN OF COVID-19 TOTAL CASES FOR THE PERIOD 2020Q1 - 2023Q1')
plt.show()
plt.savefig('1.C19- Total Cases.png')
df_global.to_csv("1.C19- Total Cases.csv")

#Death Cases
plt.rcParams["figure.figsize"] = [8.50, 5.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
plt.plot(reportingperiod, deathcases,   label = 'Death Cases', marker='.', linewidth=1, color='c', linestyle='solid',  markersize=12, markerfacecolor='white')
plt.xlabel('Reporting Period')
plt.ylabel('COVID-19 Death Cases (x1000)')
plt.legend(loc='upper left')
plt.xticks(reportingperiod)
plt.title('QUARTERLY GLOBAL MEAN OF COVID-19 DEATH CASES FOR THE PERIOD 2020Q1 - 2023Q1')
plt.show()
plt.savefig('1.C19- Death Cases.png')


#New Cases
plt.rcParams["figure.figsize"] = [8.50, 5.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
plt.plot(reportingperiod, newcases,   label = 'New Cases', marker='.', linewidth=1, color='m', linestyle='solid',  markersize=12, markerfacecolor='white')
plt.xlabel('Reporting Period')
plt.ylabel('COVID-19 New Cases (x1000)')
plt.legend(loc='upper left')
plt.xticks(reportingperiod)
plt.title('QUARTERLY GLOBAL MEAN OF COVID-19 NEW CASES FOR THE PERIOD 2020Q1 - 2023Q1')
plt.show()
plt.savefig('3.C19- New Cases.png')


#Vaccination Cases
plt.rcParams["figure.figsize"] = [8.50, 5.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
plt.plot(reportingperiod, vaccinationratio,   label = 'Vaccination Ratio', marker='.', linewidth=1, color='g', linestyle='solid',  markersize=12, markerfacecolor='white')
plt.xlabel('Reporting Period')
plt.ylabel('Vaccination Ratio')
plt.legend(loc='upper left')
plt.xticks(reportingperiod)
plt.title('QUARTERLY VACCINATION RATIO OF COVID-19 FOR THE PERIOD 2020Q1 - 2023Q1')
plt.show()
plt.savefig('4.C19- Vaccination Cases.png')

d = {'Period':reportingperiod,'Total Cases':totalcases,'Total Vaccinations':totalvaccinations}
df_analysis = pd.DataFrame(d)
df_analysis.plot(kind="bar")
plt.bar_label(label_type="edge")
plt.title('COVID-19 CAOMPARATIVE ANALYSIS BETWEEN CASES AND VACCINATION FOR THE PERIOD 2020Q1 - 2023Q1')
plt.xlabel('Reporting Period (YearQuarter)')
plt.ylabel('Cases (X1000)')
plt.show()
