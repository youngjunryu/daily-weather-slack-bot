import sys


def forecast():
    # TODO: Implement forecast function
    print("Forecasting...")


def run():
    if len(sys.argv) < 2:
        print("Usage: python controller.py forecast")
        return

    if sys.argv[1] == "forecast":
        forecast()


if __name__ == "__main__":
    run()
