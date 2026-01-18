import os

INPUT_DIR = "NTC_training_data"
OUTPUT_FILE = "ntctraining.jsonl"

def merge_jsonl_files(input_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".jsonl"):
                    file_path = os.path.join(root, file)
                    print(f"Processing: {file_path}")

                    with open(file_path, "r", encoding="utf-8") as infile:
                        for line in infile:
                            line = line.strip()
                            if line:
                                outfile.write(line + "\n")

    print(f"\n✅ All JSONL files merged into: {output_file}")

if __name__ == "__main__":
    merge_jsonl_files(INPUT_DIR, OUTPUT_FILE)
