#!/bin/bash

# Define the source and destination directories
MEDIA_SOURCE="/home/nanokernelltd/Desktop/Akshay/projects/project7/Dhanush_fan_kl53/media/"
MEDIA_DESTINATION="/home/nanokernelltd/Desktop/Akshay/projects/project7/Dhanush_fan_kl53/staticfiles/media/"

# Create the destination directory if it doesn't exist
mkdir -p "$MEDIA_DESTINATION"

# Copy the media files
cp -r "$MEDIA_SOURCE"/* "$MEDIA_DESTINATION"
