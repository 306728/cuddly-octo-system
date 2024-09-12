def v(b):
    if b[1:].count("1") % 2 == 0:
        if int(b[0]) == 1:
            return "Parity bit should be 0."
        else:
            return "No errors occurred during transmission."
    else:
        if int(b[0]) == 0:
            return "Parity bit should be 1."
        else:
            return "No errors occurred during transmission."

print(v(input()))
