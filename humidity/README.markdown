> pip3 install flask

> sudo apt-get install jupyter

> jupyter nbconvert --to python Humidity.ipynb

> pip3 install pandas

From this directory, run:
> nohup python /home/pi/Development/raspberry-pi/humidity/Humidity.py >> humidity.csv &

For the webapp, in the webapp directory, run:
> nohup python /home/pi/Development/raspberry-pi/humidity/webapp/app.py &
