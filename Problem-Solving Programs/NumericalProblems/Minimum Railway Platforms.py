def find_minimum_platforms(arrivals, departures):
    # Sort both lists independently to track timeline events
    arrivals.sort()
    departures.sort()
    
    # Base pointers and counters
    platform_needed = 0
    max_platforms = 0
    
    i = 0  # Pointer for arrivals
    j = 0  # Pointer for departures
    
    while i < len(arrivals) and j < len(departures):
        # If a train arrives before the previous leaves, an extra platform is needed.
        if arrivals[i] < departures[j]:
            platform_needed += 1
            i += 1
        # If a train leaves (or leaves at the exact arrival time), a platform becomes free.
        else:
            platform_needed -= 1
            j += 1
            
        # Keep track of the highest concurrent platforms needed
        max_platforms = max(platform_needed, max_platforms)
        
    return max_platforms

# --- Example Usage ---
# Train times represented in 24-hour format (e.g., 900 = 09:00, 1100 = 11:00)
train_arrivals   = list(map(int, input("Enter arrival Time (space-separated): ").split()))
train_departures = list(map(int, input("Enter Departure Time (space-separated): ").split()))

min_platforms = find_minimum_platforms(train_arrivals, train_departures)
print(f"Minimum platforms required for the trains are: {min_platforms}")
