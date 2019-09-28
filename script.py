from bs4 import BeautifulSoup
import requests
import re 
import csv	

#getting the html file using bs4
def get_html():
	response = requests.get('https://rera.delhi.gov.in/registered_agents_list')
	soup = BeautifulSoup(response.content, 'lxml')

	new = open("index.html" , "w")
	new.write(str(soup))
	new.close()

#get_html()

#getting details of registered agents
def get_registered_agents():
 	for id in range(17):
		response = requests.get('https://rera.delhi.gov.in/registered_agents_list?page='+str(id))
 		soup = BeautifulSoup(response.content, 'lxml')
 		
		# registration_details_table_trs = soup.find_all('tr')
		# 	 for tr in registration_details_table_trs:
		# 	 	#data.append(tr)
		# 	 	tds = tr.find_all('td')
		# 	 	for td in tds:
		# 	 		print(td.get_text().strip())
	
		rows = soup.find_all("tr")
		#storing data into csv file
		csv_other = open('other.csv', 'a')
	 	csv_individial = open('individual.csv', 'a')
	 	writer_other = csv.writer(csv_other)
	 	writer_individual = csv.writer(csv_individial)
	 	if id == 0:
	 		data = rows[0].find_all('th')
	 		csv_row = []
		 	for cell in data:
				csv_row.append(cell.get_text().encode('utf-8'))
			writer_other.writerow(csv_row)
	 		csv_row = []
		 	for cell in data:
				csv_row.append(cell.get_text().encode('utf-8'))
			writer_individual.writerow(csv_row)
	 	rows.pop(0)

	 	# csv_other = csv.writer(csv_other)
	 	# csv_individial = csv.writer(csv_individial)
	 	try:
	 		for row in rows:
	 			data = row.find_all('td')
	 			if data[4].get_text().strip() == 'Other Than Individual':
 					csv_row = []
	 				for cell in data:
	 					csv_row.append(cell.get_text().encode('utf-8'))
	 				writer_other.writerow(csv_row)
	 			else:
 					csv_row = []
	 				for cell in data:
	 					csv_row.append(cell.get_text().encode('utf-8'))
	 				writer_individual.writerow(csv_row)
	 	finally:
	 		csv_other.close()
	 		csv_individial.close() 		 		
				
get_registered_agents()	