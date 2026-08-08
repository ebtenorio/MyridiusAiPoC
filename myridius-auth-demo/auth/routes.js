const express = require('express');
const router = express.Router();
const { showResetForm, handleReset } = require('./authController');

// Route to show reset form
router.get('/reset-password/:token', showResetForm);

// Route to handle reset form submission
router.post('/reset-password/:token', handleReset);

module.exports = router;
