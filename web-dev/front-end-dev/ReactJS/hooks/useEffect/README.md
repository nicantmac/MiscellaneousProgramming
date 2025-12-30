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

Basic syntax:

useEffect(() => {
  // side effect logic
}, [dependencies]);
---
explain runs once when the component mounts, Runs whenever a specific value changes, Demonstrates fetching data from an API, Shows how to clean up side effects like timers or subscriptions.
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
