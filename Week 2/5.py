exam_scores = [45, 78, 92, 35, 67, 88, 52, 95, 41, 73, 59, 84, 30, 76]

passing_scores = list(filter(lambda score: score >= 50, exam_scores))

def score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

letter_grades = list(map(lambda score: (score, score_to_grade(score)), passing_scores))

print("All scores:", exam_scores)
print("Filtered scores:", passing_scores)
print("\nPassing scores with letter grades:")
for score, grade in letter_grades:
    print(f"- Score {score}: Grade {grade}")