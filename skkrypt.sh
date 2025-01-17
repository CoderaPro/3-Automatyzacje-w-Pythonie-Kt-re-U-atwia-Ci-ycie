#!/bin/bash
input_folder="input_images"
output_folder="processed_images"

mkdir -p "$output_folder"
for file in "$input_folder"/*; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file")
        new_filename="${filename%.*}_mod.${filename##*.}"
        cp "$file" "$output_folder/$new_filename"
    fi
    echo "Processed: $filename -> $new_filename"
done
echo "Automation completed. All files have been copied to $output_folder."


