from flask import Flask, render_template, request, redirect
import query
import main

app = Flask(__name__)

@app.route("/")
def index():

    # Define a list of lists with embedded variables
    list_of_books = query.books()

    # Pass the list of lists to the template
    templateData = {'list_of_books': list_of_books}

    return render_template('boekenkiezen.html', **templateData)


@app.route("/playpause")
def playpause():

    # Get the book information from the query parameters
    bookId = request.args.get('bookId')
    title = request.args.get('title')
    img_src = request.args.get('img_src')

    templateData = {
        'bookId': bookId,
        'title' : title,
        'img_src': img_src
    }
    main.getready(bookId)
    main.start()
    return render_template('playpause.html', **templateData)



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)

