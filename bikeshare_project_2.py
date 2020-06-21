import time
import pandas as pd
import numpy as np
#editing1 for refactoring 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

DAY=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
MONTH=['january','february','march','april','may','june','all']

def get_filters_city():
    
#editing2 for refactoring    
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
        
    """
    print('-'*40)
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    print('-'*40)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #create an empty list and append cities
    city_list=[]
    for city in CITY_DATA:
        city_list.append(city) 
        
       
    #get user input for city (chicago, new york city, washington)
    #if user type wrong city, function ask a same question
    while True:
        try:
            inp_city=input("\nPlease choose a city {}  --->   ".format(city_list)).lower()
            
        except:
            continue
        if inp_city  in city_list:
            break
        else:
            continue
    return inp_city
def get_filters_month():
    
    
    """
    Asks user to specify a month to analyze.

    Returns:
        (str) month - name of the month to analyze
        
    """
    
    # TO DO: get user input for month (all, january, february, ... , june)
    #create an empty list and append months
    month_list=[]
    for month in MONTH:
        month_list.append(month) 
        
    #get user input for month (all, january, february, ... , june)
    #if user type wrong , function ask a same question  
    
    while True:
        try:
            inp_month=input("\nPlease choose a month {}     --->   ".format(month_list)).lower()
            
        except:
            continue
        if inp_month  in month_list:
            break
        else:
            continue           
     
    return inp_month        
def get_filters_day():
    
    
    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - day of the month to analyze
        
    """
   
   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #create an empty list and append days of week
    #if user type wrong , function ask a same question  
    day_list=[]
    for day in DAY:
        day_list.append(day) 
        
      
    #  get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        try:
            inp_day=input("\nPlease choose a day {}     --->   ".format(day_list)).lower()
            
        except:
            continue
        if inp_day  in day_list:
            break
        else:
            continue           
     
    return inp_day        
def get_filters():
    

        #(str) city - name of the city to analyze
        #(str) month - name of the month to filter by, or "all" to apply no month filter
        #(str) day - name of the day of week to filter by, or "all" to apply no day 
    city=get_filters_city()
    month=get_filters_month()
    day=get_filters_day()
    print('-'*40)
    return city,month,day
def load_data(city,month,day):
    
    
    
    df = pd.read_csv(CITY_DATA[city])
     #CONVERT DATA TO DATETIME
    df['Start Time'] = pd.to_datetime(df['Start Time'],errors='coerce')
     # extract month,day from start time column
    df['month']= df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek 
    
    # filter by month if it is not chosen ALL
    if month != 'all':
        
        # assign number to month
        month_nmb = MONTH.index(month) + 1
        #filter by month
        df = df[df.month == month_nmb]
        month = month.title()
    # filter by day if it is not chosen ALL   
    if day != 'all':
        # assign number to day
        day_nmb = DAY.index(day) 
        #filter by day
        df = df[df.day == day_nmb]
        day = day.title()
        
    print("\nSelected City : ",city.title())
    print("Selected Month: ",month)
    print("Selected Day:",day)
    print("Count of Start Station:",len(df['Start Station'].unique()))
    print("Count of End Station:",len(df['End Station'].unique()))       
    print("Total Rows : {}\n" .format(len(df)))
    print('-'*40)
   
    return df
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """      
def time_stats(city):
    """Displays statistics on the most frequent times of travel independent month and day ."""

    
    start_time = time.time()

   
    df = pd.read_csv(CITY_DATA[city])
     #CONVERT ARG TO DATETIME
    df['Start Time'] = pd.to_datetime(df['Start Time'],errors='coerce')
     # extract month,day
    df['month']= df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    # calculate the most common month,hour and day
    max_month=df["month"].value_counts().head(1)
    max_day=df["day"].value_counts().head(1)
    hour = df["hour"].value_counts().head(1)
    print("\nCalculating The Most Frequent Times of Travel for {}...\n".format(city.title()))
    
     # display the most common month
     # display the most common start hour  
     # display the most common day of week
    print("Here is The Most Frequent Times of Travel")    
    print("        The most common month --> ", MONTH[(max_month.index)[0]-1])    
    print("        The most common day is --> ", DAY[(max_day.index)[0]])           
    print("        The most common start hour -->  ", hour.index[0])
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # most commonly used start station
    start_station = df["Start Station"].value_counts().head(1).index[0]
    
    start_station_trip = df["Start Station"].value_counts().head(1).max()
    
    #  most commonly used end station
    end_station = df["End Station"].value_counts().head(1).index[0]
    end_station_trip=df["End Station"].value_counts().head(1).max()
    
    # display most commonly used start station and end station
    
    print('Here is The Most Commonly Used Stations and Trips     ')
    print('        Start station --> {0} and Trip --> {1}'.format(start_station,start_station_trip ))
    print('        End station --> {0} and Trip --> {1}'.format(end_station,end_station_trip ))
    
    # calculate most frequent combination of start station and end station trip
    # GROUP BY START STATION AND END STATION
    df_start_end_station= df.groupby(['Start Station','End Station'])
    most_trip_count = df_start_end_station['Trip Duration'].count().max() 
    most_trip = df_start_end_station['Trip Duration'].count().idxmax()
    #trips =   (start_end_station).value_counts().head(1).max()
    
    #display most frequent combination of start station and end station trip
    print('        Start and End Station combination  --> {} , {} and Trip --> {}'.format( most_trip[0] , most_trip[1],most_trip_count))
    
   # print(trips)                              

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def time_converter(time):
    
    #Converte time( seconds) to day,hour,minutes and seconds
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return day,hour,minutes,seconds
def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # CALCULATE total travel time
    total_time=int(df['Trip Duration'].sum())          

    # CALCULATE mean travel time
    mean_time=int(df['Trip Duration'].mean())
    #Convert seconds to day,hour,seconds by time_converter

    print('Here is The Total Time Duration and Mean Time Duration   ')
    day, hour, minutes, seconds = time_converter(total_time)
    print("        Total Travel Time --> %d day %d hour %d minutes %d seconds" % (day, hour, minutes, seconds))
    day, hour, minutes, seconds = time_converter(mean_time)
    print("        Mean Travel Time --> %d day %d hour %d minutes %d seconds" % (day, hour, minutes, seconds)) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('Here is Counts of User Types')
    for i in range(len(user_count)):
         val = user_count[i]
         user_type = user_count.index[i] 
         
         print('        {} --> {}'.format(user_type ,val))
        

    # TO DO: Display counts of gender
    # if for exclude NaN
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('\nHere is Counts of Gender')
        for i in range(len(count_gender)):
            val = count_gender[i]
            gender = count_gender.index[i]            
            print('        {} --> {}'.format(gender ,val))
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # if for exclude NaN
    if 'Birth Year' in df.columns:
        
        
        print('\nHere is Earliest, Most Recent, and Most Common Year of Birth') 
        print('        Earliest --> ', int(df['Birth Year'].min()))
        print('        Most recent --> ', int(df['Birth Year'].max()))
        print('        Most common --> ', int(df['Birth Year'].mode()))
        
        
        

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(df):
    
    """Raw data is displayed upon request by the user in this manner: Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'."""
    row_count=5
    start_row=0
    end_row= row_count - 1
    print('\nWould you like to see some raw data from the current dataset?')
    while True:
        raw_data = input('   (yes or no) -->  ').lower()
       
        # adding +1 to rows for human readable --> it makes row count 1 to 5 
        if raw_data == 'yes':
            print('\nDisplaying rows {} to {}:'.format(start_row + 1, end_row + 1))
            print('\n', df.iloc[start_row : end_row + 1]) 
            
            start_row += row_count
            end_row += row_count
            print('-'*40)
            print('\nWould you like to see the next {} rows?'.format(row_count))
            continue
        else:
            break
            
            
        
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(city)
        station_stats(df)
        trip_duration_stats(df)           
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
