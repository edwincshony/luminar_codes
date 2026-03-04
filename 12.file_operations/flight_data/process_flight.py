# year and total number of passengers

fr = open("12.file_operations\\flight_data\\flight.txt")

flight = []

for line in fr:

    data = line.rstrip("\n").split(",")

    passenger_data = {"year":int(data[0]),"month":data[1],"passengers":int(data[2])}

    flight.append(passenger_data)

year_wise_count = {} #{1949:1520,1950:1676}

for p in flight:

    year = p.get("year") #1949

    p_count = p.get("passengers") # 112

    if year in year_wise_count: # 1949 in year_wise_count F so else works

        year_wise_count[year] += p_count

    else:

        year_wise_count[year] = p_count # {1949:112}

value_sort = sorted([[v,k] for k,v in year_wise_count.items()],reverse=True) # sorted with value

key_wise_sort1 = sorted(year_wise_count,key=year_wise_count.get) # sorted with key

print(value_sort)

print(key_wise_sort1)





