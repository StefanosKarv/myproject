const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
const db = require('./db'); // Assuming the file above is named db.js

// Serve static files from the "static" directory
app.use('/', express.static(path.join(__dirname, 'static')));

// Endpoint to get CPU data from the database
app.get('/get-cpus', (req, res) => {
  db.all('SELECT * FROM cpus', [], (err, rows) => {
    if (err) {
      res.status(500).send(err.message);
    } else {
      res.json(rows);
    }
  });
});

// Endpoint to get mobos data from the database
app.get('/get-mobos', (req, res) => {
  const query = 'SELECT * FROM motherboards';
  db.all(query, [], (err, rows) => {
    if (err) {
      console.error(err.message);
      res.status(500).send('Error fetching data from database');
    } else {
      res.json(rows);
    }
  });
});

// Endpoint to get GPU data from the database
app.get('/get-gpus', (req, res) => {
  db.all('SELECT * FROM gpus', [], (err, rows) => {
    if (err) {
      console.error(err.message);
      res.status(500).send('Error fetching data from database');
    } else {
      res.json(rows);
    }
  });
});


// Catch-all for undefined routes
app.use((req, res) => {
  res.status(404).send('Not Found');
});

// Start the server and log once when the server is running
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
