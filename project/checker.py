import os
import argparse
import subprocess
import signal

exercises = {
    "task1": {
        "summary": "Unidimensional case.",
        "description": ("TODO"),
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
        "description": ("TODO"),
        "tests": [
            ("add", 10),
            ("add_get_delete", 10),
            ("add_get_delete_defragmentation", 10),
        ],
        "max_score": 30,
    },
}

timeout = 300


def is_executable(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)


def print_comparison(input_data, output, expected_output):
    print("Test Input:")
    print(input_data)
    print("Your Output:")
    print(output)
    print("Expected Output:")
    print(expected_output)


def check_exercise(exercise):
    print(f"Checking {exercise}:\n")

    binary_path = os.path.join(".", exercise)
    tests_path = os.path.join("tests", exercise)

    if not os.path.exists(binary_path):
        print("🔴 File not found!\n")
        print(f"{exercise}: 0/{exercises[exercise]['max_score']}!\n")
        return 0

    if not is_executable(binary_path):
        print("🔴 File is not executable!\n")
        print(f"{exercise}: 0/{exercises[exercise]['max_score']}!\n")
        return 0

    test_score = 0

    for test in exercises[exercise]["tests"]:
        print(f"Checking {test[0].upper()}:")

        test_dir = os.path.join(tests_path, test[0])
        assert os.path.exists(test_dir) and os.path.isdir(test_dir)

        num_tests = len([file for file in os.listdir(test_dir) if file.endswith(".in")])
        passed = True

        for i in range(1, num_tests + 1):
            test_input = os.path.join(test_dir, f"{i}.in")
            test_output = os.path.join(test_dir, f"{i}.out")

            assert os.path.exists(test_input) and os.path.exists(test_output)

            fin = open(test_input, "r")
            fout = open(test_output, "r")

            input_data = fin.read()
            expected_output = fout.read()

            try:
                result = subprocess.run(
                    [binary_path],
                    input=input_data,
                    capture_output=True,
                    timeout=timeout,
                    check=True,
                    text=True,
                )

                output = result.stdout

                if output != expected_output:
                    print(f"🔴 Test {i} failed!\n")
                    print_comparison(input_data, output, expected_output)

                    output_lines = output.splitlines()
                    expected_output_lines = expected_output.splitlines()

                    for idx in range(
                        min(len(output_lines), len(expected_output_lines))
                    ):
                        if output_lines[idx] != expected_output_lines[idx]:
                            print(f"First difference at line {idx + 1}:")
                            print(f'Your output:      "{output_lines[idx]}"')
                            print(f'Expected output:  "{expected_output_lines[idx]}"')
                            break


                    passed = False
                    break
                else:
                    print(f"✅ Test {i} passed!")

            except subprocess.CalledProcessError as err:
                return_code = err.returncode
                print(f"🔴 Test {i} failed!\n")
                print_comparison(input_data, "", expected_output)

                if return_code > 0:
                    print(f"Program exited with error code {return_code}!\n")
                else:
                    signal_number = -return_code
                    print(
                        f"Program terminated by signal: {signal.strsignal(signal_number)} (signal {signal_number})!\n"
                    )

                passed = False
                break

            except subprocess.TimeoutExpired:
                print(f"🔴 Test {i} timed out after {timeout} seconds!\n")
                print_comparison(input_data, "", expected_output)
                passed = False
                break

            fin.close()
            fout.close()

        if passed:
            test_score += test[1]
            print(f"✅ Passed all tests in {test[0].upper()}!\n")
        else:
            print(f"🔴 Failed tests in {test[0].upper()}!\n")
        
        print("-" * 80, '\n')

    print(f"{exercise}: {test_score}/{exercises[exercise]['max_score']}!\n")
    return test_score


def main():
    parser = argparse.ArgumentParser(
        description="Check assembly exercises with detailed input/output comparison."
    )

    parser.add_argument(
        "-s", "--show", action="store_true", help="Display the summary and description."
    )

    parser.add_argument(
        "exercise",
        nargs="?",
        choices=exercises.keys(),
        help="Specify an exercise to check.",
    )

    args = parser.parse_args()

    if args.exercise:
        if args.show:
            print(f"Summary: {exercises[args.exercise]['summary']}\n")
            print(f"Description: {exercises[args.exercise]['description']}\n")
        else:
            check_exercise(args.exercise)
    else:
        if args.show:
            for ex in exercises:
                print(f"{ex}: {exercises[ex]['summary']}")
        else:
            score = 0
            max_score = 0
            for ex in exercises:
                score += check_exercise(ex)
                max_score += exercises[ex]["max_score"]
            print(f"Final grade: {score}/{max_score}!")


if __name__ == "__main__":
    main()
