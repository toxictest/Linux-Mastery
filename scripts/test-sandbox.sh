#!/usr/bin/env bash
set -euo pipefail

echo "========================================================="
echo "   Linux-Mastery: Host Environment Diagnostic Verifier   "
echo "========================================================="

missing_tools=0
required_binaries=(
  git
  curl
  python3
  docker
  strace
  lsof
  tcpdump
  jq
)

echo "[*] Checking host utility dependencies..."
for bin in "${required_binaries[@]}"; do
  if command -v "$bin" >/dev/null 2>&1; then
    echo "  [✔] Found: $bin ($(command -v "$bin"))"
  else
    echo "  [✘] MISSING: $bin"
    missing_tools=$((missing_tools + 1))
  fi
done

echo "---------------------------------------------------------"
echo "[*] Checking container virtualization service..."
if command -v docker >/dev/null 2>&1; then
  if docker info >/dev/null 2>&1; then
    echo "  [✔] Docker daemon is running and accessible."
  else
    echo "  [✘] Docker is installed, but the daemon is not running or your user is not in the docker group."
    missing_tools=$((missing_tools + 1))
  fi
else
  echo "  [✘] Docker binary not found."
  missing_tools=$((missing_tools + 1))
fi

echo "---------------------------------------------------------"
if [ "$missing_tools" -eq 0 ]; then
  echo "[SUCCESS] Host system is fully qualified to run Linux-Mastery labs."
  exit 0
else
  echo "[FAILURE] $missing_tools requirements are unfulfilled. Install the missing packages and re-run this check."
  exit 1
fi
