def google_helper(url):
  url = url[8:23]
  letters = url.split(".")
  print(letters[0].upper()+letters[1].upper()+letters[2].upper())

def main():
    print("Hello, this is the main entry point!")

if __name__ == "__main__":
    main()
    google_helper("https://docs.google.com/")