prefixes = [["kibibyte", "mebibyte", "gibibyte", "tebibyte", "pebibyte", "exbibyte"],
            ["kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte", "exabyte"]]

selected_prefix = 0

unit = input("Binary or decimal prefix: ").lower()

if unit == "binary":
    selected_prefix = 0
    multiplier = 1024
elif unit == "decimal" or unit == "denary":
    selected_prefix = 1
    multiplier = 1000

choice = input(f"{prefixes[selected_prefix]}: ").lower()

file_type = input("Image or sound file: ").lower()

if file_type == "image":
    print(f"File size: {int(input("Resolution: ")) * int(input("Colour depth: ")) / (8 * multiplier ** ((prefixes[selected_prefix].index(choice)) + 1))} {choice}s")
elif file_type == "sound":
    print(f"File size: {int(input("Sample rate")) * int(input("Resolution: ")) * int(input("Length of track (seconds): ")) / (8 * multiplier ** (prefixes[selected_prefix].index(choice) + 1))} {choice}s")
