import os
import argparse
import subprocess
import signal

exercises = {
    "prime": {
        "summary": "Determine if a given number is a prime number.",
        "description": (
            "The program should read a single integer as input and determine if the number is a prime number.\n"
            "- Input: A single integer `n`, where -1e9 <= n <= 1e9.\n"
            "- Output: Print `Yes` if the number is prime, otherwise print `No`."
        ),
        "example": {
            "input": "5",
            "output": "Yes",
            "explanation": "5 is a prime number because it is only divisible by 1 and 5."
        },
        "inputs": (
            "5", "0", "1", "2", "7", "49", "16", "-121", "-12", "-5", "63619949", "47334659", "20876407", "90642613",
            "40713271", "982412988", "289654629", "296575351"
        ),
        "outputs": (
            "Yes", "No", "No", "Yes", "Yes", "No", "No", "No", "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No",
            "No", "No"
        ),
    },
    "factorial": {
        "summary": "Compute the factorial of a number using recursion.",
        "description": (
            "The program should calculate the factorial of a non-negative integer `n`.\n"
            "- Input: A single integer `n`, where 0 <= n <= 12.\n"
            "- Output: Print the value of `n!` (n factorial)."
        ),
        "example": {
            "input": "5",
            "output": "120",
            "explanation": "The factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120."
        },
        "inputs": (
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12"
        ),
        "outputs": (
            "1", "1", "2", "6", "24", "120", "720", "5040", "40320", "362880", "3628800", "479001600"
        )
    },
    "binsearch": {
        "summary": "Find the last occurrence of an element in an array using binary search.",
        "description": (
            "Write a function that performs a binary search to find the index of a target value in a sorted array.\n"
            "If the value appears multiple times, the function should return the index of its last occurrence.\n"
            "- Input: The first line contains two integers, `n` (number of elements) and `x` (target). The second line contains the sorted array `arr` of `n` integers.\n"
            "1 <= n <= 1000, -1e9 <= arr[i] <= 1e9\n"
            "- Output: The index of the last occurrence of `x` in the array. If `x` is not found, return -1."
        ),
        "example": {
            "input": "6 2\n1 2 2 2 3 4 5",
            "output": "3",
            "explanation": "The target value 2 appears at indices 1, 2, and 3. The last occurrence is at index 3."
        },
        "inputs": (
            "6 2\n1 2 2 2 3 4", "9 3\n1 2 2 3 3 4 4 4 5", "8 1\n-10 -5 -5 0 1 2 3 5", "7 4\n-7 -5 -1 0 2 3 4",
            "10 7\n1 2 3 4 5 6 7 7 7 8", "6 20\n10 20 20 30 40 50", "5 -3\n-10 -5 -3 -3 0", "4 2\n1 2 2 2",
            "5 5\n1 2 3 4 5", "3 6\n1 2 3"
        ),
        "outputs": (
            "3", "4", "4", "6", "8", "2", "3", "3", "4", "-1"
        )
    },
    "palindrome": {
        "summary": "Check if a given string is a palindrome.",
        "description": (
            "A palindrome is a string that reads the same forward and backward.\n"
            "- Input: A single string `s` (1 <= len(s) <= 100) consisting only of lowercase English letters.\n"
            "- Output: Print `Yes` if the string is a palindrome, otherwise print `No`."
        ),
        "example": {
            "input": "radar",
            "output": "Yes",
            "explanation": "The string 'radar' reads the same forward and backward, so it is a palindrome."
        },
        "inputs": (
            "radar", "hello", "level", "rotor", "civic", "noon", "palindrome", "abcba", "abccba", "abcdefgh", "a", "aa",
            "ab", "xyzzyx", "xyzzx"
        ),
        "outputs": (
            "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "No"
        )
    },
    "minimax": {
        "summary": "Find the maximum of the column minimums in a matrix.",
        "description": (
            "The program should calculate the minimum value from each column of a matrix "
            "and then print the maximum of these minimum values.\n"
            "- Input: The first line contains two integers `n` (number of rows) and `m` (number of columns), where 1 <= n, m <= 100.\n"
            "The next `n` lines each contain `m` integers, the elements of the matrix, where -1e9 <= matrix[i][j] <= 1e9.\n"
            "- Output: Print the maximum of the column minimums."
        ),
        "example": {
            "input": "3 3\n1 2 3\n4 5 6\n7 8 9",
            "output": "3",
            "explanation": (
                "The minimums of the columns are: 1, 2, and 3. The maximum of these minimums is 3."
            )
        },
        "inputs": (
            "3 3\n1 2 3\n4 5 6\n7 8 9",
            "2 2\n-1 -2\n-3 -4",
            "4 4\n10 15 20 25\n5 8 12 18\n3 6 9 12\n7 14 21 28",
            "3 3\n-5 -5 -5\n-5 -5 -5\n-5 -5 -5",
            "1 5\n3 1 4 1 5",
            "5 1\n2\n3\n5\n1\n4",
            "3 3\n0 0 0\n1 1 1\n2 2 2",
            "2 3\n10 20 30\n-10 -20 -30"
        ),
        "outputs": (
            "3", "-3", "12", "-5", "5", "1", "0", "-10"
        )
    }
}


max_exercise_len = max(len(exercise) for exercise in exercises)
timeout = 5


def is_executable(path):
    # Check if the file from path is executable.
    return os.path.isfile(path) and os.access(path, os.X_OK)


def check_exercise(exercise):
    print(f"Checking {exercise:<{max_exercise_len}}:", end=" ")

    path = "./" + exercise

    if not os.path.exists(path):
        print("🔴 File not found!")
        return

    if not is_executable(path):
        print("🔴 File is not executable!")
        return

    assert len(exercises[exercise]["inputs"]) == len(exercises[exercise]["outputs"])

    # Iterate through test cases
    for index, input_data in enumerate(exercises[exercise]["inputs"]):
        try:
            # Run the process with input and capture output
            result = subprocess.run(
                [path],
                input=input_data,
                capture_output=True,
                timeout=timeout,
                check=True,
                text=True,
            )

            output = result.stdout.strip()
            expected_output = exercises[exercise]["outputs"][index].strip()

            # Compare the program's output to the expected output
            if output != expected_output:
                print(
                    f"🔴 Wrong answer at test {index}!\n\nInput: \"{input_data}\"\nOutput: \"{output}\"\nExpected: \"{expected_output}\"\n")
                return
        except subprocess.CalledProcessError as err:
            # Handle errors when the program exits with a non-zero status
            return_code = err.returncode

            if return_code > 0:
                print(f"🔴 Test {index} exited with error code {return_code}!")
            else:
                signal_number = -return_code
                print(
                    f"🔴 Test {index} was terminated by signal: {signal.strsignal(signal_number)} (signal {signal_number})!")
            return
        except subprocess.TimeoutExpired:
            print(f"🔴 Test {index} timed out after {timeout} second!")
            return

    print(f"✔️ All tests passed!")


def check_all_exercises():
    for exercise in exercises:
        check_exercise(exercise)


def show_exercise(exercise):
    exercise_info = exercises[exercise]

    print(f"Summary: {exercise_info['summary']}\n")
    print(f"Description: {exercise_info['description']}\n")
    print(f"Example:")
    print(f"- Input: {exercise_info['example']['input']}")
    print(f"- Output: {exercise_info['example']['output']}")
    print(f"- Explanation: {exercise_info['example']['explanation']}")


def show_all_exercises():
    for exercise in exercises:
        print(f"{exercise}: {exercises[exercise]['summary']}")


def main():
    # Setup arguments parser
    parser = argparse.ArgumentParser(
        description="Check a list of assembly exercises."
    )

    parser.add_argument(
        "-s", "--show",
        action="store_true",
        help="Display the summary, description, input/output format, and an example for the specified exercise.",
    )

    parser.add_argument(
        "exercise",
        nargs="?",
        choices=exercises.keys(),
        help="Specify an exercise to check or view its details.",
    )

    # Parse arguments
    args = parser.parse_args()

    if args.exercise:
        # If an exercise is specified
        if args.show:
            show_exercise(args.exercise)
        else:
            check_exercise(args.exercise)
    else:
        # If no exercise is specified
        if args.show:
            show_all_exercises()
        else:
            check_all_exercises()


if __name__ == "__main__":
    main()
