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
       git clone https://github.com/Riley-Cotter/Pi_Video_CRT_Player.git
  5. Add Program to Startup
    5. sudo crontab -e
     @reboot /bin/sleep 1; /home/ri/stepmom_tv/startup.sh > /home/ri/mycronlog.txt 2>&1
  6. Give Scripts Permission to be Executable
    6. sudo chmod +x /home/ri/Pi_Video_CRT_Player/setup.sh
  7. Run Setup
    8. sudo ./setup.sh
  9. Sudo raspi-config
    10. Navigate to display settings, choose composite
