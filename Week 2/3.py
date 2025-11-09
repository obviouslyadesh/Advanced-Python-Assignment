feedback_list = [
    "This is awesome product",
    "The service was excellent but no discounts",
    "All in all, Not satisfied",
    "What to say dude, it was not upto the mark",
    "Good",
    "I got trust issues after purchasing from here",
    "Worst"
]

filtered_feedback = list(filter(lambda msg: len(msg) >= 20, feedback_list))
lowercase_feedback = list(map(lambda msg: msg.lower(), filtered_feedback))

print("Original feedback:")
for msg in feedback_list:
    print(f"- {msg}")
    
print("\nFiltered and lowercase feedback:")
for msg in lowercase_feedback:
    print(f"- {msg}")