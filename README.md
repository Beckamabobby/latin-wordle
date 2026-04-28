# Latin Wordle

A Wordle-style vocabulary game for Latin students, built for the Latin program at Bentley Upper School (Lafayette, CA).

## Why this exists

The original Latin Wordle, maintained by classics scholars, rotated its puzzle on a global daily schedule. This made it difficult to use in a classroom setting where different class periods needed to play the same word on the same day, or where a teacher wanted to align puzzles with a specific lesson or unit.

Latin Wordle addresses that gap by letting teachers schedule and inject their own words, while still offering a ready-to-play vocabulary set derived from the original.

## Features

- **Teacher-controlled custom words.** An input field lets a teacher type in a word of their choice. Once submitted, the field clears itself, so the screen is safe to project to the class before the round begins.
- **Curated vocabulary fallback.** Ships with a Latin vocabulary set scraped from the original scholar-maintained Latin Wordle, so the game is playable without any setup.
- **Easy reset.** Rounds can be restarted without a full page reload or server-side intervention — useful mid-class.
- **Classic Wordle feedback.** Green/yellow/gray letter coloring for correct, present, and absent letters.

## Stack

- **Backend:** Python, Flask
- **Frontend:** Server-rendered HTML templates with static CSS/JS
- **Deployment:** WSGI entry point (`wsgi.py`) and `Procfile` for Heroku-style platforms

## Running locally

```bash
pip install -r requirements.txt
python wsgi.py
```

The app will start on `http://localhost:5000`.

## Project structure

```
app/         Flask application code
static/      CSS, JS, and static assets
templates/   Jinja2 HTML templates
wsgi.py      Production entry point
Procfile     Deployment configuration
```

## Status

Built in 2023 over a few months of spare time during high school, and used in classroom instruction at Bentley. When I graduated, I handed the code off to the CS teacher; any ongoing maintenance or deployment is on the school's side. Open issues on this repository are minor TODOs I noted but did not prioritize before handoff.

## License

MIT — see [LICENSE](LICENSE).
