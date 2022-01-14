import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        cities = ['chicago','new york city', 'washington']
        city = input('\nWhich city would you like to explore ?: chicago, new york city or washington? \n> ').lower()
        if city in cities:
            print('Thank you!, your preferred city is {}'.format(city.title()))
            break
        else:
            print("Oops, you entered a wrong input!. Try again.")
            
          
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['January','February','March','April','May','June','All']
        month = input("\nNow let's pick a month to filter by: January, February, March, April, May, June or type                                       \n'all' if you do not have any preference?\n").title()
        if month in months:
            print('Thank you!, your preferred month is {}'.format(month))
            break
        else:
            print("Oops, you entered a wrong input!. Try again.")
         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','All']
        day = input("\nFinally, what day do you want to filter by? Please select any day of the week: Sunday, Monday, Tuesday, Wednesday, \nThursday, Friday, Saturday, or all if you do not have any preference.\n").title()
        if day in days:
            print('Thank you!, your preferred day is {}'.format(day))
            break
        else:
            print("Oops, you entered a wrong input!. Try again.")
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January','February','March','April','May','June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The Most Common Month is:\n{}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The Most Common day is:\n{}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Common Hour is:\n{}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('\nThe Most commonly used start station is:\n{}'.format(Start_Station))

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe Most commonly used end station is:\n{}'.format(End_Station))


    # TO DO: display most frequent combination of start station and end station trip
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
    total_travel = df['Trip Duration'].sum()
    print("The Total travel time is:\n{}".format(total_travel))

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The Mean travel time is:\n{}".format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types Count is:\n{}'.format(user_types))

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        #print(gender_types)
        print("\nThe number of users by gender is:\n{}".format(gender_types))
    except:
        #print below string if condition above is not met
        print("\nThere is no 'Gender' column in this file.")
             

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = int(df['Birth Year'].min())
        #print Earliest_year
        print('\nThe Earliest Year is:\n{}'.format(Earliest_Year))
        #print Most_Recent_Year
        Most_Recent_Year = int(df['Birth Year'].max())
        print('\nThe Most Recent Year is:\n{}'.format(Most_Recent_Year))
        Most_Common_Year = int(df['Birth Year'].mode()[0])
        #print Most_Common_Year
        print('\nThe Most Common Year is:\n{}'.format(Most_Common_Year))
    except:
        #print below string if condition above is not met
        print("\nThere is no 'Birth Year' column in this file.")
		
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data(df):
    """Displays 5 rows of data from the file for city of choice"""
    
    while True:
        valid_entry = ['yes','no']
        response = input("Would you like to view the individual trip data for the first 5 entries ? Enter 'yes' or 'no'\n").lower()
        if response in valid_entry:
            if response == 'yes':
                start=0
                end=5
                trip_data = df.iloc[start:end,:]
                print(trip_data)
            break     
        else:
            print("Please enter a valid entry")
    if  response == 'yes':       
            while True:
                next_response = input("Would you like to view trip data for the next 5 entries? Enter 'yes' or 'no'\n").lower()
                if next_response in valid_entry:
                    if next_response == 'yes':
                        start += 5
                        end += 5
                        trip_data = df.iloc[start:end,:]
                        print(trip_data)
                    else:    
                        break  
                else:
                    print("Please enter a valid response")  

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
