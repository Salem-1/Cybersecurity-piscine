#!/bin/sh

# pip install pyinstaller

# pyinstaller --onefile ft_otp.py

pip install -r requirments.txt
export ENCRYPTION_KEY=$"(python generate_encryption_key.py)"


