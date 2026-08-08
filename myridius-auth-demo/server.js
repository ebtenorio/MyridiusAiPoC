const express = require('express');
const bodyParser = require('body-parser');
const authRoutes = require('./auth/routes');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('views'));

app.use('/auth', authRoutes);

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
