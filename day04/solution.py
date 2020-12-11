import re
def get_solution_1(input):
    def is_valid(item):
        return len(item.keys()) == 8 or len(item.keys()) == 7 and "cid" not in item
    return len(list(filter( is_valid,
                input)))

def get_solution_2(input):
    def is_valid(item):
        return all([
            len(item.keys()) == 8 or len(item.keys()) == 7 and "cid" not in item,
            "byr" in item and 1920 <= int(item["byr"]) <= 2002,
            "iyr" in item and 2010 <= int(item["iyr"]) <= 2020,
            "eyr" in item and 2020 <= int(item["eyr"]) <= 2030,
            "hgt" in item and (("in" in item["hgt"] and 59 <= int(item["hgt"].replace("in","")) <= 76) or
                ("cm" in item["hgt"] and 150 <= int(item["hgt"].replace("cm","")) <= 193)),
            "hcl" in item and re.match(r"#[0-9a-f]*",item["hcl"]) and len(item["hcl"]) == 7,
            "ecl" in item and item["ecl"] in {"amb","blu","brn","gry","grn","hzl","oth"},
            "pid" in item and item["pid"].isdigit() and len(item["pid"]) == 9
        ])

    return len(list(filter( is_valid,
                input)))

def process_input(input):
    processed = map(
            lambda data: { fields.split(":")[0].strip() : fields.split(":")[1].strip()
                            for fields in data.replace("\n"," ").split(" ") }
            ,
            input.split("\n\n")
        )
    return list(processed)

input_processed = []
with open('input.txt') as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")
