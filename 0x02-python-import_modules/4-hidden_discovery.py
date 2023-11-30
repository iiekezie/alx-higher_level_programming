#!/usr/bin/python3
# 4-hidden_discovery.py
# Ifeanyi I Ekezie
if __name__ == "__main__":
    import hidden_4
    # interaction in each word of the list
    for name in dir(hidden_4):
        if "__" in name:
            continue
        else:
            print(name)
