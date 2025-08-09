capital ={
    "France" : "Paris",
    "Germany" : "Berlin"
}

# travel_log = {
#     "France" : ["paris","lille","Dijon"],
#     "Germany" : ["berlin", "Stuttgart"]
# }

# print(travel_log["France"][1])
#
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log = {
    "France" : {
        'cities_visited' : ["paris","lille","Dijon"],
        'total_visits' : 12
    },
    "Germany" : {
        'cities_visited' : ["berlin", "Stuttgart"],
        'total_visits' : 8
    }
}
print(travel_log['Germany']["cities_visited"][1])
print(capital["France"])