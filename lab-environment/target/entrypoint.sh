#!/usr/bin/env bash
set -euo pipefail

echo "[*] Initializing intentional break-fix scenarios on target..."

cp /bin/cp /usr/local/bin/backup_cp
chmod 4755 /usr/local/bin/backup_cp

echo "SYSTEM_FLAG_STATUS=UNLOCKED" > /etc/system_status.conf
chmod 666 /etc/system_status.conf

mkdir -p /var/run/sshd
ssh-keygen -A
/usr/sbin/sshd

echo "[+] Target ready. Bound to sandbox network at 172.28.0.20."
exec tail -f /dev/null
