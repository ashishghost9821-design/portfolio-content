import json
import shutil
import sys

CONTENT_FILE = "content.json"

PROJECTS = {

"project01": {
"steps": [
    {"type": "input", "prompt": "What item would you like to buy?: ", "key": "item", "inputType": "text"},
    {"type": "input", "prompt": "What is the price for each?: ", "key": "price", "inputType": "number"},
    {"type": "input", "prompt": "How many would you like?: ", "key": "quantity", "inputType": "number"}
],
"compute": """
const total = inputs.price * inputs.quantity;
return `\nYou have bought ${inputs.quantity} ${inputs.item}\nTotal: $${total.toFixed(2)}`;
""".strip()
},

"project02": {
"steps": [
    {"type": "input", "prompt": "Enter an adjective (description): ", "key": "adjective1", "inputType": "text"},
    {"type": "input", "prompt": "Enter a noun (animal or person): ", "key": "noun", "inputType": "text"},
    {"type": "input", "prompt": "Enter an adjective (description): ", "key": "adjective2", "inputType": "text"},
    {"type": "input", "prompt": "Enter a verb (ending with -ing): ", "key": "verb", "inputType": "text"},
    {"type": "input", "prompt": "Enter an adjective (description): ", "key": "adjective3", "inputType": "text"}
],
"compute": """
return `\nThe ${inputs.adjective1} ${inputs.noun} was ${inputs.adjective2} ${inputs.verb} in the ${inputs.adjective3} forest.`;
""".strip()
},

"project03": {
"steps": [
    {"type": "input", "prompt": "Enter the radius: ", "key": "radius", "inputType": "number"}
],
"compute": """
const PI = 3.14159;
const area = PI * Math.pow(inputs.radius, 2);
const surfaceArea = 4 * PI * Math.pow(inputs.radius, 2);
const volume = (4.0 / 3.0) * PI * Math.pow(inputs.radius, 3);
return `Area:         ${area.toFixed(2)}\nSurface Area: ${surfaceArea.toFixed(2)}\nVolume:       ${volume.toFixed(2)}`;
""".strip()
},

"project04": {
"steps": [
    {"type": "input", "prompt": "Enter the principal (P): ", "key": "principal", "inputType": "number"},
    {"type": "input", "prompt": "Enter the interest rate % (r): ", "key": "rate", "inputType": "number"},
    {"type": "input", "prompt": "Enter the # of years (t): ", "key": "years", "inputType": "number"},
    {"type": "input", "prompt": "Enter # of times compounded per year (n): ", "key": "timesCompounded", "inputType": "number"}
],
"compute": """
const rate = inputs.rate / 100;
const total = inputs.principal * Math.pow(1 + rate / inputs.timesCompounded, inputs.timesCompounded * inputs.years);
return `After ${inputs.years} years, the total will be: $${total.toFixed(2)}`;
""".strip()
},

"project05": {
"steps": [
    {"type": "input", "prompt": "1. Kilograms to Pounds\n2. Pounds to Kilograms\nEnter your choice (1 or 2): ", "key": "choice", "inputType": "number"},
    {"type": "input", "prompt": "Enter the weight to convert: ", "key": "weight", "inputType": "number"}
],
"compute": """
if (inputs.choice === 1) {
  const pounds = inputs.weight * 2.20462;
  return `${inputs.weight.toFixed(2)} kg is equal to ${pounds.toFixed(2)} lbs`;
} else if (inputs.choice === 2) {
  const kilograms = inputs.weight / 2.20462;
  return `${inputs.weight.toFixed(2)} lbs is equal to ${kilograms.toFixed(2)} kg`;
} else {
  return `Invalid choice! Please enter 1 or 2`;
}
""".strip()
},

"project06": {
"steps": [
    {"type": "input", "prompt": "C. Celsius to Fahrenheit\nF. Fahrenheit to Celsius\nIs the temp in Celsius (C) or Fahrenheit (F)?: ", "key": "choice", "inputType": "text"},
    {"type": "input", "prompt": "Enter the temperature: ", "key": "temp", "inputType": "number"}
],
"compute": """
const c = (inputs.choice || "").trim().toUpperCase();
if (c === "C") {
  const f = (inputs.temp * 9 / 5) + 32;
  return `${inputs.temp.toFixed(1)} C is equal to ${f.toFixed(1)} F`;
} else if (c === "F") {
  const cel = (inputs.temp - 32) * 5 / 9;
  return `${inputs.temp.toFixed(1)} F is equal to ${cel.toFixed(1)} C`;
} else {
  return `Invalid choice! Please enter C or F`;
}
""".strip()
},

"project07": {
"steps": [
    {"type": "input", "prompt": "Enter the First number: ", "key": "num1", "inputType": "number"},
    {"type": "input", "prompt": "Enter the operator (+ - * /): ", "key": "operator", "inputType": "text"},
    {"type": "input", "prompt": "Enter the Second number: ", "key": "num2", "inputType": "number"}
],
"compute": """
let result = 0;
let extra = "";
switch ((inputs.operator || "").trim()) {
  case '+': result = inputs.num1 + inputs.num2; break;
  case '-': result = inputs.num1 - inputs.num2; break;
  case '*': result = inputs.num1 * inputs.num2; break;
  case '/':
    if (inputs.num2 === 0) { extra = `You can't divide by zero!\n`; }
    else { result = inputs.num1 / inputs.num2; }
    break;
  default:
    extra = `Invalid Operator!\n`;
}
return `${extra}Result: ${result.toFixed(4)}`;
""".strip()
},

"project08": {
"steps": [
    {"type": "input", "prompt": "Type anything and press Enter to generate random numbers: ", "key": "_start", "inputType": "text"}
],
"compute": """
const RAND_MAX = 2147483647;
const raw = Math.floor(Math.random() * (RAND_MAX + 1));
const dice = Math.floor(Math.random() * 6) + 1;
const r1 = Math.floor(Math.random() * 51) + 50;
const r2 = Math.floor(Math.random() * 51) + 50;
const r3 = Math.floor(Math.random() * 51) + 50;
return `${raw}\n${RAND_MAX}\nDice roll: ${dice}\n${r1}\n${r2}\n${r3}`;
""".strip()
},

"project09": {
"steps": [
    {
        "type": "loopWhile",
        "prompt": "Guess a number between 1 - 100: ",
        "inputType": "number",
        "key": "guesses",
        "feedback": """
if (!inputs.secret) inputs.secret = Math.floor(Math.random() * 100) + 1;
if (value === inputs.secret) return {message: '!! CORRECT !!\\nThe answer was ' + inputs.secret, stop: true};
return {message: value < inputs.secret ? 'Too low!' : 'Too high!'};
""".strip()
    }
],
"compute": """
return `It took you ${inputs.guesses.length} tries`;
""".strip()
},

"project10": {
"steps": [
    {"type": "input", "prompt": "1. Rock\n2. Paper\n3. Scissors\nChoose: ", "key": "userChoice", "inputType": "number"}
],
"compute": """
const computerChoice = Math.floor(Math.random() * 3) + 1;
const names = {1: 'Rock', 2: 'Paper', 3: 'Scissors'};
let out = `You chose ${names[inputs.userChoice]}!\nComputer chose ${names[computerChoice]}!\n`;
if (inputs.userChoice === computerChoice) {
  out += "It's a TIE!";
} else if ((inputs.userChoice === 1 && computerChoice === 3) ||
           (inputs.userChoice === 2 && computerChoice === 1) ||
           (inputs.userChoice === 3 && computerChoice === 2)) {
  const beats = {1: 'Rock beats Scissors', 2: 'Paper beats Rock', 3: 'Scissors beats Paper'};
  out += `You WIN! ${beats[inputs.userChoice]}`;
} else {
  out += "You LOSE!";
}
return out;
""".strip()
},

"project11": {
"steps": [
    {
        "type": "loopWhile",
        "prompt": "\nSelect an option:\n1. Check Balance\n2. Deposit Money (type: 2 amount)\n3. Withdraw Money (type: 3 amount)\n4. Exit\n\nEnter your choice: ",
        "inputType": "text",
        "feedback": """
if (inputs.balance === undefined) inputs.balance = 0;
const parts = value.trim().split(/\\s+/);
const choice = parseInt(parts[0], 10);
const amount = parseFloat(parts[1]);
if (choice === 1) return {message: `Your current balance is: $${inputs.balance.toFixed(2)}`};
if (choice === 2) {
  if (isNaN(amount) || amount < 0) return {message: 'Invalid amount!'};
  inputs.balance += amount;
  return {message: `Successfully deposited $${amount.toFixed(2)}`};
}
if (choice === 3) {
  if (isNaN(amount) || amount < 0) return {message: 'Invalid amount!'};
  if (amount > inputs.balance) return {message: `Insufficient funds! Your balance is $${inputs.balance.toFixed(2)}`};
  inputs.balance -= amount;
  return {message: `Successfully withdrew $${amount.toFixed(2)}`};
}
if (choice === 4) return {message: 'Thank you for using the bank!', stop: true};
return {message: 'Invalid choice! Please select 1 - 4'};
""".strip()
    }
],
"compute": """
return `Final balance: $${inputs.balance.toFixed(2)}`;
""".strip()
},

"project12": {
"steps": [
    {"type": "input", "prompt": "What is the largest planet in the solar system?\n\nA. Jupiter\nB. Saturn\nC. Uranus\nD. Neptune\n\nEnter your choice: ", "key": "g1", "inputType": "text"},
    {"type": "input", "prompt": "What is the hottest planet?\n\nA. Mercury\nB. Venus\nC. Earth\nD. Mars\n\nEnter your choice: ", "key": "g2", "inputType": "text"},
    {"type": "input", "prompt": "What planet has the most moons?\n\nA. Earth\nB. Mars\nC. Jupiter\nD. Saturn\n\nEnter your choice: ", "key": "g3", "inputType": "text"},
    {"type": "input", "prompt": "Is the Earth flat?\n\nA. Yes\nB. No\nC. Maybe\nD. Sometimes\n\nEnter your choice: ", "key": "g4", "inputType": "text"}
],
"compute": """
const answers = ['A', 'B', 'D', 'B'];
const given = [inputs.g1, inputs.g2, inputs.g3, inputs.g4].map(v => (v || '').trim().toUpperCase());
let out = '';
let score = 0;
given.forEach((g, i) => {
  if (g === answers[i]) { out += `Q${i + 1}: CORRECT!\n`; score++; }
  else { out += `Q${i + 1}: Wrong! The answer was ${answers[i]}\n`; }
});
out += `\nYour score: ${score} out of 4`;
return out;
""".strip()
},

"project13": {
"steps": [
    {"type": "input", "prompt": "Press ENTER (type anything) to read the current time: ", "key": "_start", "inputType": "text"}
],
"compute": """
const now = new Date();
const pad = n => String(n).padStart(2, '0');
const time = `${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
return `${time}\n(In the real program this line overwrites itself every second using \\r - this simulator prints one snapshot.)`;
""".strip()
}

}


def main():
    try:
        with open(CONTENT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: {CONTENT_FILE} not found in this folder.")
        sys.exit(1)

    shutil.copy(CONTENT_FILE, CONTENT_FILE + ".bak")

    updated = []

    for lang in data.get("languages", []):
        for proj in lang.get("projects", []):
            pid = proj.get("id")
            if pid in PROJECTS:
                proj["steps"] = PROJECTS[pid]["steps"]
                proj["compute"] = PROJECTS[pid]["compute"]
                updated.append(pid)

    missing = sorted(set(PROJECTS.keys()) - set(updated))

    with open(CONTENT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Backup saved: {CONTENT_FILE}.bak")
    print(f"Updated {len(updated)} project(s): {', '.join(sorted(updated))}")
    if missing:
        print(f"NOT found in {CONTENT_FILE} (id mismatch?): {', '.join(missing)}")
    print("\nDon't forget: commit + push content.json to your portfolio-content")
    print("repo's main branch - the live app fetches it from GitHub, not this file.")


if __name__ == "__main__":
    main()
