import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':'chicago.csv',
              'new york city':'new_york_city.csv',
              'washington':'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("What city you want data for : chicago, new york city, washington ?").lower()
    while type(city) != str or  city not in ["washington" , "new york city" , "chicago"]:
        city = input("What city you want data for : Chicago , New York or Washington ?").lower()
    # get user input for month (all, january, february, ... , june)

    month = input("Which month you want to check ? (enter all or the full name of the month you want) ").lower()
    while type(month) != str :
        month = input("Which month you want to check ? (enter all or the full name of the month you want) ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("which day you want to check ? (all, monday, tuesday, ... sunday)").lower()
    while type(day) != str :
        day = input("which day you want to check ? (all, monday, tuesday, ... sunday)").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    # month filteration
    if month != "all" :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df [df["month"] == month ]
    # day filiteration
    if day != 'all':

        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df["month"].mode()[0]
    print("most  common month is " , most_common_month)

    # display the most common day of week
    most_common_day = df["day"].mode()[0]
    print("most common day is " , most_common_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df["hour"].mode()[0]
    print("most common hour is ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip. I <3 Udacity"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_startstation = df["Start Station"].mode()[0]
    print("most common startstation is :" , most_common_startstation)

    # display most commonly used end station
    most_common_endstation = df["End Station"].mode()[0]
    print("most common endstation is :" , most_common_endstation)

    # display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + ' to ' + df['End Station']

    print("most common start and end station : ",df.start_end_station.mode().iloc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
<<<<<<< HEAD
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
=======
    """Displays statistics on the total and average trip duration. I love Udacity <3 """

    print('\nCalculating Trip Duration......\n')
>>>>>>> documentation
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
<<<<<<< HEAD
    print("total travel time :" , total_travel_time)
    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean travel time :" , mean_travel_time)
=======
    print("total travel time is" , total_travel_time)
    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean travel time is" , mean_travel_time)
>>>>>>> documentation

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
<<<<<<< HEAD
    """Displays statistics on bikeshare users."""
=======
    """Displays statistics on bikeshare users. I <3 Udacity"""
>>>>>>> documentation

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_of_subscribers = (df[df["User Type"] == "Subscriber"])["User Type"].count()
    count_of_customers = (df[df["User Type"] == "Customer"])["User Type"].count()
    print("Number of subscribers = " , count_of_subscribers)
    print("Number of customers = " , count_of_customers )
    # filling nan with zeros
    df.fillna("0")
    # Display counts of gender
    if 'Gender' in df  :
        count_of_males = df[df["Gender"] == "Male"]["Gender"].count()
        count_of_females = df[df["Gender"] == "Female"]["Gender"].count()
        print("Number of males = " , count_of_males)
        print("Number of females = ", count_of_females)

        # Display earliest, most recent, and most common year of birth
        print("Earliest year is " , df["Birth Year"].max())
        print("Most recent year is " , df["Birth Year"].min())
        print("Most common year is " , df["Birth Year"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        data_handeling = input("Do you want to see 5 rows of raw data ?(yes or no )").lower()
        i = 1
        while data_handeling == 'yes' :
            n = 5

            print(df.head(n*i))
            i += 1
            data_handeling = input("Do you want to see 5 more rows of raw data ?(yes or no )").lower()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
