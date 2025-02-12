import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.renaming_and_combining import *
print("Setup complete.")

reviews.head()

	country	description	designation	points	price	province	region_1	region_2	taster_name	taster_twitter_handle	title	variety	winery
0	Italy	Aromas include tropical fruit, broom, brimston...	Vulkà Bianco	87	NaN	Sicily & Sardinia	Etna	NaN	Kerin O’Keefe	@kerinokeefe	Nicosia 2013 Vulkà Bianco (Etna)	White Blend	Nicosia
1	Portugal	This is ripe and fruity, a wine that is smooth...	Avidagos	87	15.0	Douro	NaN	NaN	Roger Voss	@vossroger	Quinta dos Avidagos 2011 Avidagos Red (Douro)	Portuguese Red	Quinta dos Avidagos
2	US	Tart and snappy, the flavors of lime flesh and...	NaN	87	14.0	Oregon	Willamette Valley	Willamette Valley	Paul Gregutt	@paulgwine	Rainstorm 2013 Pinot Gris (Willamette Valley)	Pinot Gris	Rainstorm
3	US	Pineapple rind, lemon pith and orange blossom ...	Reserve Late Harvest	87	13.0	Michigan	Lake Michigan Shore	NaN	Alexander Peartree	NaN	St. Julian 2013 Reserve Late Harvest Riesling ...	Riesling	St. Julian
4	US	Much like the regular bottling from 2012, this...	Vintner's Reserve Wild Child Block	87	65.0	Oregon	Willamette Valley	Willamette Valley	Paul Gregutt	@paulgwine	Sweet Cheeks 2012 Vintner's Reserve Wild Child...	Pinot Noir	Sweet Cheeks

# Your code here
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale')) 
print(renamed)
# Check your answer
q1.check()

        country                                        description  \
0          Italy  Aromas include tropical fruit, broom, brimston...   
1       Portugal  This is ripe and fruity, a wine that is smooth...   
2             US  Tart and snappy, the flavors of lime flesh and...   
3             US  Pineapple rind, lemon pith and orange blossom ...   
4             US  Much like the regular bottling from 2012, this...   
...          ...                                                ...   
129966   Germany  Notes of honeysuckle and cantaloupe sweeten th...   
129967        US  Citation is given as much as a decade of bottl...   
129968    France  Well-drained gravel soil gives this wine its c...   
129969    France  A dry style of Pinot Gris, this is crisp with ...   
129970    France  Big, rich and off-dry, this is powered by inte...   

                                   designation  points  price  \
0                                 Vulkà Bianco      87    NaN   
1                                     Avidagos      87   15.0   
2                                          NaN      87   14.0   
3                         Reserve Late Harvest      87   13.0   
4           Vintner's Reserve Wild Child Block      87   65.0   
...                                        ...     ...    ...   
129966  Brauneberger Juffer-Sonnenuhr Spätlese      90   28.0   
129967                                     NaN      90   75.0   
129968                                   Kritt      90   30.0   
129969                                     NaN      90   32.0   
129970           Lieu-dit Harth Cuvée Caroline      90   21.0   

                 province               region             locale  \
0       Sicily & Sardinia                 Etna                NaN   
1                   Douro                  NaN                NaN   
2                  Oregon    Willamette Valley  Willamette Valley   
3                Michigan  Lake Michigan Shore                NaN   
4                  Oregon    Willamette Valley  Willamette Valley   
...                   ...                  ...                ...   
129966              Mosel                  NaN                NaN   
129967             Oregon               Oregon       Oregon Other   
129968             Alsace               Alsace                NaN   
129969             Alsace               Alsace                NaN   
129970             Alsace               Alsace                NaN   

               taster_name taster_twitter_handle  \
0            Kerin O’Keefe          @kerinokeefe   
1               Roger Voss            @vossroger   
2             Paul Gregutt           @paulgwine    
3       Alexander Peartree                   NaN   
4             Paul Gregutt           @paulgwine    
...                    ...                   ...   
129966  Anna Lee C. Iijima                   NaN   
129967        Paul Gregutt           @paulgwine    
129968          Roger Voss            @vossroger   
129969          Roger Voss            @vossroger   
129970          Roger Voss            @vossroger   

                                                    title         variety  \
0                       Nicosia 2013 Vulkà Bianco  (Etna)     White Blend   
1           Quinta dos Avidagos 2011 Avidagos Red (Douro)  Portuguese Red   
2           Rainstorm 2013 Pinot Gris (Willamette Valley)      Pinot Gris   
3       St. Julian 2013 Reserve Late Harvest Riesling ...        Riesling   
4       Sweet Cheeks 2012 Vintner's Reserve Wild Child...      Pinot Noir   
...                                                   ...             ...   
129966  Dr. H. Thanisch (Erben Müller-Burggraef) 2013 ...        Riesling   
129967                  Citation 2004 Pinot Noir (Oregon)      Pinot Noir   
129968  Domaine Gresser 2013 Kritt Gewurztraminer (Als...  Gewürztraminer   
129969      Domaine Marcel Deiss 2012 Pinot Gris (Alsace)      Pinot Gris   
129970  Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...  Gewürztraminer   

                                          winery  
0                                        Nicosia  
1                            Quinta dos Avidagos  
2                                      Rainstorm  
3                                     St. Julian  
4                                   Sweet Cheeks  
...                                          ...  
129966  Dr. H. Thanisch (Erben Müller-Burggraef)  
129967                                  Citation  
129968                           Domaine Gresser  
129969                      Domaine Marcel Deiss  
129970                          Domaine Schoffit  

[129971 rows x 13 columns]
/usr/local/lib/python3.10/dist-packages/pandas/io/formats/format.py:1458: RuntimeWarning: invalid value encountered in greater
  has_large_values = (abs_vals > 1e6).any()
/usr/local/lib/python3.10/dist-packages/pandas/io/formats/format.py:1459: RuntimeWarning: invalid value encountered in less
  has_small_values = ((abs_vals < 10 ** (-self.digits)) & (abs_vals > 0)).any()
/usr/local/lib/python3.10/dist-packages/pandas/io/formats/format.py:1459: RuntimeWarning: invalid value encountered in greater
  has_small_values = ((abs_vals < 10 ** (-self.digits)) & (abs_vals > 0)).any()

reindexed = reviews.rename_axis('wines', axis='rows')
print(reindexed)
# Check your answer
q2.check()

      country                                        description  \
wines                                                                 
0          Italy  Aromas include tropical fruit, broom, brimston...   
1       Portugal  This is ripe and fruity, a wine that is smooth...   
2             US  Tart and snappy, the flavors of lime flesh and...   
3             US  Pineapple rind, lemon pith and orange blossom ...   
4             US  Much like the regular bottling from 2012, this...   
...          ...                                                ...   
129966   Germany  Notes of honeysuckle and cantaloupe sweeten th...   
129967        US  Citation is given as much as a decade of bottl...   
129968    France  Well-drained gravel soil gives this wine its c...   
129969    France  A dry style of Pinot Gris, this is crisp with ...   
129970    France  Big, rich and off-dry, this is powered by inte...   

                                   designation  points  price  \
wines                                                           
0                                 Vulkà Bianco      87    NaN   
1                                     Avidagos      87   15.0   
2                                          NaN      87   14.0   
3                         Reserve Late Harvest      87   13.0   
4           Vintner's Reserve Wild Child Block      87   65.0   
...                                        ...     ...    ...   
129966  Brauneberger Juffer-Sonnenuhr Spätlese      90   28.0   
129967                                     NaN      90   75.0   
129968                                   Kritt      90   30.0   
129969                                     NaN      90   32.0   
129970           Lieu-dit Harth Cuvée Caroline      90   21.0   

                 province             region_1           region_2  \
wines                                                               
0       Sicily & Sardinia                 Etna                NaN   
1                   Douro                  NaN                NaN   
2                  Oregon    Willamette Valley  Willamette Valley   
3                Michigan  Lake Michigan Shore                NaN   
4                  Oregon    Willamette Valley  Willamette Valley   
...                   ...                  ...                ...   
129966              Mosel                  NaN                NaN   
129967             Oregon               Oregon       Oregon Other   
129968             Alsace               Alsace                NaN   
129969             Alsace               Alsace                NaN   
129970             Alsace               Alsace                NaN   

               taster_name taster_twitter_handle  \
wines                                              
0            Kerin O’Keefe          @kerinokeefe   
1               Roger Voss            @vossroger   
2             Paul Gregutt           @paulgwine    
3       Alexander Peartree                   NaN   
4             Paul Gregutt           @paulgwine    
...                    ...                   ...   
129966  Anna Lee C. Iijima                   NaN   
129967        Paul Gregutt           @paulgwine    
129968          Roger Voss            @vossroger   
129969          Roger Voss            @vossroger   
129970          Roger Voss            @vossroger   

                                                    title         variety  \
wines                                                                       
0                       Nicosia 2013 Vulkà Bianco  (Etna)     White Blend   
1           Quinta dos Avidagos 2011 Avidagos Red (Douro)  Portuguese Red   
2           Rainstorm 2013 Pinot Gris (Willamette Valley)      Pinot Gris   
3       St. Julian 2013 Reserve Late Harvest Riesling ...        Riesling   
4       Sweet Cheeks 2012 Vintner's Reserve Wild Child...      Pinot Noir   
...                                                   ...             ...   
129966  Dr. H. Thanisch (Erben Müller-Burggraef) 2013 ...        Riesling   
129967                  Citation 2004 Pinot Noir (Oregon)      Pinot Noir   
129968  Domaine Gresser 2013 Kritt Gewurztraminer (Als...  Gewürztraminer   
129969      Domaine Marcel Deiss 2012 Pinot Gris (Alsace)      Pinot Gris   
129970  Domaine Schoffit 2012 Lieu-dit Harth Cuvée Car...  Gewürztraminer   

                                          winery  
wines                                             
0                                        Nicosia  
1                            Quinta dos Avidagos  
2                                      Rainstorm  
3                                     St. Julian  
4                                   Sweet Cheeks  
...                                          ...  
129966  Dr. H. Thanisch (Erben Müller-Burggraef)  
129967                                  Citation  
129968                           Domaine Gresser  
129969                      Domaine Marcel Deiss  
129970                          Domaine Schoffit  

reindexed = reviews.rename_axis('wines', axis='rows')

gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

combined_products = pd.concat([gaming_products, movie_products])
print(combined_products)
# Check your answer
q3.check()

                                                  name      category  \
0                 BOOMco Halo Covenant Needler Blaster  Toys & Games   
1    Raspberry PI 3 Model B 1.2GHz 64-bit quad-core...   Electronics   
2    CanaKit 5V 2.5A Raspberry Pi 3 Power Supply / ...   Electronics   
3    Panasonic K-KJ17MCA4BA Advanced Individual Cel...   Electronics   
4    Mayflash GameCube Controller Adapter for Wii U...   Electronics   
..                                                 ...           ...   
298                  Welcome to Night Vale CD: A Novel         Books   
299             Ran (StudioCanal Collection) [Blu-ray]   Movies & TV   
300                              The Art of John Alvin         Books   
301                               Apocalypto [Blu-ray]   Movies & TV   
302  Cinelinx: A Card Game for People Who Love Movi...  Toys & Games   

                                           amazon_link  total_mentions  \
0    https://www.amazon.com/BOOMco-Halo-Covenant-Ne...             4.0   
1    https://www.amazon.com/Raspberry-Model-A1-2GHz...            19.0   
2    https://www.amazon.com/CanaKit-Raspberry-Suppl...             7.0   
3    https://www.amazon.com/Panasonic-Advanced-Indi...            29.0   
4    https://www.amazon.com/GameCube-Controller-Ada...            24.0   
..                                                 ...             ...   
298  https://www.amazon.com/Welcome-Night-Vale-CD-N...             1.0   
299  https://www.amazon.com/StudioCanal-Collection-...             1.0   
300  https://www.amazon.com/Art-John-Alvin-Andrea/d...             1.0   
301  https://www.amazon.com/Apocalypto-Blu-ray-Rudy...             1.0   
302  https://www.amazon.com/Cinelinx-Card-Game-Peop...             1.0   

     subreddit_mentions subreddit  
0                     4  r/gaming  
1                     3  r/gaming  
2                     3  r/gaming  
3                     2  r/gaming  
4                     2  r/gaming  
..                  ...       ...  
298                   1  r/movies  
299                   1  r/movies  
300                   1  r/movies  
301                   1  r/movies  
302                   1  r/movies  

[796 rows x 6 columns]

powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
print(powerlifting_combined)
# Check your answer
q4.check()

        MeetPath Federation        Date MeetCountry MeetState  \
MeetID                                                                 
0        365strong/1601  365Strong  2016-10-29         USA        NC   
0        365strong/1601  365Strong  2016-10-29         USA        NC   
0        365strong/1601  365Strong  2016-10-29         USA        NC   
0        365strong/1601  365Strong  2016-10-29         USA        NC   
0        365strong/1601  365Strong  2016-10-29         USA        NC   
...                 ...        ...         ...         ...       ...   
8481    xpc/2017-finals        XPC  2017-03-03         USA        OH   
8481    xpc/2017-finals        XPC  2017-03-03         USA        OH   
8481    xpc/2017-finals        XPC  2017-03-03         USA        OH   
8481    xpc/2017-finals        XPC  2017-03-03         USA        OH   
8481    xpc/2017-finals        XPC  2017-03-03         USA        OH   

         MeetTown                                           MeetName  \
MeetID                                                                 
0       Charlotte  2016 Junior & Senior National Powerlifting Cha...   
0       Charlotte  2016 Junior & Senior National Powerlifting Cha...   
0       Charlotte  2016 Junior & Senior National Powerlifting Cha...   
0       Charlotte  2016 Junior & Senior National Powerlifting Cha...   
0       Charlotte  2016 Junior & Senior National Powerlifting Cha...   
...           ...                                                ...   
8481     Columbus                                    2017 XPC Finals   
8481     Columbus                                    2017 XPC Finals   
8481     Columbus                                    2017 XPC Finals   
8481     Columbus                                    2017 XPC Finals   
8481     Columbus                                    2017 XPC Finals   

                    Name Sex   Equipment  ...  WeightClassKg Squat4Kg  \
MeetID                                    ...                           
0       Angie Belk Terry   F       Wraps  ...             60      NaN   
0            Dawn Bogart   F  Single-ply  ...             60      NaN   
0            Dawn Bogart   F  Single-ply  ...             60      NaN   
0            Dawn Bogart   F         Raw  ...             60      NaN   
0           Destiny Dula   F         Raw  ...           67.5      NaN   
...                  ...  ..         ...  ...            ...      ...   
8481     William Barabas   M   Multi-ply  ...            125      NaN   
8481        Justin Zottl   M   Multi-ply  ...            125      NaN   
8481       Jake Anderson   M   Multi-ply  ...            125      NaN   
8481      Jeff Bumanglag   M   Multi-ply  ...            140      NaN   
8481       Shane Hammock   M   Multi-ply  ...            140      NaN   

        BestSquatKg Bench4Kg  BestBenchKg  Deadlift4Kg  BestDeadliftKg  \
MeetID                                                                   
0             47.63      NaN        20.41          NaN           70.31   
0            142.88      NaN        95.25          NaN          163.29   
0            142.88      NaN        95.25          NaN          163.29   
0               NaN      NaN        95.25          NaN             NaN   
0               NaN      NaN        31.75          NaN           90.72   
...             ...      ...          ...          ...             ...   
8481            NaN      NaN          NaN          NaN          347.50   
8481            NaN      NaN          NaN          NaN          322.50   
8481            NaN      NaN          NaN          NaN          367.50   
8481            NaN      NaN          NaN          NaN          320.00   
8481            NaN      NaN          NaN          NaN          362.50   

        TotalKg  Place   Wilks  
MeetID                          
0        138.35      1  155.05  
0        401.42      1  456.38  
0        401.42      1  456.38  
0         95.25      1  108.29  
0        122.47      1  130.47  
...         ...    ...     ...  
8481     347.50      2  202.60  
8481     322.50      3  185.77  
8481     367.50      1  211.17  
8481     320.00      3  181.85  
8481     362.50      2  205.18  

[386414 rows x 23 columns]
