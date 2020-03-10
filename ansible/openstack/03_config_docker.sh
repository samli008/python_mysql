cd /etc/systemd/system/
mkdir docker.service.d
cd docker.service.d

cat > kolla.conf << EOF
[Service]
MountFlags=shared
EOF

systemctl daemon-reload
systemctl restart docker
systemctl enable docker
