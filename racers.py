
def non_winners(races):
    winners = set()
    loosers = set()

    for value in races.values():
        winners.add(value[0])
        loosers.add(value[1])
        loosers.add(value[2])
    
    for winner in winners:
        if winner in loosers:
            loosers.remove(winner)

    return loosers

# Time complexity:  O(R) - R = number of races
# Space complexity: O(R)

    
print(non_winners({
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}))




races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()

print("All tests passed! Discuss time/space complexity if time remains")