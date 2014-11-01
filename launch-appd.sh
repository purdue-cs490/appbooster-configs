#!/bin/bash

set -e

HOSTFWD="
tcp::1822-:22
tcp::1880-:80
"

# Container port forwards
for p in {000..099}; do
    HOSTFWD="
    $HOSTFWD
    tcp::18$p-:18$p
    "
done

netargs="user"
for hostfwd in $HOSTFWD; do
    netargs="$netargs,hostfwd=$hostfwd"
done

# Launch QEMU
cd /homes/xu227/scratch/qemu

exec /usr/bin/qemu-system-x86_64 -enable-kvm -cpu host -m 8192 -smp 16 \
-drive file=debian-appd.img,if=virtio -net nic -display none -daemonize \
-net $netargs
