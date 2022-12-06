def read_id(donor_id: str) -> int:
    with open(donor_id, "r", encoding = "utf-8") as file:
        id = file.read()
    return id