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
def update_damage(list_one):
  new_list = []
  for string in list_one:
    if (string == 'Damages not recorded'):
      new_list.append(string)
    elif (string[-1] == 'M'):
      new_list.append(float(string[0:-1] )* conversion['M'])
    elif (string[-1] == 'B'):
      new_list.append(float(string[0:-1])* conversion['B'])   
  return new_list

# test function by updating damages
updated_damages = update_damage(damages)
print(updated_damages)

# 2 
def construct_dict(list_name, list_month, list_year,list_max_sustained_wind, list_area_affected, list_damages, list_deaths):
  new_dict = {}
  for i in range(len(list_name)):
    new_dict.update({list_name[i]:{'Name': list_name[i], 'Month': list_month[i], 'Year': list_year[i], 'Max Sustained Wind': list_max_sustained_wind[i], 'Areas Affected': list_area_affected[i], 'Damage': list_damages[i], 'Deaths':list_deaths[i]}})
  return new_dict  

combined_hurricane_lists = construct_dict(names, months,years, max_sustained_winds,areas_affected,updated_damages, deaths)
print(combined_hurricane_lists)

def create_hurricanes_by_year(hurricanes):
    hurricanes_by_year = {}
    for hur in hurricanes:
        current_year = hurricanes[hur]["Year"]
        current_cane = hurricanes[hur]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_cane]
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year

print(create_hurricanes_by_year(combined_hurricane_lists))

def count_areas(areas_affected_by_canes):
  new_dict = {}
  for area_list in areas_affected_by_canes:
    for area in area_list:
      if area not in new_dict:
        new_dict[area] = 1
    else:
      new_dict[area] += 1
  return new_dict

num_hurricanes_by_area = count_areas(areas_affected)
print(num_hurricanes_by_area)

def affected_area_count(dictionary):
  most_affected = ''
  max_count = 0
  for key in dictionary.keys():
    if (dictionary[key] > max_count):
      max_count = dictionary[key]
      most_affected = key
    
    return most_affected , max_count

print(affected_area_count(num_hurricanes_by_area))    
# 7
# Rating Hurricanes by Mortality
def hurricane_mortality(dictionary):
  hurr_name = ''
  hurr_deaths = 0
  for key in dictionary:
    if (dictionary[key]['Deaths'] > hurr_deaths):
      hurr_name = key
      hurr_deaths = dictionary[key]['Deaths']
  return hurr_name, hurr_deaths  
print(hurricane_mortality(combined_hurricane_lists))  


# categorize hurricanes in new dictionary with mortality severity as key

def hurr_mortality_scale(dictionary):
  scale_dict = {1:[], 2:[], 3:[], 4:[], 5:[]}
  for key in dictionary:
    if dictionary[key]['Deaths'] > 0 and dictionary[key]['Deaths'] < 100:
      scale_dict[1].append(key)
    elif dictionary[key]['Deaths'] > 100 and dictionary[key]['Deaths'] < 500:
      scale_dict[2].append(key)
    elif dictionary[key]['Deaths'] > 500 and dictionary[key]['Deaths'] < 1000:
      scale_dict[3].append(key)
    elif dictionary[key]['Deaths'] > 1000 and dictionary[key]['Deaths'] < 10000:
      scale_dict[4].append(key)
    elif dictionary[key]['Deaths'] > 10000:
      scale_dict[5].append(key) 
  return scale_dict

print(hurr_mortality_scale(combined_hurricane_lists))


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def damage_hurr(dictionary):
  max_damage = 0
  max_damage_cane = ''
  for cane in dictionary:
    if dictionary[cane]['Damage'] == 'Damages not recorded':
      continue
    elif dictionary[cane]['Damage'] > max_damage:
      max_damage = dictionary[cane]['Damage']
      max_damage_cane = cane  
  return max_damage, max_damage_cane

print(damage_hurr(combined_hurricane_lists))
# 9
# Rating Hurricanes by Damage

def hurr_rating_damage(dictionary):
  new_dict = { 0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for cane in dictionary:
    if dictionary[cane]['Damage'] == 'Damages not recorded':
      continue
    elif dictionary[cane]['Damage'] == 0 :
      new_dict[0].append(dictionary[cane])
    elif dictionary[cane]['Damage'] > 0 and  dictionary[cane]['Damage'] <= 100000000:
      new_dict[1].append(dictionary[cane])
    elif dictionary[cane]['Damage'] > 100000000 and  dictionary[cane]['Damage'] <= 1000000000:
      new_dict[2].append(dictionary[cane])
    elif dictionary[cane]['Damage'] >  1000000000 and  dictionary[cane]['Damage'] <= 10000000000:
      new_dict[3].append(dictionary[cane])
    elif dictionary[cane]['Damage'] > 10000000000 and  dictionary[cane]['Damage'] <= 50000000000:
      new_dict[4].append(dictionary[cane])
    elif dictionary[cane]['Damage'] > 50000000000:
      new_dict[5].append(dictionary[cane])
  return new_dict

print(hurr_rating_damage(combined_hurricane_lists))


damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
