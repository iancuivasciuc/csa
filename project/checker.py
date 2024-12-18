import os
import argparse
import subprocess
import signal

exercises = {
    "task1": {
        "summary": "Unidimensional case.",
        "description": (
            "TODO"
        ),
        "tests": [
            ("add", 10),
            ("add_get", 10),
            ("add_delete", 10),
            ("add_get_delete", 5),
            ("add_get_delete_defragmentation", 15),
        ],
        "max_score": 50,
    },
    "task2": {
        "summary": "Bidimensional case.",
        "description": (
            "TODO"
        ),
        "tests": [
            ("add", 10),
            ("add_get_delete", 10),
            ("add_get_delete_defragmentation", 10),
        ],
        "max_score": 30,
    }
}

timeout = 300


def is_executable(path):
    # Check if the file from path is executable.
    return os.path.isfile(path) and os.access(path, os.X_OK)


def check_exercise(exercise):
    print(f"Checking {exercise}:")

    binary_path = os.path.join(".", exercise)
    tests_path = os.path.join("tests", exercise)

    if not os.path.exists(binary_path):
        print("🔴 File not found!")
        print(f"{exercise}: 0/{exercises[exercise]["max_score"]}!\n")
        return 0

    if not is_executable(binary_path):
        print("🔴 File is not executable!")
        print(f"{exercise}: 0/{exercises[exercise]["max_score"]}!\n")
        return 0

    test_score = 0

    for test in exercises[exercise]["tests"]:
        test_dir = os.path.join(tests_path, test[0])

        assert (os.path.exists(test_dir) and os.path.isdir(test_dir))

        num_tests = len(os.listdir(test_dir)) // 2
        passed = True

        for i in range(1, num_tests + 1):
            test_input = os.path.join(test_dir, f"{i}.in")
            test_output = os.path.join(test_dir, f"{i}.out")

            assert (os.path.exists(test_input) and os.path.exists(test_output))

            fin = open(test_input, "r")
            fout = open(test_output, "r")

            input_data = fin.read()
            expected_output = fout.read()

            try:
                # Run the process with input and capture output
                result = subprocess.run(
                    [binary_path],
                    input=input_data,
                    capture_output=True,
                    timeout=timeout,
                    check=True,
                    text=True,
                )

                output = result.stdout

                # Compare the program's output to the expected output
                if output != expected_output:
                    output_lines = output.splitlines()
                    expected_output_lines = expected_output.splitlines()

                    for idx in range(len(output_lines)):
                        if output_lines[idx] != expected_output_lines[idx]:
                            print(
                                f"🔴 Wrong answer at test {test_input}!\n\nOutput: \"{output_lines[idx]}\"\nExpected: \"{expected_output_lines[idx]}\"\n")

                            passed = False
                            break
            except subprocess.CalledProcessError as err:
                # Handle errors when the program exits with a non-zero status
                return_code = err.returncode

                if return_code > 0:
                    print(f"🔴 Test {test_input} exited with error code {return_code}!")
                else:
                    signal_number = -return_code
                    print(
                        f"🔴 Test {test_input} was terminated by signal: {signal.strsignal(signal_number)} (signal {signal_number})!")

                passed = False
                break
            except subprocess.TimeoutExpired:
                print(f"🔴 Test {test_input} timed out after {timeout} second!")

                passed = False
                break

        if passed:
            test_score += test[1]
            print(f"✔️ Passed test {test[0]}!")
        else:
            print(f"🔴 Failed test {test[0]}!")

    print(f"{exercise}: {test_score}/{exercises[exercise]["max_score"]}!\n")

    return test_score


def check_all_exercises():
    score, max_score = 0, 0
    for exercise in exercises:
        test_score = check_exercise(exercise)
        score += test_score
        max_score += exercises[exercise]["max_score"]

    print(f"Final grade: {score}/{max_score}!")


def show_exercise(exercise):
    exercise_info = exercises[exercise]

    print(f"Summary: {exercise_info['summary']}\n")
    print(f"Description: {exercise_info['description']}\n")


def show_all_exercises():
    for exercise in exercises:
        print(f"{exercise}: {exercises[exercise]['summary']}")


def main():
    # Setup arguments parser
    parser = argparse.ArgumentParser(
        description="Check a list of assembly exercise."
    )

    parser.add_argument(
        "-s", "--show",
        action="store_true",
        help="Display the summary, description, input/output format.",
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
