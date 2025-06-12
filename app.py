from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True) #This should be set to true
    
    #Left of at 13:22 on Python Blog Tutorial #1 - Flask Setup and Intro