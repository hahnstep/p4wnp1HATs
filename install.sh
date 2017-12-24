#!/bin/sh

#sudo apt-get install -y python-blinkt
#sudo pip install watchdog

if [ ! -f /etc/systemd/system/P4wnP1-HAT.service ]; then
        echo "Injecting P4wnP1 HAT startup script..."
        cat <<- EOF | sudo tee /etc/systemd/system/P4wnP1-HAT.service > /dev/null
                [Unit]
                Description=P4wnP1 HAT Support Service
                #After=systemd-modules-load.service
                After=local-fs.target
                DefaultDependencies=no
                #Before=sysinit.target
		Before=P4wnP1.service

                [Service]
                #Type=oneshot
                Type=forking
                RemainAfterExit=yes
                ExecStart=/bin/sh /home/pi/P4wnP1/p4wnp1HATs/HAT.service.sh
                StandardOutput=journal+console
                StandardError=journal+console

                [Install]
                WantedBy=multi-user.target
                #WantedBy=sysinit.target
EOF
fi

sudo systemctl enable P4wnP1-HAT.service

