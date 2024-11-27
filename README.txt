For Running this project there are some prerequisite for set up of environment
1. Download & Install Xampp for running app locally
2. Download & Install Python3

Steps:-
1. After downloading Xampp copy project_files folder in C:\xampp\htdocs 

2. Create Database
	1. start Xampp control panel and start Apache and SQL server
	2. After sucessfully starting it open your browser and type http://localhost/phpmyadmin/
	3. On left side panel click on new and create database name cec and in that create table name data
	4. In that table create coloumns as follows:-
		id Primary	int(11)				No	None				AUTO_INCREMENT
		datetime	timestamp				No	current_timestamp()	ON UPDATE CURRENT_TIMESTAMP()
		temp		int(11)				No	None			
		humi		int(11)				No	None			
		node_id	text	utf8mb4_general_ci	No	None			
		device	text	utf8mb4_general_ci	No	None		

3. Starting the web app service write in new tab of browser "http://localhost/project_files/main.php" this will show your frontend part

4. open sender.py file and the ip address with your machines ip (to get the ip on your machine open new command prompt and write command "ipconfig". Copy IPV4 address of internet providing mediam (ie. wifi, ethernet). paste it to sender.py ip. there is sample data written you can manipulate it. 

5. Open data entry folder and run terminal in it.

6. first run "python recieve.py" command. Here data is recieved to your machine sucessfull and stored in data base.You can send  entries by running "python send_data_to_vm_from_gateway.py" command in command prompt of gateway.

7. for checking new entries open "http://localhost/project_files/main.php" will be seen here and for checking data through filters till current date you can click on "see Other Details".

8. Send data to gateway through putty and on gateway copy the file named "recieve_from_node.py" which in in data entry folder. Run command "python recieve_from_node.py" on gateway so that data will be recieved on the gateway through sensor. Run "python send_data_to_vm_from_gateway.py" on another terminal on gateway. before running file beware of changing ip address on cloud vm in the python file.

Use Cases of the IoT Data Pipeline:
Smart Agriculture:
In agriculture, this system can monitor environmental conditions like temperature and humidity to optimize crop growth. Farmers can use this data to make informed decisions about irrigation, fertilization, and pest control.

Environmental Monitoring:
The system can be used for monitoring air quality, temperature, humidity, or pollution levels in various environments (e.g., cities, forests, industrial zones), enabling authorities to take preventive actions.

Industrial Automation:
This project is useful in industries for monitoring machines or equipment in real-time. It can track factors like temperature, humidity, and machine status, enabling predictive maintenance and reducing downtime.

Smart Buildings:
Used in smart buildings to collect sensor data (temperature, humidity, etc.) for HVAC systems, lighting, and energy optimization. The system ensures efficient energy usage and better indoor air quality.

Supply Chain and Logistics:
In logistics, IoT sensors can monitor the condition of goods in transit, such as temperature-sensitive pharmaceuticals or food products. Real-time data allows businesses to maintain optimal conditions and traceability.