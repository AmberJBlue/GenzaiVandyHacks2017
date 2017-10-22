import tweepy
import json
import datetime

# import twitter *
#

response = []


consumer_key = "k2REKJw8e4u87KwqJsV1dKwQD"
consumer_secret = "gdhJhgDbZzFWUD2EaMJlnJP48BKt3eJE6WkxoxBlWYwMyBLqjQ"
access_token = "921586430622818304-EM7fVE2Zpd416jj0Rxa5cMpUrL4SKzf"
access_token_secret = "ZGgaJXHniKCIgvIUcbDuIrlDyHSvVBaRfVaxO9q3Xc3rD"
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
results = api.trends_place(2352824)

def getUSATrends():

    # Creating a dictionary for the US WoeIDs
    WoeIDs = {'Worldwide': 1,
            'United States':23424977,
            'Albuquerque':2352824,
            'Atlanta':2357024,
            'Austin':2357536,
            'Baltimore':2358820,
            'Baton Rouge':2359991,
            'Birmingham':2364559,
            'Boston':2367105,
            'Charlotte':2378426,
            'Chicago':2379574,
            'Cincinnati':2380358,
            'Cleveland':2381475,
            'Colorado Springs':2383489,
            'Columbus':2383660,
            'Dallas-Ft. Worth':2388929,
            'Denver':2391279,
            'Detroit':2391585,
            'El Paso':2397816,
            'Fresno':2407517,
            'Greensboro':2414469,
            'Harrisburg':2418046,
            'Honolulu':2423945,
            'Houston':2424766,
            'Indianapolis':2427032,
            'Jackson':2428184,
            'Jacksonville':2428344,
            'Kansas City':2430683,
            'Las Vegas':2436704,
            'Long Beach':2441472,
            'Los Angeles':2442047,
            'Louisville':2442327,
            'Memphis':2449323,
            'Mesa':2449808,
            'Miami':2450022,
            'Milwaukee':2451822,
            'Minneapolis':2452078,
            'Nashville':2457170,
            'New Haven':2458410,
            'New Orleans':2458833,
            'New York':2459115,
            'Norfolk':2460389,
            'Oklahoma City':2464592,
            'Omaha':2465512,
            'Orlando':2466256,
            'Philadelphia':2471217,
            'Phoenix':2471390,
            'Pittsburgh':2473224,
            'Portland':2475687,
            'Providence':2477058,
            'Raleigh':2478307,
            'Richmond':2480894,
            'Sacramento':2486340,
            'St. Louis':2486982,
            'Salt Lake City':2487610,
            'San Antonio':2487796,
            'San Diego':2487889,
            'San Francisco':2487956,
            'San Jose':2488042,
            'Seattle':2490383,
            'Tallahassee':2503713,
            'Tampa':2503863,
            'Tucson':2508428,
            'Virginia Beach':2512636,
            'Washington':2514815}


    for key, value in WoeIDs.iteritems():
        print(key + '\'s top 50 Trending topics are: ')
        results = api.trends_place(value)
        for location in results:
            for trend in location["trends"]:
                    print " - %s" % trend["name"]
        print('\n')

        response.append(results)
getUSATrends()

# Write response to JSON file
today = str(datetime.datetime.now().date())
time = str(datetime.datetime.now().time())
postingsFile = today + time + '.USAandNashvilleTrends.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()