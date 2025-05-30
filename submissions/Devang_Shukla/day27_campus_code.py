# day27_campus_code.py
def identify_problematic_modules(scores, threshold=50):
    # Select modules that require debugging (i.e., score < threshold)
    problematic = [score for score in scores if score < threshold]
    return problematic

# Input
input_scores = input("Please enter module scores (separated by spaces): ")
# Convert the input string into a list of integers
module_scores = list(map(int, input_scores.strip().split()))
# Process
problematic_modules = identify_problematic_modules(module_scores)
# Output
if problematic_modules:
    print("Modules needing debugging:", " ".join(map(str, problematic_modules)))
else:
    print("All modules are functioning properly!")