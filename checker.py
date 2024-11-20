import os
import argparse
import subprocess
import signal

"""
Dictionary mapping each exercise name to its test data, including:
- 'summary': 
- 'description': 
- 'example': 
- 'inputs': A tuple of input values for the exercise.
- 'outputs': A tuple of expected outputs corresponding to the inputs.
"""
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
        "inputs": ("5", "0", "1", "2", "7", "49", "16", "-121", "-12", "-5"),
        "outputs": ("Yes", "No", "No", "Yes", "Yes", "No", "No", "No", "No", "No"),
    },
    "fibonacci": {
        "summary": "Thinking about it",
        "description": (
            "Here too"
        ),
        "example": {

        },
        "inputs": ("5", "0"),
        "outputs": ("21", "0"),
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
                    f"🔴 Wrong answer at test {index}!\n\tInput: \"{input_data}\"\n\tOutput: \"{output}\"\n\tExpected: \"{expected_output}\"")
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
