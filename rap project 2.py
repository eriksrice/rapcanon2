def canon(**kwargs):
    result_list = []

    key_to_value = {
        'region': {
            'East': 15,
            'East Coast': 15,
            'West': 3.6,
            'West Coast': 3.6,
            'South': 5.2,
            'Midwest': 1.6,
            'International': .5
        },
        'city': {
            'New York': 10,
            'New York City': 10,
            'Atlanta': 2.2,
            'Compton': 1.3,
            'San Francisco': .9,
            'Newark': .9, 
            'Chicago': .9,
            'Houston': .9,
            'Philadelphia': .4,
            'Los Angeles': .4,
            'South Orange': .4,
            'Virginia Beach': .4,
            'Fayetteville': .4,
            'Portsmouth': .4,
            'Long Beach': .4,
            'Toranto': .4,
            'New Orleans': .4,
            'Detroit': .4,
            'Miami': .4
        },
        'living': {
            'yes': 5,
            'no': .4
        },
        'gender': {
            'male': 15,
            'female': 2
        },
        'birth_year': {
            '1958': 1.4,
            '1959': 1.4, 
            '1960': 1.4,
            '1961': 1.4,
            '1962': 1.4,
            '1963': 1.4,
            '1964': 1.4, 
            '1965': 2.9,
            '1966': 2.9,
            '1967': 2.9,
            '1968': 4.3,
            '1969': 4.3,
            '1970': 10,
            '1971': 7.1,
            '1972': 5.7,
            '1973': 5.7,
            '1974': 5.7,
            '1975': 5.7,
            '1976': 4.3,
            '1977': 4.3,
            '1978': 4.3,
            '1979': 4.3,
            '1980': 2.9,
            '1981': 2.9,
            '1982': 2.9,
            '1983': 1.4,
            '1984': 1.4,
            '1985': 1.4,
            '1986': 1.4,
            '1987': 1.4
        },
        'commercial_peak': {
            '1980': 1.7,
            '1981': 1.7,
            '1982': 1.7,
            '1983': 1.7,
            '1984': 1.7,
            '1985': 1.7,
            '1986': 1.7,
            '1987': 3.3,
            '1988': 5,
            '1989': 5,
            '1990': 5,
            '1991': 5,
            '1992': 5,
            '1993': 5,
            '1994': 5,
            '1995': 5,
            '1996': 10,
            '1997': 10, 
            '1998': 8.3,
            '1999': 8.3,
            '2000': 5,
            '2001': 5,
            '2002': 5,
            '2003': 3.3,
            '2004': 3.3,
            '2005': 3.3,
            '2006': 3.3,
            '2007': 3.3,
            '2008': 3.3,
            '2009': 1.7,
            '2010': 1.7,
            '2011': 1.7,
            '2012': 1.7,
            '2013': 1.7,
            '2014': 1.7,
            '2015': 1.7,
            '2016': 1.7,
            '2017': 1.7
        },
        'age_at_peak': {
            '19': 2.1,
            '20': 2.1,
            '21': 2.1,
            '22': 2.1,
            '23': 2.9,
            '24': 2.9,
            '25': 4.3,
            '26': 4.3,
            '27': 4.3,
            '28': 5,
            '29': 3.6,
            '30': 2.1,
            '31': 1.4,
            '32': 1.4,
            '33': 1.4,
            '34': 1.4,
            '35': .7
        },
        'number_one_albums': {
            '1': 2,
            '2': 4,
            '3': 6,
            '4': 8,
            '5': 10,
            '6': 12,
            '7': 14,
            '8': 16,
            '9': 18,
            '10': 20,
            '11': 22,
            '12': 24,
            '13': 26,
            '14': 28
        }
    }

    for key, value in kwargs.items():
        if key in key_to_value and value in key_to_value[key]:
            result_list.append(key_to_value[key][value])
        else:
            result_list.append(0)
    
    total_sum = sum(result_list)
    
    return total_sum

#using Jay-Z as a test
print(canon(region='East Coast', city='New York City', gender='male', living='yes', birth_year='1969', commercial_peak='1998', number_one_albums='14', age_at_peak='29'))