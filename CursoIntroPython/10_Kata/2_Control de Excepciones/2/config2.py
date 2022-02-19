def main():
    try:
        open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    main()