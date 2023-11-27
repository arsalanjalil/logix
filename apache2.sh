echo "checking apache2 configuration \n"
sudo systemctl status  apache2
echo "apche2 will restart ...\n"
sudo service apache2 restart
