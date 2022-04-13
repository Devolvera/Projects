# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def update_damage_func(lst):
  new_list = []
  for item in lst:
    if item == "Damages not recorded":
      new_list.append(item)
    else:
      if item[-1] == "M":
        n = float(item[:-1])
        new_list.append(n * conversion["M"])
      else:
        n = float(item[:-1])
        new_list.append(n * conversion["B"])
  return new_list

updated_damages = update_damage_func(damages)
#print(updated_damages)
# 2 
# Create a Table
def hurricane_data(names_lst, months_lst, years_lst, max_sustained_winds_lst, areas_affected_lst, damage_lst, deaths_lst):
  hurricane_dict = {}
  for item in range(len(names_lst)):
    hurricane_dict[names_lst[item]] = {"Name": names_lst[item], "Month": months_lst[item], "Year": years_lst[item], "Max Sustained Wind": max_sustained_winds_lst[item], "Areas Affected": areas_affected_lst[item], "Damage": damage_lst[item], "Deaths": deaths_lst[item]}
  return hurricane_dict
# Create and view the hurricanes dictionary
updated_hurricane_data = hurricane_data(names, months, years, max_sustained_winds, areas_affected,updated_damages, deaths)
#print(updated_hurricane_data)
# 3
# Organizing by Year
def hurricane_by_year(dictionary):
  year_dict = {}
  for key, value in dictionary.items():
    current_year = value["Year"]
    if not current_year in year_dict:
      year_dict[value["Year"]] = [value]
    else:
      year_dict[value["Year"]].append(value)
  return year_dict
# create a new dictionary of hurricanes with year and key
hurricane_year = hurricane_by_year(updated_hurricane_data)
#print(hurricane_year)

# 4
# Counting Damaged Areas
def areas_affected_count(lst):
  areas_dict = {}
  for area in lst:
    for location in area:
      if not location in areas_dict:
        count = 1
        areas_dict[location] = count
      else:
        count += 1
        areas_dict[location] = count
  return areas_dict

# create dictionary of areas to store the number of hurricanes involved in
count_of_areas_affected = areas_affected_count(areas_affected)
#print(count_of_areas_affected)

# 5 
# Calculating Maximum Hurricane Count
def max_hurricane_count(lst):
  num = max(lst.values())
  for key, value in lst.items():
    if value == num:
      return {key, value}
    
  #for key, value in lst.items():
# find most frequently affected area and the number of hurricanes involved in
#print(max_hurricane_count(count_of_areas_affected))

# 6
# Calculating the Deadliest Hurricane
def most_deaths(lst):
  death_count = 0
  hurricane = "Test"
  for key, value in lst.items():
    if value["Deaths"] > death_count:
      death_count = value["Deaths"]
      hurricane = value["Name"]
  return {hurricane, death_count}
  
# find highest mortality hurricane and the number of deaths
#print(most_deaths(updated_hurricane_data))
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality_rating(lst):
  new_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key, value in lst.items():
    deaths = value["Deaths"]
    hurricane = value["Name"]
    if deaths < 100:
      new_dict[1].append(hurricane)
    elif deaths < 500: 
      new_dict[2].append(hurricane)
    elif deaths < 1000:
      new_dict[3].append(hurricane)
    elif deaths < 10000:
      new_dict[4].append(hurricane)
    else: 
      new_dict[5].append(hurricane)
  return new_dict

# categorize hurricanes in new dictionary with mortality severity as key
mortality_severity = mortality_rating(updated_hurricane_data)
#print(mortality_severity)

# 8 Calculating Hurricane Maximum Damage
def max_damage(lst):
  max_dmg = 0
  hurricane = "NULL"
  for key, value in lst.items():
    damage = value["Damage"]
    if damage == "Damages not recorded":
      damage = 0
    if damage > max_dmg:
      max_dmg = damage
      hurricane = value["Name"]
  return {max_dmg, hurricane}
# find highest damage inducing hurricane and its total cost
#print(max_damage(updated_hurricane_data))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating(lst):
  new_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key, value in lst.items():
    deaths = value["Damage"]
    hurricane = value["Name"]
    if deaths == "Damages not recorded":
      deaths = 0
    if deaths < 100000000:
      new_dict[1].append(hurricane)
    elif deaths < 1000000000: 
      new_dict[2].append(hurricane)
    elif deaths < 10000000000:
      new_dict[3].append(hurricane)
    elif deaths < 50000000000:
      new_dict[4].append(hurricane)
    else: 
      new_dict[5].append(hurricane)
  return new_dict

print(damage_rating(updated_hurricane_data))