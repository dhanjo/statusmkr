!#/bin/bash
echo '#######################################################################'
echo '#                          Statusmkr Setup                            #'
echo '#######################################################################'
echo

sudo apt install git;
sudo apt install golang;
sudo git clone https://github.com/tomnomnom/httprobe;
cd httprobe;
sudo go build main.go;
sudo mv main httprobe;
sudo mv httprobe /usr/bin;
