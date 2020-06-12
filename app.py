from utils import process_item

if __name__ == "__main__":
    x = input()
    while (x):
        if x.lower()=="q":
            exit()
        print(process_item(int(x)))
        x = input()
