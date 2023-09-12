# Lab 9: Birthdays

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 9 - Lab 9: Birthdays](https://cs50.harvard.edu/x/2023/labs/9/). This guide will walk you through creating a web application using Flask to keep track of friends' birthdays. You'll use a SQLite database to store the birthday data and create a simple user interface for adding and displaying birthdays.

## Getting Started

1. Log into cs50.dev and open the terminal.
2. Navigate to the appropriate directory using the `cd` command.

## Implementation Details

### 1. Displaying Existing Birthdays

In this step, you'll modify the Flask application to display existing birthdays from the database.

1. **Update app.py**: Open the `app.py` file and modify the `/` route to query the database for existing birthdays and render them in the template.

   ```python
   @app.route("/", methods=["GET", "POST"])
   def index():
       if request.method == "POST":
           # Access form data
           name = request.form.get("name")
           month = request.form.get("month")
           day = request.form.get("day")

           # Insert data into database
           db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

           return redirect("/")

       else:
           # Query for all birthdays
           birthdays = db.execute("SELECT * FROM birthdays")

           return render_template("index.html", birthdays=birthdays)
   ```

2. **Update index.html**: Open the `index.html` file and add logic to render each birthday as a row in the table.

   ```html
   <table>
       <thead>
           <tr>
               <th>Name</th>
               <th>Birthday</th>
           </tr>
       </thead>
       <tbody>
           <!-- Loop through the database entries to display them in this table -->
           {% for birthday in birthdays %}
               <tr>
                   <td>{{ birthday.name }}</td>
                   <td>{{ birthday.month }}/{{ birthday.day }}</td>
               </tr>
           {% endfor %}
        </tbody>
   </table>
   ```

### 2. Adding New Birthdays

In this step, you'll enable users to add new birthdays to the database through a form.

1. **Update index.html**: Add an HTML form to let users input a name, birthday month, and birthday day.

   ```html
   <form action="/" method="POST">
       <input type="text" name="name" placeholder="Name">
       <input type="number" name="month" placeholder="Month" min="1" max="12">
       <input type="number" name="day" placeholder="Day" min="1" max="31">
       <input type="submit" value="Add Birthday">
   </form>
   ```

2. **Update app.py**: Add logic in the `/` route to handle the form submission and insert a new birthday into the database.

   ```python
   @app.route("/", methods=["GET", "POST"])
   def index():
       if request.method == "POST":
           name = request.form.get("name")
           month = request.form.get("month")
           day = request.form.get("day")
           db.execute("INSERT INTO birthdays (name, month, day) VALUES (:name, :month, :day)",
                      name=name, month=month, day=day)
           db.commit()
           return redirect("/")
       else:
           birthdays = db.execute("SELECT * FROM birthdays")
           return render_template("index.html", birthdays=birthdays)
   ```

## Testing

1. Run the Flask application in the terminal:

   ```bash
   flask run
   ```

2. Open your web browser and navigate to the URL shown in the terminal.

3. Test adding new birthdays through the form and ensure they appear in the table.