import pandas as pd

print("A quick look into the dataset..")
ctaRides = pd.read_csv('data/CTA_Ridership.csv', sep=',')
print(ctaRides.head())

# print("Description:")
# print(ctaRides.describe())

def stationRidesByYear(station, year):
    ctaRides['date_time'] = pd.to_datetime(ctaRides['month_beginning'])

    beginning = '01/01/' + str(year)
    end = '12/31/' + str(year)

    stationRides = ctaRides[(ctaRides['stationame'] == station) &
                            (ctaRides['date_time'] >= beginning) &
                            (ctaRides['date_time'] < end)]
    return stationRides['monthtotal'].sum()


q1 = "Which one of the two train stations next to my apartment is more popular?"
# Apartment location: Edgewater
# Closest stations: Bryn Mawr and Berwyn
print("\n * " + q1)
print("Berwyn rides in 2017: " + str(stationRidesByYear('Berwyn', 2017)))
print("Bryn Mawr rides in 2017: " + str(stationRidesByYear('Bryn Mawr', 2017)))


q2 = "Which are the most popular stations? And the least ones?"
stationGroup = ctaRides.groupby(['stationame'])
stationTotals = pd.DataFrame(stationGroup['monthtotal'].sum())
stationTotals.sort_values(ascending=False, by='monthtotal', inplace=True)

print("\n * " + q2)
print("Most popular")
print(stationTotals.head(3))
print("\nLeast popular")
print(stationTotals.tail(3))
