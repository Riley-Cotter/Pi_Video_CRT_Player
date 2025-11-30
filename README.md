# Pi_Video_CRT_Player
Plays videos from a pi on a CRT TV

1.	For Windows
  a.	Download Ubuntu (Windows Subsystem for Linux)
Raspberry Pi Setup:
  1. Install Lite OS (using the raspberry pi imager)
     a.	Include WIFI 
        1.	Username: LocalWIFIUsername
        2.	Password: #LocalPassword
        3.	Enable SSH
  3. Clone Repository to RaspberryPi
    a. Install Git
        i. sudo apt install git
    b. Clone Repo
        i. git clone https://github.com/Riley-Cotter/Pi_Video_CRT_Player.git
  4. Add Program to Startup
    a.	sudo crontab -e
    b.	For Client
      i.	@reboot /bin/sleep 1; /home/ri/stepmom_tv/startup_client.sh > /home/ri/mycronlog.txt 2>&1
    c.	For Brain
      i.	@reboot /bin/sleep 1; /home/ri/stepmom_tv/startup_brain.sh  > /home/ri/mycronlog.txt 2>&1
  5. Give Scripts Permission to be Executable
    a.	sudo chmod +x /home/ri/stepmom_tv/setup.sh
  6. Run Setup
    a.	sudo ./setup.sh
  7. Sudo raspi-config a. Navigate to display settings, choose composite
