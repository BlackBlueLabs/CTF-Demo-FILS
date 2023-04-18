import hashlib



def main():
    print("This is the checker for the CTF")
    flag = input("Please enter the flag:\n")
    hashed_flag = hashlib.sha256(flag.encode('utf-8')).hexdigest()
 
    if(hashed_flag == "7a4e85edf3a5336b9634d4957159b52144b25ac830f711d15a66d8a344cd0644"):
        print("Well done! :D")
    else:
        print("Not the correct flag, try again")

if __name__ == "__main__":
    main()
    pass
        