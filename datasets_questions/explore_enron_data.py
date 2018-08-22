#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


enron_data1 = open("../final_project/poi_names.txt","r")

person_of_interst =[]

for line in enron_data1:
    if "," in line:
        person_of_interst.append(line.strip())
        
print person_of_interst        

number_of_poi = len(person_of_interst)
print "Actual number of Person of Intersts ",number_of_poi

person_of_interst_in_dataset = [person for person in enron_data.keys() if enron_data[person]["poi"]]
print "James Prentice toatal stock value",enron_data["PRENTICE JAMES"]['total_stock_value']

print "Wesley Cowell messages ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Exercised stock options of SKILLING JEFFREY K", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]



for i in ["SKILLING JEFFREY K","LAY KENNETH L","FASTOW ANDREW S"]:
    print i,"\'s total payments = ",enron_data[i]["total_payments"]

quantified_salaries = [1 for folk in enron_data.keys() if enron_data[folk]["salary"]!='NaN']

print "Number of Quantified salaries",sum(quantified_salaries)

known_email_address = [1 for folk in enron_data.keys() if enron_data[folk]["email_address"]!='NaN']
print "Number of known email addresses",sum(known_email_address)

known_total_payments = [1 for folk in enron_data.keys() if enron_data[folk]["total_payments"]!='NaN']

percentage_of_unknown_total_payments = 100 * (1 - sum(known_total_payments)/float(len(enron_data.keys())))
print "Percentage of unknown total payments = ", percentage_of_unknown_total_payments

# len(feature_format.featureFormat(enron_data,["total_payments"]))

known_total_payments_of_poi = [1 for poi in person_of_interst_in_dataset if enron_data[poi]["total_payments"]!='NaN']

unknown_total_payments_of_poi = len(person_of_interst_in_dataset) -sum(known_total_payments_of_poi)

percentage_of_unknown_total_payments_of_poi = 100 * unknown_total_payments_of_poi/float(len(person_of_interst_in_dataset))
print "Percentage of unknown total payments of poi = ",percentage_of_unknown_total_payments_of_poi

for i in enron_data.keys():
    if enron_data[i]["bonus"]== 7000000 or enron_data[i]["bonus"] == 5600000:
        print "Name :",i
