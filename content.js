const readline = require('readline');
const fs = require('fs');
const { exec } = require('child_process');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const outputFilePath = 'data.txt';

// Prompt user for input
rl.question('Enter text to append to the file: ', (userInput) => {
  // Append user input to the text file
  fs.appendFileSync(outputFilePath, userInput + '\n');

  // Run shell command to push updates to git repo
  const gitCommand = 'git add data.txt && git commit -m "Update data" && git push origin main';
  exec(gitCommand, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing git command: ${error.message}`);
      return;
    }
    console.log(`Git command output: ${stdout}`);
  });

  console.log(`Text "${userInput}" appended to ${outputFilePath}`);
  
  // Close the readline interface
  rl.close();
});
