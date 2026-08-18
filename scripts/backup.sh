#!/usr/bin/env sh
set -eu
: "${DATABASE_URL:?DATABASE_URL must be set}"
backup_file="olqn-$(date +%Y%m%d-%H%M%S).dump"
pg_dump --format=custom --file="$backup_file" "$DATABASE_URL"
echo "$backup_file"
