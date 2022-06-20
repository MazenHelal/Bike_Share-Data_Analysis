import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

Cities = ['chicago', 'new york', 'washington']

Months = ['january', 'february', 'march', 'april', 'may', 'june']

Days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Would you like to see data for Chicago, New York or Washington: ').lower()
        if city in Cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Would you like to filter data by month like "january" ,"june" or type "all" to apply with no month filter: ').lower()
        if month == 'all':
            break
        elif month in Months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Would you like to filter data by day like "monday" , "tuesday" or type "all" to apply no day filter : ').lower()
        if day =='all':
            break
        elif day in Days:
            break    

    print('-'*40)
    return city, month ,day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading data from files
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  Months.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
  
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month is : ",popular_month)


    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("Most common day of week is : ",popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common hour is : ",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common Start Station is : ",popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common End Station is : ",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #popular_start_station_end_station = df['Start Station','End Station'].mode().loc[0]
    #print("Most common Start Station is : ",popular_start_station_end_station)
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print("Total Trip Duration is : ",Total_travel_time)

    # TO DO: display mean travel time
    Total_travel_time_avr = df['Trip Duration'].mean()
    print("Total Trip Duration Avearge (Mean) is : ",Total_travel_time_avr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User type count...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        user_gender(df)

    if 'Birth Year' in df.columns:
        user_birth_year(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_gender(df):
    # TO DO: Display counts of gender
    print('\nCalculating User Gender stats...\n')
    start_time = time.time()
    gender = df['Gender'].value_counts()
    print(gender)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_birth_year(df):
    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nCalculating Birth Year stats...\n')
    start_time = time.time()
    birth_year = df['Birth Year']

    #earliest year
    earliest_year=birth_year.min()
    integer_early_year=int(earliest_year)
    print("The earliest birth year is :",integer_early_year)

    
    #most recent year
    most_recent_year=birth_year.max()
    integer_recent_year=int(most_recent_year)
    print("The most recent birth year is :",integer_recent_year)

    #most common year 
    most_common_year=birth_year.mode()[0]
    integer_most_common_year=int(most_common_year)
    print("The most common birth year is : ",integer_most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df):
    start_loc = -5
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data not in ['yes','no']:
            view_data=print ("Please type correctly with 'yes' or 'no' only  : "  ).lower()
        elif view_data=='yes':
            start_loc += 5
            print(df.iloc[start_loc : start_loc + 5])
            view_data_again=input('\nDo you want to see the next five rows ?\n' ).lower()
            if view_data_again=='no':
                break
        elif view_data =='no':
            return        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
