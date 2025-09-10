from flask import Flask
app = Flask(__name__)  # applications created

@app.route('/')                   # decorator
def Hello_world():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Batman Fan Page</title>

  <style>
    /* Reset default styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      color: white;
      background: black;
    }

    /* Header */
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px 30px;
      background: rgba(0, 0, 0, 0.7);
    }

    header h1 {
      font-size: 24px;
      letter-spacing: 2px;
    }

    nav ul {
      list-style: none;
      display: flex;
      gap: 20px;
    }

    nav ul li a {
      text-decoration: none;
      color: yellow;
      font-weight: bold;
    }

    nav ul li a:hover {
      color: white;
    }

    /* Hero Section */
    .hero {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;

      /* Put your background image here */
      background: url('') no-repeat center center/cover;
    }

    .hero-text h2 {
      font-size: 48px;
      margin-bottom: 20px;
    }

    .hero-text p {
      font-size: 20px;
      margin-bottom: 30px;
    }

    .hero-text button {
      padding: 10px 20px;
      font-size: 18px;
      border: none;
      border-radius: 5px;
      background: yellow;
      color: black;
      cursor: pointer;
      font-weight: bold;
    }

    .hero-text button:hover {
      background: white;
      color: black;
    }

    /* Footer */
    footer {
      text-align: center;
      padding: 15px;
      background: rgba(0, 0, 0, 0.8);
      font-size: 14px;
      color: gray;
    }
  </style>
</head>
<body>
  <header>
    <h1>🦇 Batman</h1>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Gallery</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
  </header>

  <section class="hero">
    <div class="hero-text">
      <h2>The Dark Knight</h2>
      <p>“I am vengeance. I am the night. I am Batman.”</p>
      <button>Learn More</button>
    </div>
  </section>

  <footer>
    <p>&copy; 2025 Batman Fan Page | Made by You 🦇</p>
  </footer>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)           # run the application
