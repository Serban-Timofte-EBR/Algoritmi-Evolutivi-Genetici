#Compania Aeriana -> Metoda Backtracking
import numpy
def find_best_combination(budget=5000, prices=(100, 60, 50), autonomies=(6000, 4200, 2800), radar_ranges=(30, 48, 32)):
    best_combination = None
    max_avg_autonomy = 0

    def backtrack(a=0, b=0, c=0, spent=0, total_autonomy=0, total_radar_range=0):
        nonlocal best_combination, max_avg_autonomy

        total_planes = a + b + c
        if spent > budget or (total_planes > 0 and total_radar_range / total_planes <= 40):
            return

        if total_planes > 0:
            avg_autonomy = total_autonomy / total_planes
            if avg_autonomy > max_avg_autonomy:
                max_avg_autonomy = avg_autonomy
                best_combination = (a, b, c)

        if spent + prices[0] <= budget:
            backtrack(a + 1, b, c, spent + prices[0], total_autonomy + autonomies[0],
                      total_radar_range + radar_ranges[0])
        if spent + prices[1] <= budget:
            backtrack(a, b + 1, c, spent + prices[1], total_autonomy + autonomies[1],
                      total_radar_range + radar_ranges[1])
        if spent + prices[2] <= budget:
            backtrack(a, b, c + 1, spent + prices[2], total_autonomy + autonomies[2],
                      total_radar_range + radar_ranges[2])

    backtrack()

    return best_combination, max_avg_autonomy


best_combination, max_avg_autonomy = find_best_combination()
if best_combination:
    print(f"Cea mai bună combinație de avioane: a = {best_combination[0]}, b = {best_combination[1]}, c = {best_combination[2]}")
    print(f"Autonomia medie maximă: {max_avg_autonomy:.2f} km")
else:
    print("Nu s-a găsit o combinație care să respecte toate condițiile.")