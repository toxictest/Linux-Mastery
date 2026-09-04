#!/usr/bin/env bash
# ==============================================================================
# Script Name : sysaudit.sh
# Purpose     : Autonomous Linux Host Profiling & Incident Diagnostic Collector
# Standards   : Defensive (set -euo pipefail), Zero External Dependencies
# ==============================================================================

set -euo pipefail

audit_run_id=$(date +%Y%m%d_%H%M%S)
audit_dir=$(mktemp -d "/tmp/sysaudit_${audit_run_id}.XXXXXX")

cleanup() {
  local exit_code=$?
  if [ -d "$audit_dir" ]; then
    if [ "$exit_code" -eq 0 ]; then
      tar_file="/tmp/audit_report_${audit_run_id}.tar.gz"
      tar -czf "$tar_file" -C "$audit_dir" .
      echo "[*] Audit completed successfully. Archive: $tar_file"
    else
      echo "[!] Audit aborted unexpectedly with error code: $exit_code" >&2
    fi
    rm -rf "$audit_dir"
  fi
  exit "$exit_code"
}
trap cleanup EXIT INT TERM

echo "[*] Initiating system audit. Staging in: $audit_dir"

mkdir -p "$audit_dir/system" "$audit_dir/storage" "$audit_dir/processes" "$audit_dir/network" "$audit_dir/security"

uname -a > "$audit_dir/system/kernel_uname.txt"
uptime > "$audit_dir/system/uptime.txt"
if [ -f /etc/os-release ]; then
  cp /etc/os-release "$audit_dir/system/os-release.txt"
fi
cat /proc/cpuinfo > "$audit_dir/system/cpuinfo.txt"
cat /proc/meminfo > "$audit_dir/system/meminfo.txt"

df -h > "$audit_dir/storage/disk_space.txt"
df -i > "$audit_dir/storage/disk_inodes.txt"
mount > "$audit_dir/storage/mounts.txt"

ps aux > "$audit_dir/processes/ps_aux.txt"

ip a > "$audit_dir/network/interfaces.txt"
ip r > "$audit_dir/network/routing_table.txt"
if command -v ss >/dev/null 2>&1; then
  ss -tulpn > "$audit_dir/network/listening_sockets.txt"
fi

find / -xdev -perm -4000 -type f -exec ls -la {} + 2>/dev/null > "$audit_dir/security/suid_files.txt" || true
find /etc -type f -perm -0002 -exec ls -la {} + 2>/dev/null > "$audit_dir/security/world_writable_etc.txt" || true

if command -v getcap >/dev/null 2>&1; then
  getcap -r / 2>/dev/null > "$audit_dir/security/capabilities.txt" || true
fi

if command -v journalctl >/dev/null 2>&1; then
  journalctl -p err -xb --no-pager > "$audit_dir/system/journal_errors.txt" || true
fi

echo "[+] Data collection complete. Finalizing archive package..."
