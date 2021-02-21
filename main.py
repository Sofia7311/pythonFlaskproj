# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask

app = Flask(__name__)
@app.route("/")
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    return "HELLO!!!"  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
