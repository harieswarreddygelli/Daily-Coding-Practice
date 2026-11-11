# Read total seconds from input 
total_seconds = int(input())

# Calculate hours, minutes, and seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Print the result in the specified format
print(f"{hours}h {minutes}m {seconds}s")
