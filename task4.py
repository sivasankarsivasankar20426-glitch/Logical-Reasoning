# Rule-Based Expert System using Backward Chaining
# Student Academic Guidance

# Facts about the student
facts = {
    "GoodAttendance",
    "CompletedAssignments",
    "GoodMarks",
    "KnowsProgramming"
}

# Rules for academic guidance
rules = {
    "GoodAcademicPerformance": [
        "GoodAttendance",
        "GoodMarks"
    ],

    "EligibleForPlacement": [
        "GoodAcademicPerformance",
        "CompletedAssignments",
        "KnowsProgramming"
    ],

    "NeedsExtraPractice": [
        "CompletedAssignments",
        "GoodAttendance"
    ],

    "ReadyForInterview": [
        "EligibleForPlacement"
    ]
}

# Backward Chaining function
def backward_chaining(goal, visited=None):

    if visited is None:
        visited = set()

    print("Trying to prove:", goal)

    # Check whether goal is already a fact
    if goal in facts:
        print("  Fact found:", goal)
        return True

    # Avoid repeated checking
    if goal in visited:
        return False

    visited.add(goal)

    # Check rules that can prove the goal
    if goal in rules:

        print("  Applying rule for:", goal)

        for condition in rules[goal]:

            print("  Need to prove:", condition)

            if not backward_chaining(condition, visited):
                print("  Failed to prove:", condition)
                return False

        print("  All conditions satisfied for:", goal)
        return True

    print("  No fact or rule found for:", goal)
    return False


# Selected goal
goal = "EligibleForPlacement"

print("STUDENT ACADEMIC GUIDANCE")
print("----------------------------")
print("Goal:", goal)
print("\nReasoning Steps:")
print("----------------------------")

result = backward_chaining(goal)

print("\nFinal Conclusion")
print("----------------------------")

if result:
    print(goal, "is TRUE")
else:
    print(goal, "is FALSE")