function greeting(name = "learner") {
  const cleanName = name.trim() || "learner";
  return `Hello, ${cleanName}! Welcome to Copilot Skills Lab.`;
}

if (require.main === module) {
  console.log(greeting("JavaScript learner"));
}

module.exports = { greeting };
