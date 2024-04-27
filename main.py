from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def guess_game():
    """
    Main part of the program that is guessing user's number.
    User hints computer if it's too small or too big, user musn't cheat.
    :return: The user's guessed number.
    """
    start_form = """
                    <html>
                        <head>
                            <title>Guessing Game</title>
                        </head>
                        <body>
                            <form action="" method="POST">
                                <label>Think of a number between 0 and 1000 and I will guess it!</label>
                                <br>
                                <input type="submit" value="PLAY">
                                <input type="hidden" name="min" value="{}">
                                <input type="hidden" name="max" value="{}">
                            </form>
                        </body>
                    </html>  
    """
    form = """
        <html>
            <head>
                 <title>Guessing Game</title>
            </head>
            <body>
                <form action="" method="POST">
                <label>I'm guessing: {guess}</label>
                <input type="submit" name="hint" value="Too small">
                <input type="submit" name="hint" value="Too big">
                <input type="submit" name="hint" value="You won!">
                <input type="hidden" name="min" value="{min}">
                <input type="hidden" name="max" value="{max}">
                <input type="hidden" name="guess" value="{guess}">
            </body>
        </html>
    """
    finish_form = """
                <html>
                    <head>
                        <title>Guessing Game</title>
                    </head>
                    <body>
                        <label>
                        You're number is {guess}!
                        </label>
                    </body>
                </html>
    """

    if request.method == "GET":
        return start_form.format(0, 1000)
    else:
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        guess = int(request.form.get("guess"))
        hint = request.form.get("hint")

        if hint == "Too small":
            min = guess
        elif hint == "Too big":
            max = guess
        elif hint == "You won!":
            return finish_form.format(guess=guess)

        guess = (max - min) // 2 + min

        return form.format(guess=guess, min=min, max=max)

if __name__ == "__main__":
    app.run(debug=True)












































