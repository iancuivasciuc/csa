import os
import subprocess
import signal

"""Dictionary mapping each exercise name to its test data, including:
- 'inputs': A tuple of input values for the exercise.
- 'outputs': A tuple of expected outputs corresponding to the inputs."""
exercises = {
    "./prime": {
        "inputs": ("1", "2", "3", "4", "5", "6", "7", "8"),
        "outputs": ("No", "Yes", "No", "Yes", "Yes", "No", "Yes", "No"),
    },
}

max_exercise_len = max(len(exercise) for exercise in exercises)
timeout = 5


def is_executable(file):
    # Check if file is executable.
    return os.path.isfile(file) and os.access(file, os.X_OK)


def check_exercise(exercise):
    print(f"Checking {exercise:<{max_exercise_len}}:", end=" ")

    if not os.path.exists(exercise):
        print("🔴 File not found!")
        return

    if not is_executable(exercise):
        print("🔴 File is not executable!")
        return

    assert len(exercises[exercise]["inputs"]) == len(exercises[exercise]["outputs"])

    # Iterate through test cases
    for index, input_data in enumerate(exercises[exercise]["inputs"]):
        input_with_newline = input_data + "\n"

        try:
            # Run the process with input and capture output
            result = subprocess.run(
                [exercise],
                input=input_with_newline,
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


def main():
    current_dir = os.getcwd()
    print(f"Checking executables in: {current_dir}")

    for exercise in exercises:
        check_exercise(exercise)


if __name__ == "__main__":
    main()
