const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.post("/api/summarize-email", (req, res) => {
  const { subject, body } = req.body;

  // Simulate a summary for now
  const summary = `Summary of email: Subject is "${subject}" and body is approximately ${body.length} characters long.`;

  res.json({ summary });
});

app.get("/", (req, res) => {
  res.send("Webhook is live!");
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
