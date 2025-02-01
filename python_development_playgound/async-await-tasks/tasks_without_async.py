import time

def brewCoffee():
    print("Start brewCoffee()")
    time.sleep(3)
    print("End brewCofee()")
    return "Coffee ready"

def toastBread():
    print("Start toastBread()")
    time.sleep(2)
    print("End toastBread()")
    return "frokost ready"

def main():
    start_time = time.time()
    
    result_coffee = brewCoffee()
    result_bread = toastBread()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of brewCofee: {result_coffee}")
    print(f"Result of toastBread: {result_bread}")
    print(f"Total Execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
