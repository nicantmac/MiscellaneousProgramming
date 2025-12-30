useEffect

This folder contains examples demonstrating how the useEffect hook works in React. useEffect allows you to perform side effects in function components, such as:
---
Fetching data
Subscribing to events
Updating the DOM
Running logic when state or props change
---
What is useEffect?

useEffect runs after a component renders.
It lets your component react to changes in state, props, or lifecycle events.

There are only 3 valid patterns you will ever use in real React apps - 1️⃣ No dependency array, 2️⃣ Empty dependency array [], 3️⃣ Dependency array with values, 🔁 Multiple dependencies

Basic syntax:

useEffect(() => {
  // side effect logic
}, [dependencies]);
---
explain runs once when the component mounts, Runs whenever a specific value changes, Demonstrates fetching data from an API, Shows how to clean up side effects like timers or subscriptions.
---
Examples:

Fetching data

Logging something

Setting up timers

Subscribing / unsubscribing

Syncing state with props or URL
---
🧠 Key Concepts
Concept	Meaning
Dependency Array	Controls when effect runs
Cleanup Function	Runs before unmount or re-run
Empty Array []	Runs once
No Array	Runs every render
---
✅ When to Use useEffect

Use it for:

Fetching data

Timers / intervals

Event listeners

Syncing with external systems

Do not use it for:

Simple derived state

Basic calculations

Rendering logic

---
useEffect is for side effects, not rendering logic.

If something can be derived directly from props or state — don’t put it in an effect.

---
🔍 Summary Table
Dependency Array	Runs When
None	Every render
[]	Once (on mount)
[value]	When value changes
[a, b]	When a or b changes
---
🧠 Mental Model (Memorize This)

useEffect runs after render,
and reruns when anything in the dependency array changes.
---
