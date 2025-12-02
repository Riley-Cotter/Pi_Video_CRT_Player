# Pi_Video_CRT_Player
Plays videos from a pi on a CRT TV

1.	For Windows
  a.	Download Ubuntu (Windows Subsystem for Linux)
Raspberry Pi Setup:
  1. Install Lite OS (using the raspberry pi imager)
    
  2. Include WIFI 
        1.	Username: LocalWIFIUsername
        2.	Password: #LocalPassword
        3.	Enable SSH
  4. Clone Repository to RaspberryPi
    a. Install Git
        i. sudo apt install git
    b. Clone Repo
  git clone https://github.com/Riley-Cotter/Pi_Video_CRT_Player.git
  6. Add Program to Startup
    5. sudo crontab -e
     @reboot /bin/sleep 1; /home/ri/Pi_Video_CRT_Player/startup.sh > /home/ri/mycronlog.txt 2>&1
  7. Give Scripts Permission to be Executable
    6. sudo chmod +x /home/ri/Pi_Video_CRT_Player/setup.sh
  8. Run Setup
    8. sudo ./Pi_Video_CRT_Player/setup.sh
  9. Sudo raspi-config
    10. Navigate to display settings, choose composite
