const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');
const app = express();

app.use(cors());
app.use(express.json());

// Serve static files (HTML, CSS, JS, images, etc.)
app.use(express.static(__dirname));

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/joinform', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Flexible schema
const employeeSchema = new mongoose.Schema({}, { strict: false });
const Employee = mongoose.model('Employee', employeeSchema);

// Save form data
app.post('/api/employees', async (req, res) => {
  try {
    const employee = new Employee(req.body);
    await employee.save();
    res.status(201).json(employee);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Optional: Route for each HTML file (not strictly needed if using express.static)
// app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'new.html')));
// app.get('/nomination.html', (req, res) => res.sendFile(path.join(__dirname, 'nomination.html')));
// ...repeat for other HTML files if you want direct routes

// Start server
app.listen(8080, () => console.log('Server running on port 8080'));
