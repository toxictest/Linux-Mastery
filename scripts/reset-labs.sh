#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
compose_file="$repo_root/lab-environment/docker-compose.yml"

if [ ! -f "$compose_file" ]; then
  echo "[-] Missing compose file: $compose_file" >&2
  exit 1
fi

echo "[*] Stopping existing lab environment..."
docker compose -f "$compose_file" down --remove-orphans --volumes || true

echo "[*] Rebuilding clean lab environment..."
docker compose -f "$compose_file" up -d --build

echo "[*] Current lab status:"
docker compose -f "$compose_file" ps
