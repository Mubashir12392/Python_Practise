# mubashir = {
#     "name" : "mubashir",
#     "father" : "yameen",
#     "class" : "Elite"
# }

# # getting all keys from dictionary
# for x in mubashir.keys():
#     print(x)
# # getting all values from dictionary
# for x in mubashir.values():
#     print(x)


# # NESTED DICTIONARY

# country = {
#     "pakistan" : "Islamabad",
#     "england" : "London",
#     "dic2" : {
#             "punjab" : "Faisalabad",
#             "sindh" : "Karachi",
#             "dic3" : {
#                 "faisalabad" : "Abdullah pull",
#                 "lahore" : "DHA",
#                 "islamabad" : "F9",
#                 "dic4" : {
#                     "abdullahpull" : "Abdullah garden",
#                     "d-ground" : "Bambino",
#                     "kohinoor" : "bachi",
#                     "dic5" : {
#                         "bachi" : "aqsa",
#                         "cafe" : "chahy nagar"
#                     }
#                 }
#             }
#     }
# }


# print(f"""Our city {country['pakistan']} is very beautiful. {country['dic2']['punjab']} ma aik jaga ha {country['dic2']['dic3']['faisalabad']}
# or {country['dic2']['dic3']['faisalabad']} sa 16 km door kohinoor ma aik sexy si {country['dic2']['dic3']['dic4']['kohinoor']} ha. os 
# {country['dic2']['dic3']['dic4']['kohinoor']} ka naam {country['dic2']['dic3']['dic4']['dic5']['bachi']} ha.
# """)


# print({country["dic2"]["dic3"]})








# # LIST OF DICTS
# dicts_in_list = [
#     {"pakistan" : "Islamabad",   "england" : "London"},
#     {"punjab" : "Faisalabad", "sindh" : "Karachi",},
#     {"faisalabad" : "Abdullah pull", "lahore" : "DHA", "islamabad" : "F9",},
#     {"abdullahpull" : "Abdullah garden", "d-ground" : "Bambino", "kohinoor" : "bachi",}
# ]


# # LISTS INSIDE DICTS

# list_inside_dicts = {
#     ["pakistan","Islamabad","england","London"],
#     ["punjab","Faisalabad","sindh","Karachi"],
#     ["faisalabad","Abdullah pull","lahore","DHA","islamabad","F9"],
#     ["abdullahpull","Abdullah garden","d-ground","Bambino","kohinoor","bachi"]

# }
 
Student = {"324" :{"Name" : "Usman Malik",
                 "Father" : "Tariq Malik",
                 "Age" : 20,
                 "Class" : "Royal",
},
"325" : {
    "Name" : "Hamza Ali",
    "Father" : "Nadeem Rana",
    "Age" : 22,
    "Class" : "Royal",
}
}

for roll_number, values in Student.items():
    print(f'{roll_number} - {values["Name"]} - {values["Father"]} - {values["Age"]} - {values["Class"]}')
    


    



# for keys, values in Student.items():
#     for x in values.values():
#         print(keys, x)


"""
324, usman, tariq, 20, royak
"""