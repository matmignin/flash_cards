#!/usr/bin/env python3
from quiz import app

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
