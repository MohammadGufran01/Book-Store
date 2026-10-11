"""
Migration script to migrate backed-up SQLite data to Neon PostgreSQL.

Usage:
1. In PowerShell:
   $env:DATABASE_URL="postgres://user:password@host/dbname?sslmode=require"
   python migrate_data_to_neon.py
"""
import os
import sys
import subprocess

def run():
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        print("[ERROR] DATABASE_URL environment variable is not set!")
        print("Please set your DATABASE_URL securely in your terminal session before running this script.")
        print("Example (PowerShell):")
        print('  $env:DATABASE_URL="postgres://user:password@host/dbname?sslmode=require"')
        print('  python migrate_data_to_neon.py')
        sys.exit(1)

    print("[1/3] Running Django migrations on persistent database...")
    res = subprocess.run([sys.executable, 'manage.py', 'migrate'], check=False)
    if res.returncode != 0:
        print("[ERROR] Migrations failed. Please verify your DATABASE_URL connectivity.")
        sys.exit(res.returncode)

    print("\n[2/3] Loading backed-up data into persistent database...")
    backup_file = 'db_data_backup.json'
    if not os.path.exists(backup_file):
        print(f"[ERROR] Backup file '{backup_file}' not found.")
        sys.exit(1)

    res = subprocess.run([sys.executable, 'manage.py', 'loaddata', backup_file], check=False)
    if res.returncode != 0:
        print("[ERROR] Data loading failed. Check schema compatibility.")
        sys.exit(res.returncode)

    print("\n[3/3] Migration completed successfully!")
    print("All books, authors, genres, reviews, users, carts, and orders have been safely loaded into your persistent database.")

if __name__ == '__main__':
    run()
