justice_league = ["superman", "batman", "wonder woman", "flash", "aquaman", "green lantern"]

# Find the indices of "aquaman" and "flash"
index_flash = justice_league.index("flash")

# Move "green lantern" between "aquaman" and "flash"
justice_league.remove("green lantern")
justice_league.insert(index_flash + 1, "green lantern")

print(justice_league)
