ceph osd pool create images 50
ceph osd pool create vms 50
ceph osd pool create volumes 50
ceph osd pool set images size 2
ceph osd pool set vms size 2
ceph osd pool set volumes size 2

ceph osd pool application enable images rbd
ceph osd pool application enable vms rbd
ceph osd pool application enable volumes rbd
