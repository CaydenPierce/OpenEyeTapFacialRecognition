sudo sed -i 's/#xserver-command=X -s 0/#xserver-command=X/g' /etc/lightdm/lightdm.conf
sudo sed -i 's/#xserver-command=X/#xserver-command=X -s 0/g' /etc/lightdm/lightdm.conf
