import json

# JSONファイルからJSONLファイルへの変換と内容の変更
def json_to_modified_jsonl(json_file_name, output_jsonl_file_name):
    with open(json_file_name, "r", encoding="utf-8") as json_file, open(output_jsonl_file_name, "w", encoding="utf-8") as jsonl_file:
        data = json.load(json_file)
        for item in data:
            # "instruction" フィールドを "text" フィールドに変更
            item["text"] = item["instruction"]
            del item["instruction"]
            
            # "input" フィールドを "text" フィールドに追加
            item_input = {"text": item["input"]}
            del item["input"]
            
            # "output" フィールドを "text" フィールドに追加
            item_output = {"text": item["output"]}
            del item["output"]
            
            # JSONLファイルに書き込む
            jsonl_file.write(json.dumps(item, ensure_ascii=False) + "\n")
            jsonl_file.write(json.dumps(item_input, ensure_ascii=False) + "\n")
            jsonl_file.write(json.dumps(item_output, ensure_ascii=False) + "\n")

# JSONからJSONLへの変換と内容の変更
json_to_modified_jsonl("alpaca_cleaned_ja.json", "output2.jsonl")

print("変換が完了しました。")