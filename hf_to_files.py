import os
from datasets import load_dataset


CACHE_DIR = "F:/Users/kingh/.cache/huggingface/datasets"

# This dataset has no train/valid/test split
SPLIT = "train[:5]"


ds = load_dataset(
    "codeparrot/apps",
    cache_dir=CACHE_DIR,
    split=SPLIT,
)


def main():
    for row in ds:
        problem_id = row["problem_id"]
        question = row["question"]
        solutions = row["solutions"]
        input_output = row["input_output"]
        difficulty = row["difficulty"]
        url = row["url"]
        starter_code = row["starter_code"]

        folder = f"./problem_{problem_id}"

        os.makedirs(folder, exist_ok=True)

        with open(f"{folder}/question.txt", "w", encoding="utf-8") as f:
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


if __name__ == "__main__":
    main()
