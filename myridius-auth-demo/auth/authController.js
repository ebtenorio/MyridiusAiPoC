exports.showResetForm = (req, res) => {
  // In real app: validate token
  res.sendFile('resetPassword.html', { root: 'views' });
};

exports.handleReset = (req, res) => {
  const { password } = req.body;
  // In real app: update DB with new password
  res.send('Password reset successful!');
};
