import os
import json
from datasets import load_dataset


CACHE_DIR = "F:/Users/kingh/.cache/huggingface/datasets"

# Only first 100
SPLIT = "train[:100]"


ds = load_dataset(
    "codeparrot/apps",
    cache_dir=CACHE_DIR,
    split=SPLIT,
)


def main():
    for row in ds:
        problem_id = row["problem_id"]
        question = row["question"]
        url = row["url"]
        difficulty = row["difficulty"]
        starter_code = row["starter_code"]
        solutions = json.loads(row["solutions"])
        input_output = json.loads(row["input_output"])

        folder = f"./problem_{problem_id}"

        os.makedirs(folder, exist_ok=True)
        os.makedirs(f"{folder}/solutions", exist_ok=True)
        os.makedirs(f"{folder}/input_output", exist_ok=True)

        with open(f"{folder}/question.md", "w", encoding="utf-8") as f:
            f.write(question)
            f.write("\n")

        with open(f"{folder}/url.txt", "w", encoding="utf-8") as f:
            f.write(url)
            f.write("\n")

        with open(f"{folder}/difficulty.txt", "w", encoding="utf-8") as f:
            f.write(difficulty)
            f.write("\n")

        with open(f"{folder}/starter_code.py", "w", encoding="utf-8") as f:
            f.write(starter_code)
            f.write("\n")

        for i, solution in enumerate(solutions):
            with open(
                f"{folder}/solutions/solution_{i}.py", "w", encoding="utf-8"
            ) as f:
                f.write(solution)
                f.write("\n")

        for i, (input, output) in enumerate(
            zip(input_output["inputs"], input_output["outputs"])
        ):
            with open(
                f"{folder}/input_output/input_{i}.txt", "w", encoding="utf-8"
            ) as f:
                f.write(input)
                # f.write("\n")
            with open(
                f"{folder}/input_output/output_{i}.txt", "w", encoding="utf-8"
            ) as f:
                f.write(output)
                # f.write("\n")


if __name__ == "__main__":
    main()
